class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        if not isinstance(account, Account):
            return False
        self.account.append(account)
        return True

    def find_account(self, identifier):
        is_int = isinstance(identifier, int)
        for account in self.account:
            if (is_int and account.id == identifier) or account.name == identifier:
                return account
        return None

    def transfer(self, origin, dest, amount: float):
        """
        @origin:  int(id) or str(name) of the first account
        @dest:    int(id) or str(name) of the destination account
        @amount:  float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if not isinstance(amount, float) or amount < 0:
            return False
        account_origin = self.find_account(origin)
        account_dest = self.find_account(dest)
        if account_origin is None or account_dest is None:
            return False
        if self.is_corrupted(account_origin) or self.is_corrupted(account_dest):
            return False
        if account_origin.value < amount:
            return False
        account_origin.transfer(-amount)
        account_dest.transfer(amount)
        return True

    def is_corrupted(self, account):
        """
        Check if an account is corrupted
        @account: account
        @return True if the account is corrupted, False if it's not
        """
        attributes = dir(account)
        # Even number of attributes
        if len(attributes) % 2 == 0:
            return True
        # Has *no* attributes starting with zip or addr
        # -- and has an attribute starting with b
        has_zip = False
        has_addr = False
        for p in attributes:
            if p.startswith('b'):
                return True
            else:
                has_zip = p.startswith('zip') if not has_zip else True
                has_addr = p.startswith('addr') if not has_addr else True
        if not has_zip or not has_addr:
            return True
        # Doesn't have the attributes `name`, `id` or `value
        if 'id' not in attributes or 'name' not in attributes or 'value' not in attributes:
            return True
        return False

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        account = self.find_account(account)
        if account is None:
            return False
        has_zip = False
        has_addr = False
        for p in dir(account):
            if p.startswith('b'):
                delattr(account, p)
            else:
                has_zip = p.startswith('zip') if not has_zip else True
                has_addr = p.startswith('addr') if not has_addr else True
        setattr(account, 'zip', 34000 if not has_zip else account.zip)
        setattr(account, 'addr',
                '1234-abcdef-5678-wxyz' if not has_addr else account.addr)
        attributes = dir(account)
        if 'id' not in attributes:
            setattr(account, 'id', len(self.account))
        if 'name' not in attributes:
            setattr(account, 'name', 'Account#{}'.format(account.id))
        if 'value' not in attributes:
            setattr(account, 'value', 0)
        if len(dir(account)) % 2 == 0:
            new_attribute = 'my_super_attribute'
            while new_attribute in attributes:
                new_attribute += 'e'
            setattr(account, new_attribute, True)
        return True


if __name__ == '__main__':
    a1 = Account('Francois', value=12500)
    a1.value = 12500
    a2 = Account('Jean')
    a2.value = 12500
    a3 = Account('Francis')
    a3.value = 12500
    bank = Bank()
    bank.add(a1)
    bank.add(a2)
    bank.add(a3)

    print('example')
    print(dir(a1))
    print(dir(a2))
    bank.transfer(a1.name, a2.name, 12.0)
    print(dir(a1))
    print(dir(a2))

    del a1.id
    print('\na1 - id')
    print(dir(a1))
    bank.transfer(a1.name, a2.name, 12.0)
    print(dir(a1))

    setattr(a1, 'my_super_attribute', False)
    print('\na1 - my_super_attribute')
    print(dir(a1))
    bank.transfer(a1.name, a2.name, 12.0)
    print(dir(a1))

    setattr(a1, 'b_is_b', 42)
    print('\na1 - starts with b')
    print(dir(a1))
    bank.transfer(a1.name, a2.name, 12.0)
    bank.fix_account(a1.name)
    bank.transfer(a1.name, a2.name, 12.0)
    print(dir(a1))
