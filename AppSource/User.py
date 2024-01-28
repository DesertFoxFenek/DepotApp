import pyodbc

class User:

    login = ''
    password =''

    def __init__(self):
        #parametry polaczenia csii ze localhost
        self.server = '.\SQLEXPRESS' #tcp:depot-app-db-server.database.windows.net,1433;
        self.database = 'DepotAppDb' #DepotAppDB
        self.depots = []
        self.depot_num = None

    def login_user(self, g_login, g_password):
        self.login = g_login
        self.password = g_password

        try:
            self.conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.login};PWD={self.password};TrustServerCertificate=yes;Trusted_Connection=no'
            self.connection = pyodbc.connect(self.conn_str)
            self.cursor = self.connection.cursor()
            self.querry = f'SELECT * FROM WroclawDepots'
            self.cursor.execute(self.querry)
            self.data = self.cursor.fetchall()
            self.connection.close()

            User.login = g_login
            User.password = g_password
            for row in self.data: self.depots.append(row)

            print('Zalogowano pomyslnie')
            return self.depots

        except Exception as ex:
            return ex
        
    def get_dep_number(self, number): self.depot_num = number