import json
from src.generate_key_pair import generate_key_pair

DEFAULT_DID = 'did:web:example.com'


def generate_did_web():
    key = generate_key_pair()
    public_key_jwk = json.loads(key.export_public())

    content = create_did_document_contents(DEFAULT_DID, public_key_jwk)

    with open('did.json', 'w') as f:
        f.write(json.dumps(content, indent=4))


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
