student_list=[]

print("Welcome to the Student Data Organizer!")
print()
print("Enter student details: ")

while True: 
    print("Select an option: ")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    print()
    if choice==1:
        student_id = int(input("Student_id: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        date_of_birth = input("Date of Birth(YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")

        subjects_set = set()

        for subject in subjects:
            subjects_set.add(subject.strip())

         # tuple for student id and dob(date of birth)
        std_info=(student_id, date_of_birth)

        student = {
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects_set,
            "info": std_info
            
        }

        student_list.append(student)

        
        
        print()

        print("Student added successfully!")
        print()

    elif choice==2:
        print("--- Display All Students ---")
        for student in student_list:
            print(f"Student_id: {student['info'][0]} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | Date of birth: {student['info'][1]} |Subjects: {student['subjects']}")  
        print()


    elif choice==3:
        print("--- Update Student Information ---")
        student_id = int(input("Enter Student ID to update: "))
        for student in student_list:
            if student["info"][0] == student_id:
                
                print("1. Enter new name: ")
                print("2. Enter new age: ")
                print("3. Enter new grade: ")
                print("4. Enter new subejcts: ")
                choice=int(input("Enter your choice: "))
                
                if choice==1:
                    new_name = input("Enter new name: ")
                    student["name"]=new_name
                    print("Student's name updated successfully!")
                    break
                
                
                if choice==2:
                    new_age = int(input("Enter new age: "))
                    student["age"]=new_age
                    print("Student's age updated successfully!")
                    break
                
               
                if choice==3:
                     new_grade = input("Enter new grade: ")
                     student["grade"]=new_grade
                     print("Student's grade updated successfully!")
                     break
                
                     
               
                if choice==4:
                     new_subjects = input("Enter new subjects: ")
                     new_subjects= new_subjects.split(",")
                     student["subjects"]=new_subjects
                     print("Student's subjects updated successfully!")
                     break
                
            
        else:
            print("Student ID isn't found.")      
        print() 
           

    elif choice==4:
        print(" ---Delete Student--- ")
        student_id = int(input("Enter student id to delete student: "))
        for student in student_list:
            if student["info"][0]==student_id:
                student_list.remove(student)
                
                print("Student ID deleted Successfully!")
                break
        else:
            print("Student ID isn't found")
        print()        
                
    elif choice==5:
        print("--- Display Subjects offered ---")
        s = set()
        for std in student_list:
            for subject in std["subjects"]:
                s.add(subject)
        for subject in s:    
                print(subject)
        print()
        
    elif choice==6:
        print("Exiting the program. Goodbye!")
        break

