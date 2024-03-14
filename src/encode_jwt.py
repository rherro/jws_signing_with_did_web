import jwt
from generate_key_pair import read_private_key_from_disk

JWT_FILENAME = 'data/jwt'

MESSAGE = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna 
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

PAYLOAD = {"payload": MESSAGE}


def encode_jwt():
    private_key = read_private_key_from_disk()
    encoded_jwt = jwt.encode(PAYLOAD, private_key, algorithm="EdDSA")
    save_jwt_to_file(encoded_jwt)
    return encoded_jwt


def save_jwt_to_file(encoded_jwt):
    with open(JWT_FILENAME, 'w') as f:
        f.write(encoded_jwt)


if __name__ == '__main__':
    encode_jwt()
    print(f"The following file has been created:\n"
          f"    1. {JWT_FILENAME}\n")
