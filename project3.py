print(" Welcome to Student Data Organizer ")



allstu = []

allsub = set()


def add_student():
    print("\nAdd New Student")
    sid = input("Student ID :- ")
    dob = input("Date of Birth (DD/MM/YYYY) :- ")

    id_dob = (sid, dob)

    name = input("Student Name :- ")
    age = int(input("Age :- "))
    grade = input("Grade :- ")
    subjects = input("Enter Subjects (comma separated) :- ").split(",")


    subjects = [sub.strip() for sub in subjects]


    for sub in subjects:
        allsub.add(sub)


    student_info = {
        "id_dob": id_dob,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }


    allstu.append(student_info)

    print(f"\nStudent {name} added successfully!\n")



def display_students():
    print("\nAll Student Records")
    if not allstu:
        print("No students found.\n")
        return
    for s in allstu:
        sid, dob = s["id_dob"]

        print("ID: %s | Name: %s | Age: %d | Grade: %s" % (sid, s["name"], s["age"], s["grade"]))
        print("DOB: {} | Subjects: {}".format(dob, ", ".join(s["subjects"])))
        print(f"Student {s['name']} record displayed successfully.\n")


def update_student():
    print("\nUpdate Student Information")
    sid = input("Student ID to update :- ")

    for s in allstu:
        if s["id_dob"][0] == sid:
            print("Student found:", s["name"])
            new_age = input("Enter new Age (leave blank to keep same) :- ")
            if new_age:
                s["age"] = int(new_age)
            new_subjects = input("Enter new Subjects (comma separated, leave blank to keep same) :- ")
            if new_subjects:
                subjects = [sub.strip() for sub in new_subjects.split(",")]
                s["subjects"] = subjects
                for sub in subjects:
                    allsub.add(sub)
            print("Student information updated successfully!\n")
            return
    print("Student not found!\n")



def delete_student():
    print("\nDelete Student")
    sid = input("Enter Student ID to delete :- ")

    for i in range(len(allstu)):
        if allstu[i]["id_dob"][0] == sid:
            del allstu[i]
            print("Student deleted successfully!\n")
            return
    print("Student not found!\n")



def display_subjects():
    print("\nAll Unique Subjects Offered")
    if not allsub:
        print("No subjects found.\n")
    else:
        print(", ".join(allsub))
    print()



while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = input("Enter your choice :- ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_subjects()
    elif choice == "6":
        print("\nThank you for using Student Data Organizer. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")