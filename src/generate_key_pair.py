from jwcrypto import jwk


def generate_key_pair():
    key = jwk.JWK.generate(kty='OKP', crv='Ed25519')
    public_key = key.export_to_pem(private_key=False)
    private_key = key.export_to_pem(private_key=True, password=None)

    with open('private_key.pem', 'wb') as f:
        f.write(private_key)

    with open('public_key.pem', 'wb') as f:
        f.write(public_key)
