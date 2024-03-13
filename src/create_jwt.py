import jwt
from src.generate_key_pair import read_private_key_from_disk

PAYLOAD = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna 
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""


def create_jwt():
    private_key = read_private_key_from_disk()
    encoded_jwt = jwt.encode({"payload": PAYLOAD}, private_key, algorithm="EdDSA")

    with open('jwt', 'w') as f:
        f.write(encoded_jwt)

    return encoded_jwt
