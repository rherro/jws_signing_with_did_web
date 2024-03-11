import json
from jwcrypto import jwk

DEFAULT_DID = 'did:web:example.com'
PEM_PASSWORD = 'WEAK_PASSWORD_FOR_DATA_AT_REST'.encode()


def generate_key_pair():
    key = jwk.JWK.generate(kty='OKP', crv='Ed25519')
    save_key_pair_to_disk(key)
    return key


def save_key_pair_to_disk(key):
    private_key = key.export_to_pem(private_key=True, password=PEM_PASSWORD)
    with open('private_key.pem', 'wb') as f:
        f.write(private_key)

    public_key = key.export_to_pem(private_key=False)
    with open('public_key.pem', 'wb') as f:
        f.write(public_key)


def generate_did_web():
    key = generate_key_pair()
    public_key_jwk = key.export_public()

    content = create_did_document_contents(DEFAULT_DID, public_key_jwk)

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
