## JWS Signing and Verification Project utilitizing a W3C DID:WEB

### Requirements
To use this project, you will need to have [Docker](https://docs.docker.com/engine/install/) installed.

----

### Setup
To setup the environment, clone this project and run the following:
```shell
git clone git@github.com:rherro/jws_signing_with_did_web.git
docker build -t demo .
docker run -it --rm demo
```

Then at the docker prompt, activate the python virtual environment:
```
source .venv/bin/activate
```

----

### Running the scripts
1. Generate a private/public keypair and create an associated DID document by running the following:
    ```
    python src/generate_did.py
    ```

2. Start the Django webserver as a background process by running the following:
    ```
    nohup python src/django_web_server/manage.py runserver &
    ```

3. Create a JWT using the private key from step 1 by running the following:
    ```
    python src/encode_jwt.py
    ```

4. Decode the JWT (from step 3) using the public key from the DID:WEB document (from step 2) by running the following:
    ```
    python src/decode_jwt.py
    ```
