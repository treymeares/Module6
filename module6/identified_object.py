# Trey Meares M3 Project

class IdentifiedObject:
    # Abstract class for oid, __eq__, and __hash__
    @property
    def oid(self):
        '''
        read-only property called oid (for "object id" since id is a built-in function in Python)
        and use it for equality tests and hashing.
        :return:read only (private) oid
        '''
        return self._oid

    def __init__(self, id):
        '''
        constructor for class to set the id.
        :param oid:
        '''
        self._oid = id

    def __eq__(self, other):
        '''
        __eq__ class oveririding equal for oid
        :param other: take in other param for comparison
        :return: true if equal or false if not.
        '''
        if self is other:
            return True
        elif hasattr(other, "_oid"):
            return self._oid == other._oid
        else:
            return False

    def __hash__(self):
        '''
        oveririding __hash__ class
        :return: hash for oid
        '''
        return hash(self.oid)
