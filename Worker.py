class Worker:
    def __init__(self, name, equipment_cert, shifts):
        self.name = name
        self.equipment_cert = equipment_cert
        self.shifts = shifts
        #self.current_task = current_task

    def get_name(self):
        return self.name

    def get_equipment_cert(self):
        return self.equipment_cert

    def get_shifts(self):
        return self.shifts

    #def get_current_task(self):
    #    return self.current_task
