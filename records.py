import os

from emission_source import EmissionSource

class Records:
    def __init__(self, records_file_name='emission_sources.dat'):
        # list of emission sources
        self.emission_sources = []

        # gets the path to the current file
        current_path = os.path.dirname(__file__)
        self.sources_file_path = os.path.join(current_path, records_file_name)
        print(self.sources_file_path)
        # checks if records file does not already exist to use the default file name or not
        if not os.path.isfile(self.sources_file_path):
            with open(self.sources_file_path, 'w') as sources_file:
                sources_file.write('id,source_name,consumption_amount,year,month,state,total_co2emission\n')

            last_source_id = -1

        else:
            with open(self.sources_file_path, 'r') as sources_file:
                # ignores the file header information
                for line in sources_file.readlines()[1:]:
                    record_id, source_name, consumption_amount, year, month, state, total_co2emission = line.split(',')
                    consumption_amount = float(consumption_amount)
                    year = int(year)
                    month = int(month)
                    total_co2emission = float(total_co2emission)
                    record_id = int(record_id)

                    source = EmissionSource(source_name, consumption_amount, year, month, state, total_co2emission, record_id)
                    self.add_emission_source(source)

            if len(self.emission_sources) > 0:
                # max returns an EmissionSource object, so we access its id after the function call
                last_source_id = max(self.emission_sources, key=lambda x: x.id).id

            else:
                last_source_id = -1    

        self.last_source_index_when_first_loaded = len(self.emission_sources)
        print(self.last_source_index_when_first_loaded)
        EmissionSource.id = last_source_id

    def add_emission_source(self, new_source):
        self.emission_sources.append(new_source)

    def get_emission_source_by_id(self, source_id):
        for source in self.emission_sources:
            if source_id == source.id:
                return source

    def get_all_emission_sources(self):
        return self.emission_sources

    def __del__(self):
        with open(self.sources_file_path, 'a') as sources_file:
            for source in self.emission_sources[self.last_source_index_when_first_loaded:]:
                output_line = f'{source.id},{source.name},{source.consumption_amount},{source.year},{source.month},{source.state},{source.total_co2emission}\n'
                sources_file.write(output_line)