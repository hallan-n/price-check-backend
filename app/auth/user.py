from passlib.context import CryptContext

crypt_context = CryptContext(schemes=["sha256_crypt"])
crypt_context.hash("password")

