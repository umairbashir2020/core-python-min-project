"""
Dictionary
collection  = key + pair = pair =data 
{key1:value1 , key2:value2}

"""
# initialize dictionary
student_grade ={}

# add new student
def add_student(name,grade):
    student_grade[name] = grade
    #[john] = 100
    print(f"student {name} added with a {grade} ")
    # Added john with a 100

# update s student
def update_student(name,grade):
    if name in student_grade:
        student_grade[name] = grade
        #john = 200
        print(f"{name} with marks are updated {grade}")
    else:
        print("{name} not found...")

# delete a student
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name}  has been deleted")
    else:
        print(f"{name} not found!")

# view all students
def view_student():
    if student_grade:
        for name ,grade in student_grade.items():
            print(f"{name} : { grade}")
    else:
        print("No Record found!")


def main():
    while True:
        print('\n Student Grades Management System')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice =int(input("Enter your Choice = "))

        if choice == 1:
            name = input('Enter student name = ')
            grade = int(input('Enter student grade = '))
            add_student(name,grade)

        elif choice == 2:
            name = input("Enter student name you want to update = ")
            grade =int(input("Enter student grade = "))
            update_student(name,grade)
        
        elif choice == 3:
            name = input("Enter student name you want to delete = ")
            delete_student(name)

        elif choice == 4:
            view_student()

        elif choice == 5:
            print("Exit the program... ")
            break

        else:
            print("Invalid choice")

main()
    



