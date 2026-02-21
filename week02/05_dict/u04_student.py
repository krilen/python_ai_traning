# Worked and played to long on this one. If I needed to use this I would had done it using OOP.


# Data to have something to work with
students = {
 'josmA2000': {'firstname': 'John', 'lastname': 'Smith', 'birthyear': 2000, 'key': 'A', 'grades': ''},
 'anobD1999': {'firstname': 'Anna', 'lastname': 'Öberg', 'birthyear': 1999, 'key': 'D', 'grades': ''},
 'librE2005': {'firstname': 'Liam', 'lastname': 'Brown', 'birthyear': 2005, 'key': 'E', 'grades': ''},
 'emasI2003': {'firstname': 'Emma', 'lastname': 'Åström', 'birthyear': 2003, 'key': 'I', 'grades': ''},
 'noleL2008': {'firstname': 'Noah', 'lastname': 'Lee', 'birthyear': 2008, 'key': 'L', 'grades': ''},
 'olmuO2007': {'firstname': 'Olivia', 'lastname': 'Müller', 'birthyear': 2007, 'key': 'O', 'grades': ''},
 'axzhP2004': {'firstname': 'Axel', 'lastname': 'Zhang', 'birthyear': 2004, 'key': 'P', 'grades': ''},
 'idniA2002': {'firstname': 'Ida', 'lastname': 'Nilsson', 'birthyear': 2002, 'key': 'A', 'grades': ''},
 'erbeD2001': {'firstname': 'Erik', 'lastname': 'Berg', 'birthyear': 2001, 'key': 'D', 'grades': ''},
 'saliE2006': {'firstname': 'Sara', 'lastname': 'Lind', 'birthyear': 2006, 'key': 'E', 'grades': ''}
}

VALID_LETTERS = "abcdefghijklmnopqrstuvwxyz"
TRANSFORM_LETTERS = {"ö": "o", "å": "a", "ä": "a", "ü": "u"}


def main():
    while True:
        selection = menu()
        print()
        
        match selection:
            case "q":
                print("Please come again")
                print()
                
                break
        
            case "a":
                while True:
                    add_student()
                    print()
                    
                    add_another_student = input("Do you want to add another student (y/n) >> ").casefold()
                    
                    if add_another_student == "y":
                        continue
                    
                    else:
                        break
            
            case "l":
                list_students()
                
            case "g":
                student_grades()
                
            case _:
                continue
            
    return


def student_name_short(name):
    short = ""
    
    for letter in name:
        if letter in VALID_LETTERS:
            short += letter
            
        elif letter in list(TRANSFORM_LETTERS.keys()):
            short += TRANSFORM_LETTERS[letter]
            
        if len(short) == 2:
            break
            
    if len(short) < 2:
        return short +"x" 
    
    return short


def menu():
    
    while True:
        print()
        print("================= Student at Python AI high =================")
        print()
        print("Chose what you want to do!")
        print(" 'a' - Add a student")
        print(" 'l' - See all students")
        print(" 'g' - Student grades")
        print()
        print(" 'q' - To quit!")
        print()
        
        selection = input("Your selection >> ")
        
        if selection in ["a", "l", "q", "g"]:
            break
        
        else:
            print("Not a valid selection!")
            
    return selection


def add_student():
    student_firstname = student_lastname = student_birthyear = student_key = None
    
    while True:
        student = {"firstname": "", "lastname": "", "birthyear": 0, "key": "", "grades": ""}
        
        if not student_firstname:
            student_firstname = input("The students firstname >> ").title()
            
            if student_firstname == "":
                print("Please provide a firstname for the student, try again!")
                continue
            
        if not student_lastname:
            student_lastname = input("The students lastname >> ").title()
            
            if student_lastname == "":
                print("Please provide a lastname for the student, try again!")
                continue
            
        if not student_birthyear:
            try:
                student_birthyear = int(input("The students birthyear, between 1950 and 2014 >> "))
                
                # Reused the exception that already existed
                if student_birthyear < 1950 or student_birthyear > 2014:
                    raise ValueError
            
            except ValueError:
                print("That is not a valid birthyear for a student, try again!")
                student_birthyear = None
                continue

        if not student_key:
            student_key = input("The students key (A, D, E, I, L, O and P are valid) >> ").upper()
        
        if student_key not in ["A", "D", "E", "I", "L", "O", "P"] or len(student_key) != 1:
            print("That is not a valid student key, try again!")
            student_key = None
            continue
        
        student_id = (student_name_short(student_firstname.lower()) 
                    +student_name_short(student_lastname.lower())
                    +student_key
                    +str(student_birthyear))

        student["firstname"] = student_firstname
        student["lastname"] = student_lastname
        student["birthyear"] = student_birthyear
        student["key"] = student_key
        
        if bool(students.get(student_id, False)):
            
            for i in range(1,10):
                
                new_student_id = student_id[:3] + str(i) + student_id[4:]
                
                if not bool(students.get(new_student_id, False)):
                    student_id = new_student_id
                    break
            
            else:
                print("Not possible to create a student ID and add student.")
                student_id = None

        if student_id:
            
            print()
            print("Student to be added")
            print(f" - Student ID: {student_id}")
            print(f" - First name: {student["firstname"]}")
            print(f" - Last name: {student["lastname"]}")
            print(f" - Key: {student["key"]}")
            print(f" - Birth year: {student["birthyear"]}")
            print()
            
            student_save_input = input("Do you want to add this student ('y' to add) >> ")
            
            if student_save_input.casefold() == "y":
                students[student_id] = student
            
                print(f"A student with the student ID: '{student_id}' was saved.")
        
        break

    return


def list_student(student_id):
    
    print(student_id)

    student = students.get(student_id, False)
        
    if bool(student):
        print(f"Student: {student_id}")
        print(f" - First name: {student["firstname"]}")
        print(f" - Last name: {student["lastname"]}")
        print(f" - Key: {student["key"]}")
        print(f" - Birth year: {student["birthyear"]}")
        print(f" - Grades: {"-" if student["grades"] == "" else student["grades"]}")

        return True

    else:
        return False


def list_students():
    
    for student_id in students:
        
        print()
        _ = list_student(student_id)


def student_grades():
    
    print()
    print("Students")
    
    for student_id in students:
        print(f" - Student ID: {student_id}, {students[student_id]['firstname']} {students[student_id]['lastname']} (Grades: {'-' if students[student_id]['grades'] == '' else students[student_id]['grades']}).")
        
    print()
    
    while True:
        student_input = input("Enter the 'Student ID' to modify its grades ('q' to quit) >> ")
        
        if student_input.casefold() == "q":
            break
        
        else:
            
            try:
                student = students[student_input]
        
            except KeyError:
                print("Student not found, try again!")
                continue
            
            else:
                student_input_grades = input("Enter the string of grades ('F', 'E', 'C', 'B' and 'A') for the student ()'q' to quit) >> ")
                
                if student_input_grades.casefold() == "q":
                    break
        
                else:
                    students[student_input]["grades"] = ", ".join([g.upper() for g in student_input_grades if g.upper() in ['F', 'E', 'C', 'B', 'A']])
            
    return
    
if __name__ == "__main__":
    
    main()
    
    
    