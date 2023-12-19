import pyodbc

class DBConnectorSerivice():
    def __init__(self):

        #parametry polaczenia csii ze localhost
        server = '.\SQLEXPRESS'
        database = 'DepotAppDb'
        username ='TestUser'
        password = 'TestUser'
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
    
    def del_data(self): pass