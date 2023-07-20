from emission_source import EmissionSource
import application as app

class Records:
    def __init__(self):
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)
        return self.records

    def get_record_by_id(self):
        return {record.id: record for record in self.records}
            
    def get_all_records(self):
        return self.records