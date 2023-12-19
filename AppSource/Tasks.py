import datetime

class Tasks():
    def __init__(self) -> None:
        pass

    def depart_from_depot(): pass
    def back_to_depot(): pass
    def tech_callout(): pass

class RouteWorker():
    def __init__(self,vehicle, route, brigade):
        self.vehicle = vehicle
        self.route = route
        self.brigade = brigade
        self.brigade = str(self.brigade) + '_' +str(self.route[0])

    def create_day_schedule(self,starttime_h,starttime_m,cycles):
        self.timestart_on_depot = datetime.datetime.combine(datetime.date.today(),datetime.time(hour=starttime_h,minute=starttime_m))
        self.timestart_on_line = self.timestart_on_depot + datetime.timedelta(minutes=20)
        self.route_time = datetime.datetime.combine(datetime.date.today(),self.route[3])
        self.timeend = self.timestart_on_line + datetime.timedelta(minutes=(self.route_time.minute*cycles+10),hours=(self.route_time.hour*cycles))


    def __del__(self): None
