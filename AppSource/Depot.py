import DBConnector

class Depot:
    def __init__(self, DepotNumber, DepotName, DepotType):
        self.DepotNumber = DepotNumber
        self.DepotName = DepotName
        self.DepotType = DepotType
        self.VehicleList = []

    def get_vehicles(self):
        connectDb = DBConnector.DBConnectorSerivice()
        self.temp_data = connectDb.fetch_data_vehicle(self.DepotNumber)

        for row in self.temp_data:
            self.VehicleList.append(Vehicle(row[0],row[1],row[2]))

    def test_ilosc(self):
        return len(self.VehicleList)

class Vehicle:
    def __init__(self,Id, Name, Model):
        self.Id = Id
        self.Name = Name
        self.Model = Model

class OperativeLines():
    def __init__(self):
        self.LineList = []

    def get_lines(self,depot_type):
        connectDb = DBConnector.DBConnectorSerivice()
        self.temp_data = connectDb.fetch_data_timetables()

        self.LineList = [row for row in self.temp_data if row[4] == depot_type]

class Line():
    def __init__(self, number, start_place, finish_place, turn_around_time, type):
        self.number = number
        self.start_place = start_place
        self.finish_place = finish_place
        self.turn_around_time = turn_around_time
        self.type = type

class ImportedBrigade():
    def __init__(self):
        self.BrigadeData = []

    def recive_brigades(self, Depot_Name):
        connectDb = DBConnector.DBConnectorSerivice()
        self.temp_data = connectDb.fetch_brigade_table(Depot_Name)       

        for row in self.temp_data:
            self.BrigadeData.append(row)

        return self.BrigadeData