student_list=[]

print("Welcome to the Student Data Organizer!")
print()
print("Enter Student details: ")

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
        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth(YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")

        subjects_set = [s.strip() for s in subjects.split(",")]
        subjects_list=list(subjects_set)

        # tuple for student id and dob(date of birth)
        student_information = (student_id, dob)
        student = {
            "Student ID": student_id,
            "Name": name,
            "Age": age,
            "Grade": grade,
            "Date of Birth": dob,
            "Subjects": subjects_set
        }
        
        student_list.append(student)
        
        print()

        print("Student added successfully!")
        print()

        
    elif choice==2:
        print("--- Display All Students ---")
        for student in student_list:
            print(f"Student ID: {student['Student ID']} | Name: {student['Name']} | Age: {student['Age']} | Grade: {student['Grade']} | Subjects: {', '.join(student['Subjects'])}")
        print()

    elif choice==3:
        print("--- Update Student Information ---")
        student_id = int(input("Enter Student ID to update: "))
        for student in student_list:
            if student["Student ID"] == student_id:
                new_age= input("Enter new Age: ")
                student.update({"Age": new_age})
                new_grade= input("Enter new Grade: ")
                student.update({"Grade": new_grade})
                new_subjects = input("Enter new Subjects (comma - separated): ")
                student.update({"Subjects": [s.strip() for s in new_subjects.split(",")]})
                
                print()
                print("Student information updated successfully!")
                print()
                break
        else:
            print("Student ID isn't found.")      
            print() 

    elif choice==4:
        print("--- Delete Student ---")       
        student_id = int(input("Enter Student ID to delete: "))
        for student in student_list:
            if student["Student ID"] == student_id:
                student_list.remove(student)
                print()
                print("Student deleted successfully!")
                print()
                break
        else:
            print("Student ID isn't found.")  
            print()

    elif choice==5:
            print("--- Display Subjects Offered ---")
            subjects_offered = set()
            for student in student_list:
                subjects_offered.update(student["Subjects"])
            print("Subjects Offered: " , ", ".join(subjects_offered))
            print()


    elif choice==6:
        print("Exiting the program. Goodbye!")
        break