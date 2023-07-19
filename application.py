from emission_source import EmissionSource

class Application:

    def __init__(self):
       pass

    def run(self):
        while True:
            option = input("""Type 1 to register a new emission source
Type 2 to show a source and its emission for a specific id
Type 3 to show all the sources and its emissions
Type 4 to show the emissions factor of the SIN""")

            if option == '1':
                source_name = input("Insert the name of the emission source: ")
                consumption_amount = input("Insert the consumption amount: ")
                year = input("Insert the year: ")
                month = input("Insert the month: ")
                state = input("Insert the state: ")
                total_co2emissions = input("Insert the total ")
                new_emission_source =  EmissionSource(source_name, consumption_amount, year, month, state, total_co2emissions)

            elif option == '2':
                pass

            elif option == '3':
                pass

            elif option == '4':
                pass