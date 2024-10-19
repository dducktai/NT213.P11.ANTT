import hashlib

hash_to_find = "a7c5bbb9aee1c49beb8819da6b5855aea43d0a6cf58b1b8bcf703ec74a4b359d" 

file_path = "rockyou.txt"

# Hàm băm bằng SHA-256
def hash_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Đọc file rockyou.txt và kiểm tra từng mật khẩu
with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    found = False  # Biến kiểm tra xem mật khẩu có được tìm thấy không
    for line in file:
        password = line.strip()
        hashed_password = hash_sha256(password)

        if hashed_password == hash_to_find:
            print(f"Mật khẩu gốc là: {password}")
            found = True 
            break
    if not found:
        print("Không tìm thấy mật khẩu phù hợp.")
