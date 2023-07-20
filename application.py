from emission_source import EmissionSource
from records import Records
class Application:

    def __init__(self):
       pass

    def run(self):
        while True:
            option = input("""Type '1' to register a new emission source
Type '2' to show a source and its emission for a specific id
Type '3' to show all the sources and its emissions
Type '4' to show the emissions factor of the SIN\n""")

            if option == '1':
                source_name = input("Insert the name of the emission source: ")
                consumption_amount = input("Insert the consumption amount: ")
                year = input("Insert the year: ")
                month = input("Insert the month: ")
                state = input("Insert the state: ")
                total_co2emissions = input("Insert the total of CO2 emission: ")
                new_emission_source =  EmissionSource(source_name, consumption_amount, year, month, state, total_co2emissions)

                try:
                    records_file = input("Enter the path to the file or leave it empty to create a file automatically in the current directory: ")

                    if not records_file.strip():  # check if the user provided a file path or left it empty
                        # if the file path is not provided, use a default file name
                        default_file_name = "records_file.dat"
                        records_file = default_file_name

                    with open(records_file, 'a') as file:
                        file.write(str(new_emission_source))
                        Records().add_record(new_emission_source.id)

                        print(f"Successful registration. Record ID is {new_emission_source.id}.")

                    EmissionSource().save_next_id()
                except Exception as e:
                    print("An error ocurred in the registration process: ", str(e))

            elif option == '2':

                all_records = Records().get_all_records()

                emission_id = input("Insert the ID of the emission you want to see: ")

                if emission_id in all_records:
                    print(all_records[emission_id])

                else:
                    print(f"Emission ID {emission_id} not found.")


            elif option == '3':
                all_records =  Records().get_all_records()

                if all_records:
                    for record_id, record in all_records.items():
                        print(f"Record ID: {record_id}")
                        print(record)
                        print()
                else:
                    print("No emissions records found.")


            elif option == '4':
                pass