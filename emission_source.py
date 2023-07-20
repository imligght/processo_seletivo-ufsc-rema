class EmissionSource:

    def __init__(self, source_name, consumption_amount, year, month, state, total_co2emissions, id=None):
        if id == None:
            EmissionSource.id += 1
            self.id = EmissionSource.id

        else:
            self.id = id

        self.source_name = source_name
        self.consumption_amount = consumption_amount
        self.year = year
        self.month = month
        self.state = state
        self.total_co2emissions = total_co2emissions

    def view_total_co2_emissions(self):
        return self.total_co2emissions
    
    def __str__(self):
        return f"{self.id}\n" \
               f"{self.source_name}\n" \
               f"{self.consumption_amount}\n" \
               f"{self.year}\n" \
               f"{self.month}\n" \
               f"{self.state}\n" \
               f"{self.total_co2emissions}\n"

    # def __del__(self):
    #     self.save_next_id()
    
    # def get_emission_source(self, emission_source):
    #     emission_source_atributs = EmissionSource().id, EmissionSource().source_name, EmissionSource().consumption_amount, EmissionSource().year, EmissionSource().month, EmissionSource().state, EmissionSource().total_co2emissions
    #     str(emission_source_atributs)

    #     return emission_source_atributs