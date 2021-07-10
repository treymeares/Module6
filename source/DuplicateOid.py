class DuplicateOID(Exception):
    """
    Exception clsss for duplicate OID. Throws excetpion when OID==Other.OID
    """
    def __init__(self, oid):
        self.oid = oid
