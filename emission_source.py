class EmissionSource:
    id: int

    def __init__(self, consumption_amount, year, month, state, source_name, total_co2emission=0, id=None):
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
        pass
        


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