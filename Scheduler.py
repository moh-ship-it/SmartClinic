class Scheduler:
                #   start_time is initional time
    def __init__(self, start_time=9):
        self.start_time = start_time
        self.schedule = []

    def add_patients(self, patients):
        self.patients = [p for p in patients if not p.has_lab_tests]
        self.patients.sort(key=lambda p: p.calculate_priority(), reverse=True)

    def generate_schedule(self):
        current_time = self.start_time
        for p in self.patients:
            start = max(current_time, p.arrival_time)
            end = start + p.estimated_duration
            self.schedule.append({
                "patient_id": p.id,
                "doctor": p.doctor_id,
                "start": start,
                "end": end
            })
            current_time = end

    def display_schedule(self):
        print("📅 Appointment Schedule:")
        for entry in self.schedule:
            print(f"Patient {entry['patient_id']} with {entry['doctor']} from {entry['start']}:00 to {entry['end']}:00")

