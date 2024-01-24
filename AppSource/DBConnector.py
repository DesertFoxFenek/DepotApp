import pyodbc
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

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
        self.querry = f'SELECT * FROM TimetableDB'
        self.cursor.execute(self.querry)
        self.data = self.cursor.fetchall()
        self.connection.close()

        return self.data
    
    def fetch_brigade_table(self, depot):
        self.connection = pyodbc.connect(self.conn_str)
        self.cursor = self.connection.cursor()
        self.depot_table = depot+'DepotBrigadeTable'
        self.querry = f'SELECT * FROM {self.depot_table}'
        self.cursor.execute(self.querry)
        self.data = self.cursor.fetchall()
        self.connection.close()

        return self.data
    
    def fetch_user(self,given_login,given_pass):
        ph = PasswordHasher()
        self.data = []
        self.connection = pyodbc.connect(self.conn_str)
        self.cursor = self.connection.cursor()
        self.querry = f'SELECT * FROM Users WHERE Login = ?'
        self.cursor.execute(self.querry, given_login)
        self.temp = self.cursor.fetchall()
        for i in self.temp[0]:
            if type(i) == str:
                i.rstrip()
            self.data.append(i)

        print(self.data, given_pass)
        self.data_pass = ph.hash(self.data[2])

        print(self.data_pass, given_pass)

        try:
            ph.verify(self.data_pass, given_pass)
            print('sukces')
        except VerifyMismatchError: print('unluku')

    def del_data(self): pass