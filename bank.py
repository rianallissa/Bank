
from savingsaccount import SavingsAccount

class Bank(dict):
    """A collection of savings accounts indexed by name and pin."""

    def __init__(self):
        super().__init__()
        self.loadAccounts()

    def loadAccounts(self):
        """Pre-load some dummy accounts (you can add or change these)."""
        self["Rian|1234"] = SavingsAccount("Rian", "1234", 100.0)
        self["Alice|1111"] = SavingsAccount("Alice", "1111", 250.0)
        self["Bob|2222"] = SavingsAccount("Bob", "2222", 500.0)

    def get(self, name, pin):
        """Returns the account object matching name and pin, or None."""
        return super().get(name + "|" + pin, None)


def createBank():
    """Factory function to return a new Bank instance."""
    return Bank()


   
