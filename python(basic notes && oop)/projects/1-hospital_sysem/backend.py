from patient import Patient

class HospitalManger:
    def __init__(self, specializations_cnt):
        self.specializations = [[] for _ in range(specializations_cnt)]
        self.MAX_QUEUE = 10
        self.NORMAL = 0
        self.URGENT = 1
        self.SUPER_URGENT = 2

    def can_add_more_patients(self, specialization):
        return len(self.specializations[specialization]) < self.MAX_QUEUE

    def add_patient_smart(self, specialization, name, status): 
        spec = self.specializations[specialization]
        spec.append(Patient(name, status))  # Add at end
        spec.sort() # in-place sort based on large status first. it preserves the old order!
        # as python don't know how to compare objects (which comes first), you need to add __lt__

    def add_patient(self, specialization, name, status):
        spec = self.specializations[specialization]
        pat = Patient(name, status)

        if status == 0 or len(spec) == 0:           # Add normal
            spec.append(pat)      # Add at end
        elif status == 1:   # Add urgent
            # Add before the normal patients, but after current urgents / super-urgents
            if spec[-1].status != self.NORMAL:      # if no normals, then it should be added after the end
                spec.append(pat)
            else:   # Find the first normal and add before it
                for idx, patient in enumerate(spec):
                    if patient.status == self.NORMAL:
                        spec.insert(idx, pat)
                        break
        else:
            # Add before the normal or urgent patients, but after current super-urgents
            if spec[-1].status == self.SUPER_URGENT:      # if all are super urgent, just add at the end
                spec.append(pat)
            else:   # Find the first normal/urgent and add before it
                for idx, patient in enumerate(spec):
                    if patient.status == self.NORMAL or patient.status == self.URGENT:
                        spec.insert(idx, pat)
                        break

    def get_printable_patients_info(self):
        results = []    # send back results to front end to print on its way
        for idx, specialization in enumerate(self.specializations):
            if not specialization:
                continue
            cur_patients = []
            for patient in specialization:
                cur_patients.append(str(patient))
            results.append((idx, cur_patients))
        return results

    def get_next_patients(self, specialization):
        if len(self.specializations[specialization]) == 0:
            return None
        return self.specializations[specialization].pop(0)

    def remove_patient(self, specialization, name):
        spec = self.specializations[specialization]
        for idx, patient in enumerate(spec):
            if patient.name == name:
                del spec[idx]
                return True
        return False

