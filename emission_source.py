class EmissionSource:

    def __init__(self, source_name, consumption_amount, year, month, state, total_co2emissions):

        self.id = self.get_next_id()
        self.source_name = source_name
        self.consumption_amount = consumption_amount
        self.year = year
        self.month = month
        self.state = state
        self.total_co2emissions = total_co2emissions

    def get_next_id(self):
        try:
            with open('id_counter.txt', 'r') as file:
                return int(file.read().strip())
        except FileNotFoundError:
            return 0
        
    def save_next_id(self):
        with open('id_counter.txt', 'w') as file:
            file.write(str(self.id + 1))

    def view_total_co2_emissions(self):
        return self.total_co2emissions
    
    def __str__(self):
        return f"Emission Source ID: {self.id}\n" \
               f"Source Name: {self.source_name}\n" \
               f"Consumption Amount: {self.consumption_amount}\n" \
               f"Year: {self.year}\n" \
               f"Month: {self.month}\n" \
               f"State: {self.state}\n" \
               f"Total CO2 Emissions: {self.total_co2emissions}\n"

    def __del__(self):
        self.save_next_id()
    
    # def get_emission_source(self, emission_source):
    #     emission_source_atributs = EmissionSource().id, EmissionSource().source_name, EmissionSource().consumption_amount, EmissionSource().year, EmissionSource().month, EmissionSource().state, EmissionSource().total_co2emissions
    #     str(emission_source_atributs)

    #     return emission_source_atributs