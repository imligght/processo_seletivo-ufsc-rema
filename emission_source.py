class EmissionSource:

    id = -1

    def __init__(self, source_name, consumption_amount, year, month, state, total_co2emissions):

        EmissionSource.id += 1
        self.id = EmissionSource.id
        self.source_name = source_name
        self.consumption_amount = consumption_amount
        self.year = year
        self.month = month
        self.state = state
        self.total_co2emissions = total_co2emissions

    def view_total_co2_emissions(self):
        return self.total_co2emissions