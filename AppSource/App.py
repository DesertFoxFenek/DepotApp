import InterfaceConnector

class App:
    def __init__(self) -> None:
        pass
    def Run(self):
        while(True):
            ThisInterface = InterfaceConnector.Interface()
            ThisInterface.show_depot_init_menu()
            input()
            ThisInterface.show_operating_lines()
            input()

Main = App()
Main.Run()

print(Main)