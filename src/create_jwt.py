import json
import jwt
from jwcrypto import jwk
from src.generate_key_pair import read_private_key_from_disk
import urllib.request

BASE_URL = 'http://localhost:8000'
DID_WEB_URL = f'{BASE_URL}/.well-known/did.json'
DID_WEB_DOCUMENT_PATH = 'did.json'

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

    with open('jwt', 'w') as f:
        f.write(encoded_jwt)

    return encoded_jwt


def decode_jwt():
    with open('jwt', 'r') as f:
        encoded_jwt = f.read()

    try:
        did_web_document = urllib.request.urlopen(DID_WEB_URL).read()
    except Exception as e:
        raise Exception(f"Unable to retrieve DID:WEB from '{DID_WEB_URL}'")

    did_web_json = json.loads(did_web_document.decode())
    publicKeyJwk = did_web_json["verificationMethod"][0]['publicKeyJwk']
    key = jwk.JWK(**publicKeyJwk)
    public_key = key.export_to_pem()

    message = jwt.decode(encoded_jwt, public_key, algorithms=["EdDSA"])
    return message


    # read jwt from file
    # get DID:WEB document
    # extract public key
    # decode
    # return payload