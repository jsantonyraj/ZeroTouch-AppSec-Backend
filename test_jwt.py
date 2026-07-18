from app.security.jwt_handler import create_access_token

token = create_access_token(
    {
        "sub": "sahaya@example.com"
    }
)

print(token)
