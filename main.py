from Patient import Patient
from Scheduler import Scheduler

if __name__ == "__main__":
    num = int(input('enter the numbers of paint \n'))
    patients = []
    for i in range(num):
        print(f'paitent:{i+1}')
        m = int(input('ente id \t'))
        n = int(input('enter the Arrive time'))
        patients.append(Patient(m, n,30, "emergency", 20, "Dr. Ahmed", False, True))
    # for nn in Patient:
    #     nn.
    # patients = [
    #     Patient(m, n, 65, "emergency", 20, "Dr. Ahmed", False, True),
    #     # Patient(102, 9, 30, "consultation", 15, "Dr. Leila", False, False),
    #     # Patient(103, 10, 70, "follow-up", 10, "Dr. Ahmed", True, False),
    #     # Patient(104, 9, 45, "emergency", 25, "Dr. Leila", False, True),
    # ]

    scheduler = Scheduler()
    scheduler.add_patients(patients)
    scheduler.generate_schedule()
    scheduler.display_schedule()






#   patientsNumbers = int(input('enter the patint'))
#     patt=[]
#     for pt in range (patientsNumbers):
#         id = int(input('enter id'))
#         avv = int(input('avvri time'))
#         age = int(input('age'))
#         cas = str(input('cas'))
#         es = int(input('es'))
#         dn = str(input('es'))
#         hal = bool(input('hal'))
#         pri = bool(input('pri'))
#     patt.append(Patient(id, avv, age, cas, es, dn, hal, pri))