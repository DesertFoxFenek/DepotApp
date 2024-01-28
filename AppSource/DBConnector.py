import pyodbc
import User

class DBConnectorSerivice():
    def __init__(self):

        #parametry polaczenia csii ze localhost
        server = '.\SQLEXPRESS' #tcp:depot-app-db-server.database.windows.net,1433;
        database = 'DepotAppDb' #DepotAppDB
        username = User.User.login #DesertFoxFenek
        password = User.User.password #haslo Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
        self.conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;Trusted_Connection=no'



    def fetch_data_vehicle(self,SelectedDepotType):
        if SelectedDepotType == 1: SQLDepotType = 1
        elif SelectedDepotType == 2: SQLDepotType = 2
        elif SelectedDepotType == 3 : SQLDepotType = 3
        elif SelectedDepotType == 4 : SQLDepotType = 4
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


    def del_data(self): pass