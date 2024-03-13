import json
import jwt
from jwcrypto import jwk
from src.generate_key_pair import read_private_key_from_disk
import urllib.request

BASE_URL = 'http://localhost:8000'
DID_WEB_URL = f'{BASE_URL}/.well-known/did.json'
DID_WEB_DOCUMENT_PATH = 'did.json'
JWT_FILENAME = 'data/jwt'

MESSAGE = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna 
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

PAYLOAD = {"payload": MESSAGE}


def create_jwt():
    private_key = read_private_key_from_disk()
    encoded_jwt = jwt.encode(PAYLOAD, private_key, algorithm="EdDSA")
    save_jwt_to_file(encoded_jwt)
    return encoded_jwt


def decode_jwt():
    encoded_jwt = read_jwt_from_file()
    did_web_document = retrieve_did_web_document()
    public_key_as_pem = extract_public_key_from_did_web(did_web_document)

    message = jwt.decode(encoded_jwt, public_key_as_pem, algorithms=["EdDSA"])
    return message


def save_jwt_to_file(encoded_jwt):
    with open(JWT_FILENAME, 'w') as f:
        f.write(encoded_jwt)


def read_jwt_from_file():
    with open(JWT_FILENAME, 'r') as f:
        encoded_jwt = f.read()
    return encoded_jwt


def retrieve_did_web_document():
    try:
        did_web_document = urllib.request.urlopen(DID_WEB_URL).read()
    except Exception as e:
        raise Exception(f"Unable to retrieve DID:WEB from '{DID_WEB_URL}'")

    return did_web_document


def extract_public_key_from_did_web(did_web_document):
    did_web_json = json.loads(did_web_document.decode())
    public_key_jwk_json = did_web_json["verificationMethod"][0]['publicKeyJwk']
    public_key_jwk = jwk.JWK(**public_key_jwk_json)
    public_key_as_pem = public_key_jwk.export_to_pem()
    return public_key_as_pem
