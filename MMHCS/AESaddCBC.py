from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# 1. Tạo khóa ngẫu nhiên 16 bytes (128 bit)
key = get_random_bytes(16)

# 2. Hàm Mã hóa (Tự động tạo IV)
def encrypt_aes(msg, key):
    # Tạo IV ngẫu nhiên mỗi lần mã hóa
    iv = get_random_bytes(AES.block_size) # 16 bytes
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Đệm dữ liệu trước khi mã hóa
    padded_data = pad(msg, AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    # Trả về IV + Ciphertext (IV không cần bí mật, chỉ cần duy nhất)
    return iv + encrypted

# 3. Hàm Giải mã
def decrypt_aes(iv_and_ciphertext, key):
    # Tách IV (16 byte đầu) và Ciphertext (phần còn lại)
    iv = iv_and_ciphertext[:16]
    ciphertext = iv_and_ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = cipher.decrypt(ciphertext)
    return unpad(padded_data, AES.block_size)

# --- Thực thi ---
msg = b"Sinh vien PTIT hoc Mat ma hoc"
print(f"Original: {msg}")

# Mã hóa
encrypted_blob = encrypt_aes(msg, key)
print(f"Gửi đi (Hex): {encrypted_blob.hex()}")

# Giải mã
recovered = decrypt_aes(encrypted_blob, key)
print(f"Khôi phục: {recovered.decode('utf-8')}")


# Setup chung
data_lap = b"Secret!!" * 4 # 32 bytes giống hệt nhau

# 1. Thử với AES-ECB
cipher_ecb = AES.new(key, AES.MODE_ECB)
out_ecb = cipher_ecb.encrypt(data_lap)
print("\n--- AES ECB Mode (Lộ mẫu) ---")
print(f"Block 1: {out_ecb[:16].hex()}")
print(f"Block 2: {out_ecb[16:].hex()}")
# NHẬN XÉT VỀ KẾT QUẢ

# 2. Thử với AES-CBC
iv = get_random_bytes(16)
cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
out_cbc = cipher_cbc.encrypt(data_lap)
print("\n--- AES CBC Mode (Che mẫu) ---")
print(f"Block 1: {out_cbc[:16].hex()}")
print(f"Block 2: {out_cbc[16:].hex()}")
# NHẬN XÉT VỀ KẾT QUẢ