Feature: Part 1 - Generate a key pair and DID document
    As an administrator
    I want to generate a private/public keypair and store a valid DID document
    In order to prepare the system for message handling

    Scenario: Generate a key pair and save to disk
        When I generate a private/public keypair
        Then I see that a file is generated for both a private and public key

    Scenario: Generate a did:web document from the saved keypair
        When I generate a did:web document from the saved keypair
        Then I see that a file is generated containing the did:web document
