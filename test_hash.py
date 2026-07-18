from app.security.security import hash_password
from app.security.security import verify_password

password = "Welcome@123"

hashed = hash_password(password)

print("Original :", password)
print("Hash     :", hashed)

print(
    verify_password(
        password,
        hashed
    )
)
