import os
import json
from jwcrypto import jwk

PEM_PASSWORD = 'WEAK_PASSWORD_FOR_DATA_AT_REST'.encode()


def generate_key_pair():
    key = jwk.JWK.generate(kty='OKP', crv='Ed25519')
    public_key = key.export_to_pem(private_key=False)
    private_key = key.export_to_pem(private_key=True, password=PEM_PASSWORD)

    with open('private_key.pem', 'wb') as f:
        f.write(private_key)

    with open('public_key.pem', 'wb') as f:
        f.write(public_key)

    return key


def generate_did_web():
    key = generate_key_pair()
    if not os.path.isfile('private_key.pem') or not os.path.isfile('public_key.pem'):
        raise RuntimeError('Unable to generate did document because no keys exist!')

    did = 'did:web:example.com'
    public_key_jwk = key.export_public()

    content = create_did_document_contents(did, public_key_jwk)

    with open('did.json', 'wb') as f:
        f.write(json.dumps(content).encode())


def create_did_document_contents(did, public_key_jwk):
    content = {
        "@context": [
            "https://www.w3.org/ns/did/v1",
            "https://w3id.org/security/suites/jws-2020/v1"
        ],
        "id": did,
        "verificationMethod": [
            {
                "id": f"{did}#key-0",
                "type": "JsonWebKey2020",
                "controller": did,
                "publicKeyJwk": public_key_jwk
            }
        ],
        "authentication": [
            f"{did}#key-0",
        ],
        "assertionMethod": [
            f"{did}#key-0",
        ],
        "keyAgreement": [
            f"{did}#key-0",
        ]
    }
    return content
