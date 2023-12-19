import Depot

class Interface():
    def __init__(self) -> None:
        pass
    def show_depot_init_menu(self):
        print("Inicjalizowanie zajezdni.\nPodaj numer w ktorej bedzie operowane z wybranych nizej.\n1. Zajezdnia Borek\n2. Zajezdnia Olbin\n3. Zajezdnia Gaj\n4. Zajezdnia Obornicka")
        self.option = int(input())

        if self.option == 1: self.ThisDepot = Depot.Depot('Zajezdnia Borek','Tram')
        elif self.option == 2: self.ThisDepot = Depot.Depot('Zajezdnia Olbin','Tram')
        elif self.option == 3: self.ThisDepot = Depot.Depot('Zajezdnia Gaj','Tram')
        elif self.option == 4: self.ThisDepot = Depot.Depot('Zajezdnia Obornicka','Bus')
        else: print("Podano zla wartosc")
        
        self.ThisDepot.get_vehicles()

        print(f'Zaladowano {self.ThisDepot.DepotName}. Oraz tabor w liczbie: {self.ThisDepot.test_ilosc()}')

    def show_operating_lines(self):
        self.ThisDepotTypeLines = Depot.OperativeLines()
        self.ThisDepotTypeLines.get_lines(self.ThisDepot.DepotType)
        print(f'Znaleziono {len(self.ThisDepotTypeLines.LineList)} pasujacych linii')

    def use_programed_schedule(): pass
    def program_one_by_one(): pass