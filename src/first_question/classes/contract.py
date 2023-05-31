class Contract:
    def __init__(self, identifier, debt):
        self.identifier = identifier
        self.debt = debt

    def __str__(self):
        return f"Identifier: {self.identifier}, Debt: {self.debt}"
