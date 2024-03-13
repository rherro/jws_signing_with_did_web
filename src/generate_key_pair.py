import os

from jwcrypto import jwk

PEM_PASSWORD = 'WEAK_PASSWORD_FOR_DATA_AT_REST'.encode()
PRIVATE_KEY_FILENAME = 'data/private_key.pem'
PUBLIC_KEY_FILENAME = 'data/public_key.pem'


def generate_key_pair():
    key = jwk.JWK.generate(kty='OKP', crv='Ed25519')
    save_key_pair_to_disk(key)
    return key


def save_key_pair_to_disk(key):
    private_key = key.export_to_pem(private_key=True, password=PEM_PASSWORD)
    with open(PRIVATE_KEY_FILENAME, 'wb') as f:
        f.write(private_key)

    public_key = key.export_to_pem(private_key=False)
    with open(PUBLIC_KEY_FILENAME, 'wb') as f:
        f.write(public_key)


def read_private_key_from_disk():
    try:
        with open(PRIVATE_KEY_FILENAME, 'rb') as f:
            data = f.read()

            key = jwk.JWK()
            key.import_from_pem(data=data, password=PEM_PASSWORD)
            return key.export_to_pem(private_key=True, password=None)
    except Exception:
        raise Exception('Unable to read private key!')
