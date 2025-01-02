class Holdings:
    def __init__(self, issuer, title_of_class, shares:int, marketValue:float):
        self._issuer = issuer
        self._title_of_class = title_of_class
        self._shares:int = shares
        self._values:float = marketValue

    @property
    def Issuer(self):
        return self._issuer

    @property
    def TitleOfClass(self):
        return self._title_of_class

    @property
    def Shares(self):
        return self._shares

    @property
    def MarketValue(self):
        return self._values

    def __repr__(self):
        return f"Holdings(Issuer={self.Issuer}, TitleOfClass={self.TitleOfClass}, Shares={self.Shares}, Values={self.Values})"
