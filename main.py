import json
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    students = {}

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
def calculate_grade(avg):
    if avg>=60:
        return "A+"
    elif avg>=50:
        return "A"
    elif avg>=40:
        return "B"
    elif avg>=30:
        return "C"
    elif avg>=25:
        return "D"
    else:
        return "F"
def add_student():
    name=input("Enter Student name:")
    if name in students:
        print("Student already exists!")
        return
    try:
        math=float(input("Enter Marks obtained in Maths:"))
        os=float(input("Enter Marks obtained in Operating System:"))
        coa=float(input("Enter Marks obtained in Computer Org. and Arch.:"))
        hum=float(input("Enter Marks obtained in Universal Human Values:"))
        daa=float(input("Enter Marks obtained in Design and Analysis of Algorithms:"))
        students[name]={
            "Discrete Mathematics":math,
            "Operating System":os,
            "Computer Organization and Architecture":coa,
            "Universal Human Values":hum,
            "Design and Analysis of Algorithms":daa
        }
        save_data()
        print("Record Saved Successfully!")
    except ValueError:
        print("Please enter a valid numeric marks!")
def view_report():
    name=input("Enter Student Name:")
    if name not in students:
        print("Student record not found!")
        return
    marks=students[name]
    total=sum(marks.values())
    average=total/len(marks)
    highest=max(marks.values())
    lowest=min(marks.values())
    grade=calculate_grade(average)
    print("\n======REPORT CARD======")
    print("Name:",name)

    for subject,mark in marks.items():
        print(f"{subject}:{mark}")
    print("--------------------------")
    print("Total  :",total)
    print("Average:",round(average,2))
    print("Highest:",highest)
    print("Lowest :",lowest)
    print("Grade  :",grade)
    print("===========================\n")

def update_marks():
    name=input("Enter Student Name:")
    if name not in students:
        print("Student record not found.")
        return
    try:
        students[name]["Discrete Mathematics"]=float(input("New DM Marks:"))
        students[name]["Operating System"]=float(input("New OS Marks:"))
        students[name]["Computer Organization and Architecture"]=float(input("New COA Marks:"))
        students[name]["Universal Human Values"]=float(input("New UHV Marks:"))
        students[name]["Design and Analysis of Algorithms"]=float(input("New DAA Marks:"))
        save_data()
        print("Record updated Successfully!")
    except ValueError:
        print("Please enter valid numeric marks.")
def view_all_students():
    if not students:
        print("No student records found!")
        return

    print("\n===== STUDENT LIST =====")
    for name in students:
        print(name)
    print(f"\nTotal Students: {len(students)}")
def delete_record():
    name=input("Enter Student Name:")
    if name in students:
        del students[name]
        save_data()
        print("Record Deleted Successfully!")
    else:
        print("Student record not found!")

while True:
    print("\n=====STUDENT REPORT CARD SYSTEM=====")
    print("1.Add Student Record")
    print("2.View Report Card")
    print("3.Update Marks")
    print("4.Delete Record")
    print("5.View All Students")
    print("6.Exit")

    try:
        choice=int(input("Enter Your Choice:"))

        if choice==1:
            add_student()
        elif choice==2:
            view_report()
        elif choice==3:
            update_marks()
        elif choice==4:
            delete_record()
        elif choice == 5:
            view_all_students()
        elif choice==6:
            print("Thank You for using the System!")
            break
        else:
            print("Invalid Choice. Try Again.")
    except ValueError:
        print("Please enter a valid number.")