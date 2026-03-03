from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def count_diff_bits(b1, b2):
    # Hàm đếm số bit khác nhau giữa 2 chuỗi bytes
    diff = 0
    for byte1, byte2 in zip(b1, b2):
        xor_val = byte1 ^ byte2
        diff += bin(xor_val).count('1')
    return diff

key = get_random_bytes(16)
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)

# Trường hợp 1: Bản gốc
msg1 = pad(b'00000000'*2, AES.block_size)
c1 = cipher.encrypt(msg1)

# Trường hợp 2: Thay đổi CHỈ 1 BIT ở đầu vào (bit cuối cùng từ 0 -> 1)
msg2 = pad(b'0000000000000001', AES.block_size)
# Lưu ý: Cần tạo lại đối tượng cipher vì MODE_CBC có trạng thái
cipher = AES.new(key, AES.MODE_CBC, iv)
c2 = cipher.encrypt(msg2)

print(f"Cipher 1: {c1.hex()}")
print(f"Cipher 2: {c2.hex()}")

diff_bits = count_diff_bits(c1, c2)
total_bits = len(c1) * 8
print(f"Số bit thay đổi: {diff_bits}/{total_bits} (~{diff_bits/total_bits*100:.2f}%)")
# Nhận xét về Kết quả: Một sự thay đổi nhỏ ở đầu vào dẫn đến thay đổi lớn ở đầu ra