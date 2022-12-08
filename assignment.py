import re
#Doctor class-----------------------------------------------------
class Doctor:
    ID = []
    Name = []
    Specialization = []
    Working_Time = []
    Qualification = []
    Room_Number = []
    def readDoctorsFile(self):
        global lines
        with open('files/doctors.txt', 'r', encoding = 'UTF-8') as f:
            lines = f.readlines()
            for i in lines:
                line = re.search('(.+)_(.+)_(.+)_(.+)_(.+)_(.+)', i)
                self.ID.append(line.group(1))
                self.Name.append(line.group(2))
                self.Specialization.append(line.group(3))
                self.Working_Time.append(line.group(4))
                self.Qualification.append(line.group(5))
                self.Room_Number.append(line.group(6))
    def searchDoctorById(self):
        self.readDoctorsFile()
        while True:
            id = input('Enter the doctor Id:\n')  
            if id in self.ID:
                x = self.ID.index(id)
                print("{:<5} {:<12} {:<12} {:<10} {:<15} {:<10}".format(f'{self.ID[0]}',f'{self.Name[0]}',f'{self.Specialization[0]}',f'{self.Working_Time[0]}',f'{self.Qualification[0]}',f'{self.Room_Number[0]}'))
                print("{:<5} {:<12} {:<12} {:<10} {:<15} {:<10}".format(f'\n{self.ID[x]}',f'{self.Name[x]}',f'{self.Specialization[x]}',f'{self.Working_Time[x]}',f'{self.Qualification[x]}',f'{self.Room_Number[x]}\n'))
                print('\nBack to the prevoius Menu\n')
                break
            else:
                print("Can't find the doctor with the same ID on the system\n")
                print("Back to the prevoius Menu\n")
                continue
    def searchDoctorByName(self):
        self.readDoctorsFile()
        while True:
            name = input('Enter the doctor name:\n')  
            if name in self.Name:
                x = self.Name.index(name)
                print("{:<5} {:<12} {:<12} {:<10} {:<15} {:<10}".format(f'{self.ID[0]}',f'{self.Name[0]}',f'{self.Specialization[0]}',f'{self.Working_Time[0]}',f'{self.Qualification[0]}',f'{self.Room_Number[0]}'))
                print("{:<5} {:<12} {:<12} {:<10} {:<15} {:<10}".format(f'\n{self.ID[x]}',f'{self.Name[x]}',f'{self.Specialization[x]}',f'{self.Working_Time[x]}',f'{self.Qualification[x]}',f'{self.Room_Number[x]}\n'))
                print('\nBack to the prevoius Menu\n')
                break
            else:
                print("Can't find the doctor with the same ID on the system\n")
                print("Back to the prevoius Menu\n")
                continue
    def displayDoctorsList(self):
        self.readDoctorsFile()
        for i in range(6):
            print("{:<5} {:<12} {:<12} {:<10} {:<15} {:<10}".format(f'{self.ID[i]}',f'{self.Name[i]}',f'{self.Specialization[i]}',f'{self.Working_Time[i]}',f'{self.Qualification[i]}',f'{self.Room_Number[i]}\n'))
        print('\nBack to the prevoius Menu\n')
    def writeListOfDoctorsToFile(self):
        global msg
        x = input("Enter the doctor's ID:\n")
        y = input("Enter the doctor's name:\n")
        z = input("Enter the doctor's specility:\n")
        m = input("Enter the doctor's timing (e.g., 7am-10pm):\n")
        n = input("Enter the doctor's qualification:\n")
        p = input("Enter the doctor's room number:\n")
        msg = f'\n{x}_{y}_{z}_{m}_{n}_{p}'
    def addDrToFile(self):
        with open('files/doctors.txt', 'a', encoding = 'UTF-8') as f:
            f.write(msg)
            print('Back to the prevoius Menu')
    def editDoctorInfo(self):
        self.readDoctorsFile()
        new_msg = ''
        while True:
            id = input('Please enter the id of the doctor that you want to edit their information:\n')  
            if id in self.ID:
                x = self.ID.index(id)
                y = input("Enter new Name:\n")
                z = input("Enter new Specilist in:\n")
                m = input("Enter new Timing:\n")
                n = input("Enter new Qualification:\n")
                p = input("Enter new Room number:\n")
                n_msg = f'{id}_{y}_{z}_{m}_{n}_{p}\n'
                lines[x] = n_msg
                for i in lines:
                    new_msg += i
                with open('files/doctors.txt', 'w', encoding = 'UTF-8') as f:
                    f.write(new_msg)
                print('Back to the prevoius Menu')
                break
            else:
                print('Please enter a valid ID')
doctor = Doctor()
#Hospital  Facility class----------------------------------------
class Facility:
    # def __init__(self, Ambulance, Admit_Facility, Canteen, Emergency):
    #     self.Ambulance = Ambulance
    #     self.Admit_Facility = Admit_Facility
    #     self.Canteen = Canteen
    #     self.Emergency = Emergency
    def displayFacilities(self):
        with open('files/facilities.txt', 'r', encoding = 'UTF-8') as f:
            lines = f.readlines()
            for i in lines:
                Hospital = re.search('(.+)', i)
                x = Hospital.group()
                print(f'{x}\n')
            print('Back to the Main Menu')
    def addFacility(self):
        name = input('Enter Facility name:\n\n')
        with open('files/facilities.txt', 'a', encoding = 'UTF-8') as f:
            f.write(f'\n{name}')
            print('\nBack to the Main Menu')   
facility = Facility()

    


#common programming-----------------------------------------------
while True:
    select = input('''Welcome to Alberta Hospital (AH) Managment system
Select from the following options, or select 0 to stop:
1 - 	Doctors
2 - 	Facilities
3 - 	Laboratories
4 - 	Patients\n''')
    match select:
        case '1':
            while True:
                D_menu = input('''Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu\n''')
                match D_menu:
                    case '1':
                        doctor.displayDoctorsList()
                        continue
                    case '2':
                        doctor.searchDoctorById()
                        continue
                    case '3':
                        doctor.searchDoctorByName()
                        continue
                    case '4':
                        doctor.writeListOfDoctorsToFile()
                        doctor.addDrToFile()
                        continue
                    case '5':
                        doctor.editDoctorInfo()
                        continue
                    case '6':
                        break                 
        case '2':
            while True:
                F_menu = input('''Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu
''')
                match F_menu:
                    case '1':
                        facility.displayFacilities()
                        continue
                    case '2':
                        facility.addFacility()
                    case '3':
                        break
        case '0':
            break                     