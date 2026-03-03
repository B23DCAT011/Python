from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# 1. Cấu hình
key = b'HELLOTET' # Khóa phải đúng 8 bytes
cipher = DES.new(key, DES.MODE_ECB)

# 2. Dữ liệu (9 bytes - không chia hết cho 8)
data = b"Hello EVERYONE"
print(f"Data gốc ({len(data)} bytes): {data}")

# 3. Padding (Thêm đệm để đủ block 8 bytes)
padded_data = pad(data, DES.block_size)
print(f"Data sau padding ({len(padded_data)} bytes): {binascii.hexlify(padded_data)}")
# print(f"Data sau padding ({len(padded_data)} bytes): {padded_data.hex()}")
# Nhận xét về dữ liệu sau khi đệm có đặc điểm gì?

# 4. Mã hóa
ciphertext = cipher.encrypt(padded_data)
print(f"Ciphertext: {binascii.hexlify(ciphertext)}")
# print(f"Ciphertext: {ciphertext.hex()}")

# 5. Giải mã & Unpad
decipher = DES.new(key, DES.MODE_ECB)
decrypted_padded = decipher.decrypt(ciphertext)
decrypted_data = unpad(decrypted_padded, DES.block_size)
print(f"Decrypted: {decrypted_data.decode('utf-8')}")