students = {}
VALID_LETTERS = "abcdefghijklmnopqrstuvwxyz"
TRANSFORM_LETTERS = {"ö": "o", "å": "a", "ä": "a", "ü": "u"}

# TMP data so I have something to work with
{
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



def main():
    
    while True:
        
        selection = menu()
        
        if selection == "q":
            print("Please come again")
            break
        
        elif selection == "a":
            
            while True:
                
                print()
                add_student()
                
                print()
                add_another_student = input("Do you want to add another student (y/n) >> ").casefold()
                
                if add_another_student == "y":
                    continue
                
                else:
                    break
            
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
        print(" 'l' - See students ")
        print(" 'q' - To quit!")
        print()
        
        selection = input("Your selection >> ")
        
        if selection in ["a", "l", "q"]:
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
                print("Please provide a firstname for the student!")
                continue
            
        if not student_lastname:
            student_lastname = input("The students lastname >> ")
            
            if student_lastname == "":
                print("Please provide a lastname for the student!")
                continue
            
        if not student_birthyear:
            try:
                student_birthyear = int(input("The students birthyear, between 1950 and 2014 >> "))
                
                if student_birthyear < 1950 or student_birthyear > 2013:
                    raise ValueError
            
            except ValueError:
                print("That is not a valid birthyear for a student, try again!")
                student_birthyear = None
                continue

        if not student_key:
            student_key = input("The students key (A, D, E, I, L, O and P are valid) >> ").upper()
        
        if student_key not in ["A", "D", "E", "I", "L", "O", "P"] and len(student_key) == 1:
            print("That is not a valid student key, try again!")
            student_key = None
            continue
                
        
        student_id = (student_name_short(student_firstname.lower()) 
                    +student_name_short(student_lastname[:2].lower())
                    +student_key
                    +str(student_birthyear))
        
        student["firstname"] = student_firstname
        student["lastname"] = student_lastname
        student["birthyear"] = student_birthyear
        student["key"] = student_key
        
        students[student_id] = student
        
        student_firstname = student_lastname = student_birthyear = student_key = None

        break
    


if __name__ == "__main__":
    
    main()
    
    
    