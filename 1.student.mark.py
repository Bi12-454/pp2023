# Initialize empty lists and dictionaries to store data
students = []
courses = []
marks = {}

def input_students():
# Input number of students in a class
    num_students = int(input("Enter number of students in the class: "))
# Input student information: id, name, DoB
    for i in range(num_students):
        student = {}
        student["id"] = input("Enter student ID: ")
        student["name"] = input("Enter student name: ")
        student["dob"] = input("Enter student date of birth (DD/MM/YYYY): ")
        students.append(student)

def input_courses():
# Input number of courses
    num_courses = int(input("Enter number of courses: "))
# Input course information: id, name
    for i in range(num_courses):
        course = {}
        course["id"] = input("Enter course ID: ")
        course["name"] = input("Enter course name: ")
        courses.append(course)

def input_marks():
# Select a course, input marks for student in this course
    print("Select a course:")
    for i, course in enumerate(courses):
        print(i+1, "-", course["name"])
    course_num = int(input("Enter course number: "))
    selected_course = courses[course_num-1]

    for student in students:
        mark = float(input("Enter mark for %s in %s: " % (student["name"], selected_course["name"])))
        if student["id"] in marks:
            marks[student["id"]][selected_course["id"]] = mark
        else:
            marks[student["id"]] = {selected_course["id"]: mark}

def list_courses():
# List courses
    print("Courses:")
    for course in courses:
        print(course["id"],"-",course["name"])

def list_students():
    # List students
    print("Students:")
    for student in students:
        print(student["id"],"-",student["name"])

def show_marks():
# Show student marks for a given course
    print("Select a course to show marks:")
    for i, course in enumerate(courses):
        print(i+1, "-", course["name"])
    course_num = int(input("Enter course number: "))
    selected_course = courses[course_num-1]

    print("Marks for", selected_course["name"], ":")
    for student in students:
        if student["id"] in marks and selected_course["id"] in marks[student["id"]]:
            print(student["name"],"-", marks[student["id"]][selected_course["id"]])
        else:
            print(student["name"], "- No mark") 

# Main program
while True:
    print("Select an option")
    print("1. Input students infor ")
    print("2. Input courses infor")
    print("3. Input marks for a course")
    print("4. List courses")
    print("5. List students")
    print("6. Show student marks for a given choice")
    print("7. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_students()
    elif choice == "2":
        input_courses()
    elif choice == "3":
        input_marks()        
    elif choice == "4":
        list_courses()
    elif choice == "5":
        list_students()
    elif choice == "6":
        show_marks()
    elif choice == "7":
        break
    else:
        print("Invalid choice!")