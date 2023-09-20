class Patient:
    def __init__(self, name, status):
        self.name, self.status = name, status

    def __str__(self):
        status = ['Normal', 'Urgent', 'Super Urgent'][self.status]
        return f'Patient: {self.name} is {status}'

    def __repr__(self):
        return F'Patient(name="{self.name}", status={self.status})'

    def __lt__(self, other):    # see: def add_patient_smart
        return self.status > other.status   # given 2 patients: which one comes first? one with bigger status
