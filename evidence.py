from Pojisteny import Pojisteny
class Evidence:

    def __init__(self):
        self.pojisteni = []

    
    def vytvorit_pojisteneho(self):

        """
            tvorba pojisteneho
        """
        
        jmeno = input('\nZadej jméno: ')
        prijmeni = input('Zadej příjmení: ')
        vek = int(input('Zadej věk: '))
        telefon = input('Zadej telefon: ')
        print("Nový pojištěnec zaevidován.\n")
    
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(pojisteny)
    
    def vyhledat_pojisteneho(self):

        """
            hledani pojisteneho
        """

        hledane_jmeno = input('Zadej jméno: ')
        hledane_prijmeni = input('Zadej příjmení: ')
    
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == hledane_jmeno and pojisteny.prijmeni == hledane_prijmeni:
                print(str(pojisteny))
                break
        else:
            print('Pojištěný nenalezen, zkuste prosím znovu.')
    
    def vypis_pojisteneho(self):

        """
            vypis pojistenych
        """

        for pojisteny in self.pojisteni:
            print(str(pojisteny))
    
    def main(self):

        """ 
            volby moznosti
        """
        
        while True:
            print('==========================\nEVIDENCE POJISTNÉ UDÁLOSTI\n==========================\n')
            volba = input('Zvolte možnost:\n'
                '[1] Vytvořit nového pojištěného\n'
                '[2] Vyhledat pojištěného\n'
                '[3] Vypis pojištěných\n'
                '[4] Konec aplikace\n'
                '\n'
                'Zadej volbu: ')
            
            if volba == '1':
                Evidence.vytvorit_pojisteneho(self)
            elif volba == '2':
                Evidence.vyhledat_pojisteneho(self)
            elif volba == '3':
                Evidence.vypis_pojisteneho(self)
            elif volba == '4':
                print('Konec aplikace.\n')
                break
            else:
                print('\nNeplatná volba, zkuste prosím znovu...\n')

