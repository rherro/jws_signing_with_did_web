import json
import jwt
from jwcrypto import jwk
import urllib.request
from encode_jwt import JWT_FILENAME, MESSAGE

BASE_URL = 'http://localhost:8000'
DID_WEB_URL = f'{BASE_URL}/.well-known/did.json'
DID_WEB_DOCUMENT_PATH = 'did.json'


def decode_jwt():
    encoded_jwt = read_jwt_from_file()
    did_web_document = retrieve_did_web_document()
    public_key_as_pem = extract_public_key_from_did_web(did_web_document)

    message = jwt.decode(encoded_jwt, public_key_as_pem, algorithms=["EdDSA"])
    return message


def read_jwt_from_file():
    try:
        with open(JWT_FILENAME, 'r') as f:
            encoded_jwt = f.read()
    except Exception as e:
        raise Exception(f"Unable to read JWT file: '{JWT_FILENAME}'")

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


if __name__ == '__main__':
    result = decode_jwt()
    print(f"The decoded message is:\n"
          f"{result['payload']}")

    if result['payload'] == MESSAGE:
        print('This message matches the original!\n')
    else:
        print('This message DOES NOT match the original!\n')
