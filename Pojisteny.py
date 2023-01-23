class Pojisteny:

    """
        vola urcite atributy
    """
    
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon
    
    def __str__(self):
        """ 
            doplneni atributu
        """
        return f'{self.jmeno} {self.prijmeni}, {self.vek} let, {self.telefon}'