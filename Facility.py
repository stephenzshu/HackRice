class Facility:
    def __init__(self, name, lat, lon, equipment_list):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.equipment_list = equipment_list

    def get_name(self):
        return self.name

    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

    def get_equipment_list(self):
        return self.equipment_list
