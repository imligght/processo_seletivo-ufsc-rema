from emission_source import EmissionSource
from records import Records
class Application:

    def __init__(self):
        self.records = Records()

    def run(self):
        while True:
            option = int(input("""Type 1 to register a new emission source
Type 2 to show a source and its emission for a specific id
Type 3 to show all the sources and its emissions
Type 4 to show the emissions factor of the SIN\n"""))

            if option == 1:
                try:
                    source_name = input("Insert the name of the emission source: ")
                    consumption_amount = float(input("Insert the consumption amount: "))
                    year = int(input("Insert the year (yyyy): "))
                    month = int(input("Insert the month (mm): "))
                    state = input("Insert the state: ")
                    total_co2emissions = float(input("Insert the total of CO2 emission: "))
                    new_emission_source =  EmissionSource(source_name, consumption_amount, year, month, state, total_co2emissions)
                    self.records.add_emission_source(new_emission_source)

                    print(f"Register sucessful. The emission source ID {new_emission_source.id}")

                except Exception as e:
                    print('An error ocurred in the registration process: ', str(e))

                print(self.records.emission_sources)

            elif option == 2:

                emission_id = int(input("Insert the ID of the emission you want to see: "))

                if (emission_source := self.records.get_emission_source_by_id(emission_id)):
                    print(emission_source)

                else:
                    print(f"Emission ID {emission_id} not found.")

            elif option == 3:
                emission_sources = self.records.get_all_emission_sources()
                if len(emission_sources) > 0:
                    for emission_source in emission_sources:
                        print(emission_source)
                else:
                    print("No emissions records found.")

            elif option == 4:
                pass

            elif option == 5:
                return