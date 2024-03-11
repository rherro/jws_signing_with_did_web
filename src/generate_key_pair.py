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
