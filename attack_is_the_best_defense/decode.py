import base64

# Base64 encoded values
encoded_password = "bXlwYXNzd29yZDk4OTgh"
encoded_username = "bXlsb2dpbg=="

# Decode base64 values
password = base64.b64decode(encoded_password).decode("utf-8")
username = base64.b64decode(encoded_username).decode("utf-8")

# Print decoded values
print("Decoded username:", username)
print("Decoded password:", password)
