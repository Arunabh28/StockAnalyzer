class ChangeInData:
    def __init__(self, issuer:str, change_type:str, quantity:int|float):
        self._issuer = issuer
        self._ChangeType = change_type
        self._values = quantity

    @property
    def Issuer(self):
        return self._issuer

    @property
    def Quantity(self):
        return self._values
    
    @property
    def Change_Type(self):
        return self._ChangeType

    def __repr__(self):
        return f"ChangeInData(Issuer={self.Issuer}, Change_Type={self.Change_Type},  Quantity={self.Values})"
