import pyodbc
import pandas as pd
from datetime import datetime, timedelta

class DBConnectorSerivice():
    def __init__(self):

        #parametry polaczenia csii ze localhost
        server = '.\SQLEXPRESS' #tcp:depot-app-db-server.database.windows.net,1433;
        database = 'DepotAppDb' #DepotAppDB
        username ='TestUser' #DesertFoxFenek
        password = 'TestUser' #haslo Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
        self.conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;Trusted_Connection=yes'



    def fetch_data_vehicle(self,SelectedDepotType):
        if SelectedDepotType == 'Zajezdnia Borek': SQLDepotType = 1
        elif SelectedDepotType == 'Zajezdnia Olbin': SQLDepotType = 2
        elif SelectedDepotType == 'Zajezdnia Gaj' : SQLDepotType = 3
        elif SelectedDepotType == 'Zajezdnia Obornicka' : SQLDepotType = 4
        else: return None

        self.connection = pyodbc.connect(self.conn_str)
        self.cursor = self.connection.cursor()
        self.querry = f'SELECT * FROM VehiclesTable WHERE Depot = {SQLDepotType}'
        #self.querry = f'SELECT * FROM master.dbo.VehiclesTable'
        self.cursor.execute(self.querry)
        self.data = self.cursor.fetchall()
        self.connection.close()

        return self.data
    
    def fetch_data_timetables(self):
        self.connection = pyodbc.connect(self.conn_str)
        self.cursor = self.connection.cursor()
        #self.querry = f'SELECT * FROM TimetableDB WHERE Type LIKE {depot_type}'
        self.querry = f'SELECT * FROM TimetableDB WHERE Id = 2 OR Id = 4 OR Id = 6 OR Id = 7 OR Id = 10 OR Id = 12 OR Id = 13 OR Id = 14 OR Id = 18 OR Id = 19 OR Id = 20 OR Id = 21 OR Id = 22 OR Id = 23'
        self.cursor.execute(self.querry)
        self.data = self.cursor.fetchall()
        self.connection.close()

        return self.data
    
    def del_data(self): pass

Vh = DBConnectorSerivice()
tmp_vh = Vh.fetch_data_vehicle('Zajezdnia Borek')

Tb = DBConnectorSerivice()
tmp_tb = Tb.fetch_data_timetables()

tmp_df = []
for i in tmp_vh:
    txt = (i[0],i[4])
    tmp_df.append(txt)
vehicles_df = pd.DataFrame(tmp_df)
vehicles_df.columns = ['Id', 'Depot']

tmp_df = []
for i in tmp_tb:
    txt = (i[0], i[1], i[2], i[3])
    tmp_df.append(txt)
lines_df = pd.DataFrame(tmp_df)
lines_df.columns = ['NumerLinii', 'StartPlace', 'FinishPlace','TurnAroundTime']

# Tworzenie danych dla tabeli Przypisanie
assignment_data = {'Id': [], 'Brygada': [],'Linia': [], 'Id(Pojazdu)': [], 'CzasStartu': []}

start_time = datetime.strptime('04:00', '%H:%M')

assigned_vehicles = set()

for index, row in lines_df.iterrows():
    for brygada in range(1, 12):

        available_vehicles = set(vehicles_df['Id']) - assigned_vehicles
        if not available_vehicles:
            print("Brak dostępnych pojazdów.")
            break

        selected_vehicle = min(available_vehicles)
        assigned_vehicles.add(selected_vehicle)

        assignment_data['Id'].append(len(assignment_data['Id']) + 1)
        assignment_data['Brygada'].append(brygada)
        assignment_data['Linia'].append(row['NumerLinii'])
        assignment_data['Id(Pojazdu)'].append(selected_vehicle)
        assignment_data['CzasStartu'].append((start_time + timedelta(minutes=(brygada - 1) * 5)).strftime('%H:%M'))
    start_time += timedelta(minutes=3)

assignment_df = pd.DataFrame(assignment_data)

# Zapisanie danych do pliku CSV
vehicles_df.to_csv('vehicles.csv', index=False)
lines_df.to_csv('lines.csv', index=False)
assignment_df.to_csv('assignment.csv', index=False)
