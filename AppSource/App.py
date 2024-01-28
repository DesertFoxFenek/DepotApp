import InterfaceConnector

class App:

    NAME = 'DepotApp'
    VERSION = '0.2.24.01' #wydanie.wersja.rok.miesiac

    def __init__(self) -> None:
        pass
    def Run(self):
        while(True):
            ThisInterface = InterfaceConnector.Interface()
            ThisInterface.login()
            ThisInterface.show_operating_lines()
            ThisInterface.use_programed_schedule()
            #ThisInterface.program_one_by_one()
            input()

    def Quit(self):
        self.QUIT = -1
        return self.QUIT
    
    def Info(self):
        txt = 'Program {}, wersja {}.\n.'
        print(txt.format(self.NAME, self.VERSION))


if __name__ == '__main__':
    app = App()
    app.Run()