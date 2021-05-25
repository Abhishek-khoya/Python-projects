rollNumberWiseDataStore=dict()
mobileNumberWiseDataStore=dict()
students=[]
def addStudent():
    try:
        rollNumber=int(input("Enter Roll Number : ")) 
        if rollNumber<=0:raise ValueError
    except:
        print("Invalid Roll Number")
        return
    if rollNumber in rollNumberWiseDataStore:
        print(f"{rollNumber} is already exists to {rollNumberWiseDataStore[rollNumber][1]}")
        return
    name=input("Enter Name : ")
    mobileNumber=input("Enter Mobile Number : ")
    if mobileNumber in mobileNumberWiseDataStore:
        print(f"{mobileNumber} is already exists to {mobileNumberWiseDataStore[mobileNumber][0]}")
        return
    while True:
        save=input("Do you wants to save data (Y/N) : ")
        if save not in "YyNn":
            print("Press (Y/N)")
            continue
        else:break
    if save in "Yy":
        student=(rollNumber,name,mobileNumber)
        rollNumberWiseDataStore[rollNumber]=student
        mobileNumberWiseDataStore[mobileNumber]=student
        students.append(student)
        print("Student Added")
    else:
        print("Student not added")
def getAll():
    if len(students)==0:
        print("Student is not added yet")
    for student in students:
        print(student)
def searchStudent():
    while True:
        search=input("Search by Roll Number or search by Mobile Number (R/M) : ")
        if search not in "RrMm":
            print("Press R/M")
            continue
        else:break
    if search in "Rr":
        try:
            rln=int(input("Enter Roll Number : "))
            if rln<=0:raise ValueError
        except:
            print("Roll Number is Invalid")
            return
        if rln not in rollNumberWiseDataStore:
            print("Invalid Roll Number")
            return
        student=rollNumberWiseDataStore[rln]
        print(f"Roll Number : {student[0]}")
        print(f"Name : {student[1]}")
        print(f"Mobile Number : {student[2]}")
        input("Press enter to continue.............")
    if search in "Mm":
        mn=input("Enter Mobile Number : ")
        if mn not in mobileNumberWiseDataStore:
            print("Invalid Mobile Number")
            return
        student=mobileNumberWiseDataStore[mn]
        print(f"Roll Number : {student[0]}")
        print(f"Name : {student[1]}")
        print(f"Mobile Number : {student[2]}")
        input("Press enter to continue.............")
def editStudent():
    while True:
        search=input("Edit by Roll Number (R) or edit by Mobile Number (M) : ")
        if search not in "RrMm":
            print("Press R/M")
            continue
        else:break
    if search in "Rr":
        try:
            rln=int(input("Enter Roll Number : "))
            if rln<=0:raise ValueError
        except:
            print("Roll Number is Invalid")
            return
        if rln not in rollNumberWiseDataStore:
            print("Invalid Roll Number")
            return
        student=rollNumberWiseDataStore[rln]
    if search in "Mm":
        mn=input("Enter Mobile Number : ")
        if mn not in mobileNumberWiseDataStore:
            print("Invalid Mobile Number")
            return
        student=mobileNumberWiseDataStore[mn]
    print(f"Roll Number : {student[0]}")
    print(f"Name : {student[1]}")
    print(f"Mobile Number : {student[2]}")
    while True:
        edit=input("Do you wants to edit this record (Y/N) : ")
        if edit not in "YyNn":
            print("Press Y/N")    
            continue
        else:break
    if edit in "Nn":
        print("Student not edited : ")
        return
    name=input("Enter new name : ")
    mobileNumber=input("Enter new mobile number : ")
    if student[2]!=mobileNumber:
        if mobileNumber in mobileNumberWiseDataStore:
            print(f"{mobileNumber} is already exists to {mobileNumberWiseDataStore[mobileNumber][0]}")
            return
    while True:
        update=input("Do you wants to update this record : ")
        if update not in "YyNn":
            print("Press (Y/N)")
            continue
        else:break
    if update in "Yy":
        student=(student[0],name,mobileNumber)
        rollNumberWiseDataStore[student[0]]=student
        mobileNumberWiseDataStore[mobileNumber]=student
        i=0
        sz=len(students)
        while i<sz:
            t=students[i]
            if t[0]==student[0]:
                students[i]=student
            i=i+1
        print("Student updated")
    if update in "Nn":        
        print("Student not Updated")        
def deleteStudent():
    if len(students)==0:
        print("Student is not added")
    while True:
        search=input("Delete by Roll Number or Delete by Mobile Number (R/M) : ")
        if search not in "RrMm":
            print("Press R/M")
            continue
        else:break
    if search in "Rr":
        try:
            rln=int(input("Enter Roll Number : "))
            if rln<=0:raise ValueError
        except:
            print("Roll Number is Invalid")
            return
        if rln not in rollNumberWiseDataStore:
            print("Invalid Roll Number")
            return
        student=rollNumberWiseDataStore[rln]
    if search in "Mm":
        mn=input("Enter Mobile Number : ")
        if mn not in mobileNumberWiseDataStore:
            print("Invalid Mobile Number")
            return
        student=mobileNumberWiseDataStore[mn]
    print(f"Roll Number : {student[0]}")
    print(f"Name : {student[1]}")
    print(f"Mobile Number : {student[2]}")
    while True: 
        delete=input("Do you wants to delete this data (Y/N) : ")
        if delete not in "YyNn":
            print("Press (Y/N)")
            continue
        else:break
    if delete in "Nn":
        print("Student not deleted")
        return
    if delete in "Yy":
        rollNumberWiseDataStore.pop(student[0])
        mobileNumberWiseDataStore.pop(student[2])
        i=0
        sz=len(students)
        while i<sz:
            t=students[i]
            if t[0]==student[0]:break
        students.pop(i)
        print("Student Deleted")        
while True:
    print("1. Add")
    print("2. Edit")
    print("3. Delete")
    print("4. Search")
    print("5. GetAll")
    print("6. Exit")
    try:
        choice=int(input("Enter your choice (1-6): "))
        if choice<1 or choice>6:raise ValueError
    except:
        print("Invalid Choice")
    if choice==1:addStudent()
    if choice==2:editStudent()
    if choice==3:deleteStudent()
    if choice==4:searchStudent()
    if choice==5:getAll()
    if choice==6:break
print("Bye,Have a nice day")
        