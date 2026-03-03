from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

hex_ciphertext = "c28596a49e69fb10"
key = b'Student1'

# 2. Chuyển đổi chuỗi Hex thành Bytes
ciphertext_bytes = bytes.fromhex(hex_ciphertext)

# 3. Khởi tạo đối tượng DES với chế độ ECB
decipher = DES.new(key, DES.MODE_ECB)

# 4. Thực hiện giải mã
decrypted_padded = decipher.decrypt(ciphertext_bytes)

# 5. Loại bỏ Padding để lấy nội dung gốc
# Vì DES làm việc theo block 8 bytes, thông thường dữ liệu sẽ được pad
print(decrypted_padded)
password = unpad(decrypted_padded, DES.block_size)
print(f"Mật khẩu gốc là: {password.decode('utf-8')}")
