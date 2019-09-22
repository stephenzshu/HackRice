class Worker:
    def __init__(self, name, equipment_cert, shift, current_facility, current_task):
        self.name = name
        self.equipment_cert = equipment_cert
        self.shift = shift
        self.current_facility = current_facility
        self.current_task = current_task

    def get_name(self):
        return self.name

    def get_equipment_cert(self):
        return self.equipment_cert

    def get_shift(self):
        return self.shift

    def get_current_facility(self):
        return self.current_facility

    def get_current_task(self):
        return self.current_task