from savingsaccount import SavingsAccount


class Bank(object):
    """This class represents a bank as a collection of savings accounts."""

    def __init__(self):
        """Creates an empty bank."""
        self._accounts = []

    def add(self, account):
        """Adds a savings account to the bank."""
        self._accounts.append(account)

    def remove(self, name):
        """Removes an account by name."""
        for account in self._accounts:
            if account.name == name:
                self._accounts.remove(account)
                return True
        return False

    def get(self, name):
        """Returns the account with the given name or None."""
        for account in self._accounts:
            if account.name == name:
                return account
        return None

    def __str__(self):
        """Returns string representation of the bank, sorted by name."""
        return "\n".join(str(account) for account in sorted(self._accounts))


def main():
    """A simple test of the Bank class."""
    bank = Bank()
    
    # Add some test accounts
    bank.add(SavingsAccount("Zoe", "111", 1000))
    bank.add(SavingsAccount("Alice", "222", 750))
    bank.add(SavingsAccount("Bob", "333", 500))
    bank.add(SavingsAccount("Charlie", "444", 1250))

    print("Accounts sorted by name:\n")
    print(bank)


if __name__ == "__main__":
    main()
