class EmissionSource:
    id: int

    def __init__(self, source_name, consumption_amount, year, month, state, total_co2emission, id=None):
        if id == None:
            EmissionSource.id += 1
            self.id = EmissionSource.id

        else:
            self.id = id

        self.name = source_name
        self.consumption_amount = consumption_amount
        self.year = year
        self.month = month
        self.state = state
        self.total_co2emission = total_co2emission

    def total_co2emission_calculation(self):
        


    def view_total_co2_emissions(self):
        return self.total_co2emission
    
    def __str__(self):
        return f"Emission Source ID: {self.id}\n" \
               f"Source Name: {self.name}\n" \
               f"Consumption Amount: {self.consumption_amount}\n" \
               f"Year: {self.year}\n" \
               f"Month: {self.month}\n" \
               f"State: {self.state}\n" \
               f"Total CO2 Emissions: {self.total_co2emission}\n"

    # def get_emission_source(self, emission_source):
    #     emission_source_atributs = EmissionSource().id, EmissionSource().source_name, EmissionSource().consumption_amount, EmissionSource().year, EmissionSource().month, EmissionSource().state, EmissionSource().total_co2emission
    #     str(emission_source_atributs)

    #     return emission_source_atributs