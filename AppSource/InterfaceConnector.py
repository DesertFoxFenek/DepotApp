import Depot
import Tasks
import datetime as dt
import User

class Interface():
    def __init__(self):
        self.brigades_list = []

    def login(self):
        print('login: ')
        username = input()
        print('password: ')
        password = input()
        self.user = User.User()

        print(self.user.login_user(username,password))
        print("Inicjalizowanie zajezdni.\nPodaj numer w ktorej bedzie operowane z wybranych nizej.")
        for i in self.user.depots:
            print(str(i)+'\n')

        self.option = int(input()) - 1
        self.depot = self.user.depots[self.option]
        self.ThisDepot = Depot.Depot(self.depot[0],self.depot[1],self.depot[2])
        self.ThisDepot.get_vehicles()
        print(f'Zaladowano {self.ThisDepot.DepotName}. Oraz tabor w liczbie: {len(self.ThisDepot.VehicleList)}')

    def show_operating_lines(self):
        self.ThisDepotTypeLines = Depot.OperativeLines()
        self.ThisDepotTypeLines.get_lines(self.ThisDepot.DepotType)
        print(f'Znaleziono {len(self.ThisDepotTypeLines.LineList)} pasujacych linii')

    def use_programed_schedule(self):
        self.BrigadesOnLinesObj = Depot.ImportedBrigade()
        self.BrigadesOnLines = self.BrigadesOnLinesObj.recive_brigades(self.ThisDepot.DepotName.split()[1])
        for row in self.BrigadesOnLines:
            print(row)

    def select_line(self):
        i = 1
        for row in self.ThisDepotTypeLines.LineList:
            print(f'Linia {row.Id} - {i}')
            i+=1

        print(f'Wybierz numer przy linii.')
        choosen = int(input())
        self.line = self.ThisDepotTypeLines.LineList[choosen - 1]

        return self.line
    
    def select_vehicle(self):
        i = 1
        for row in self.ThisDepot.VehicleList:
            print(f'Pojazd numer {i}\n Numer Taborowy: {row.Id}  Producent: {row.Name} Model: {row.Model}')
            i+=1

        print(f'Wybierz pojazd.')
        choosen = int(input())
        self.vehicle = self.ThisDepot.VehicleList[choosen - 1]

        return self.vehicle


    def program_one_by_one(self):
        self.selected_line = self.select_line()
        self.selected_vehicle = self.select_vehicle()

        print(f'Planowanie wyjazdow. Godzina aktualna: {dt.datetime.now()}')
        print(f'Podaj czas wyjazdu z zajezdni i ilosc zaplanowanych przejazdow.')
        print(f'Godzina:')
        self.time_h = int(input())
        print(f'Minuta:')
        self.time_m = int(input())
        print(f'Ilosc zaplanowanych przejazdow: ')
        self.cycles = int(input())
        print(f'Brygada: ')
        self.brigade = int(input())

        self.Created_Brigade = Tasks.RouteWorker(self.selected_vehicle,self.selected_line,self.brigade)
        self.Created_Brigade.create_day_schedule(self.time_h,self.time_m,self.cycles)

        print(f'Utworzono\nLinia: {self.Created_Brigade.route[0]}\nBrygada: {self.Created_Brigade.brigade}\nPojazd: {self.Created_Brigade.vehicle.Name} {self.Created_Brigade.vehicle.Model} {self.Created_Brigade.vehicle.Id}\nGodzina rozpoczecia pracy: {self.Created_Brigade.timestart_on_depot}\nGodzina rozpoczecia pracy na linii: {self.Created_Brigade.timestart_on_line}\nGodzina zjazdu na zajezdnie: {self.Created_Brigade.timeend}')

        self.brigades_list.append(self.Created_Brigade)