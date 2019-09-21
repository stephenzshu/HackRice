class Equipment:
    def __init__(self, name, probability_fail, hours_to_fix):
        self.name = name
        self.probability_fail = probability_fail
        self.hours_to_fix = hours_to_fix

    def get_name(self):
        return self.name

    def get_probability_to_fail(self):
        return self.probability_fail

    def get_hours_to_fix(self):
        return self.hours_to_fix
