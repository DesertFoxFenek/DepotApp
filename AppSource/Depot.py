import DBConnector

class Depot:
    def __init__(self, DepotName, DepotType):
        self.DepotName = DepotName
        self.DepotType = DepotType
        self.VehicleList = []

    def get_vehicles(self):
        connectDb = DBConnector.DBConnectorSerivice()
        temp_data = connectDb.fetch_data_vehicle(self.DepotName)

        for row in temp_data:
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
        temp_data = connectDb.fetch_data_timetables()

        self.LineList = [row for row in temp_data if row[4] == depot_type]

class Line():
    def __init__(self, number, start_place, finish_place, turn_around_time, type):
        self.number = number
        self.start_place = start_place
        self.finish_place = finish_place
        self.turn_around_time = turn_around_time
        self.type = type