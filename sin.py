from emission_source import EmissionSource

class Sin:

    def __init__(self, north_region_states):
        self.north_region_states = ['Amazonas', 'AM', 'Pará', 'PA', 'Acre', 'AC', 'Roraima', 'RR', 'Rondônia', 'RO', 'Amapá', 'AP', 'Tocantins', 'TO']

    def sin_calc(self, emission_source):
        self.emission_source = emission_source

        if emission_source.year == 2011:
            emission_factor = (emission_source.consumption_amount / 1000) * 0,4148

        elif emission_source.year == 2012:
            emission_factor = (emission_source.consumption_amount / 1000) * 0,7125

        elif emission_source.year == 2013:
            emission_factor = (emission_source.consumption_amount / 1000) * 0,8726

        elif emission_source.year == 2014:
            emission_factor = (emission_source.consumption_amount / 1000) * 0,8151

        elif emission_source.year == 2015:
            emission_factor = (emission_source.consumption_amount / 1000) * 0,8438

        return emission_factor