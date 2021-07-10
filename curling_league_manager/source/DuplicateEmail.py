class DuplicateEmail(Exception):
    """
    Exception class for duplicate email. Throws exception when email equal
    to another email.
    """
    def __init__(self, email):
        self.email = email
