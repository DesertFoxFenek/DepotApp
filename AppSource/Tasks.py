class Tasks():
    def __init__(self) -> None:
        pass

    def depart_from_depot(): pass
    def back_to_depot(): pass
    def tech_callout(): pass

class RouteWorker():
    def __init__(self,vehicle, route):
        self.vehicle = vehicle
        self.route = route

    def create_day_schedule(self,starttime,cycles):
        self.timestart = starttime
        self.timeend = self.route[3] * 10 * cycles

    def __del__(self): None
