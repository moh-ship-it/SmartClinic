class Patient:
    def __init__(self, id, arrival_time, age, case_type, estimated_duration, doctor_id, has_lab_tests, priority_flag):
        self.id = id
        self.arrival_time = arrival_time
        self.age = age
        self.case_type = case_type
        self.estimated_duration = estimated_duration
        self.doctor_id = doctor_id
        self.has_lab_tests = has_lab_tests
        self.priority_flag = priority_flag

    def calculate_priority(self):
        score = 0
        if self.priority_flag:
            score += 100
        if self.case_type == "emergency":
            score += 80
        if self.age >= 60:
            score += 50
        score -= self.estimated_duration
        return score


