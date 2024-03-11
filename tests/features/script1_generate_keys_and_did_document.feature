Feature: Script 1 - Generate a key pair and did document
    In order to prepare the system
    As an administrator
    I want to generate a private/public keypair and store a valid DID document

    Scenario: Generate a key pair and save to disk
        When I generate a private/public keypair
        Then I see that a file is generated for both a private and public key
