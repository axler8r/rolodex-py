from rolodex.email_address import EmailAddress, EmailAddressKind, create


def test_create_email_address():
    ea = EmailAddress('someone@examle.com', EmailAddressKind.Office)
    assert ea.address == 'someone@examle.com' and \
        ea.kind == EmailAddressKind.Office


def test_create_nil_email_address():
    ea = EmailAddress()
    assert ea.address == '' and \
        ea.kind == EmailAddressKind.Unspecified


def test_create_email_address_with_function():
    ea = create('someone@example.com', EmailAddressKind.Office)
    assert ea.address == 'someone@example.com' and \
        ea.kind == EmailAddressKind.Office
