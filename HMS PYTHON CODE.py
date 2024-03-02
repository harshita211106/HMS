# python connect
import mysql.connector
obj=mysql.connector.connect(host="localhost", user="root",passwd="sqlpassword)
mycursor=obj.cursor()


# create databases
mycursor.execute("create database if not exists covid")
mycursor.execute("use covid")
# create table for patient
mycursor.execute("create table if not exists patient(patientid int auto_increment primary key,pname varchar(30) not null,page int(3) not null,pgender varchar(6) not null,phoneno bigint(10) not null,admitdate date,patient_problem varchar(30) not null)")
# create table for staff
mycursor.execute("create table if not exists staff(staffid int auto_increment primary key, staffname varchar(30)not null, staffage int not null,staffgender varchar(6) not null, staffphoneno bigint not null, dateofjoining date,salary int)")
# create table for change the password of admin section
mycursor.execute("create table if not exists password(password varchar(30) not null)")
# create table for patientrecord
mycursor.execute("create table if not exists patientrecord(patientid int not null,pname varchar(30) not null, page int(3) not null,pgender varchar(6) not null, phoneno bigint(10) not null, admitdate date, dischargedate date)")
# create table for staffrecord
mycursor.execute("create table if not exists staffrecord(staffid int not null,staffname varchar(30)not null,staffage int not null,staffgender varchar(6) not null,staffphoneno bigint not null,joiningdate date,salary int,total_working_day date)")
# create table for doctor
mycursor.execute("create table if not exists doctor(doctorid int auto_increment primary key,doctorname varchar(40) not null,department varchar(40) not null,gender varchar(6) not null, work_experience int(5) not null,phone_number bigint(10) not null,dateofjoinig date, salary int(10) not null)")
# create table for department wise salary
mycursor.execute("create table if not exists salary(department varchar(40)not null, salary int(7) not null)")
# create table for doctor job
mycursor.execute("create table if not exists job(apply_id int auto_increment primary key,apply_job_date date,dname varchar(40), department varchar(10),work_experience int(5),gender varchar(6),phone_number bigint(10) not null, status varchar(10))")
# create table for doctor record
mycursor.execute("create table if not exists doctorrecord(doctorid int,doctorname varchar(40) not null,department varchar(40) not null,gender varchar(6) not null,phone_number bigint(10) not null,dateofjoinig date,date_of_relived date)")

# create table for symptoms and department
mycursor.execute("create table if not exists symptoms_and_dept(symptoms varchar(50), department varchar(40))")
# create table for login
mycursor.execute("create table if not exists login(name varchar(30) not null,mobile_number bigint(10) unique, password varchar(20) unique)")
# create table for appointment
mycursor.execute("create table if not exists appointment(patient_name varchar(30) not null,age int(2)not null,gender varchar(6)not null,mobile_number bigint(10)not null, doctorid int(12) not null, department varchar(40))")
# create table for treatment price
mycursor.execute("create table if not exists treatment_price(symptoms varchar(20) not null,price float(10) not null)")
obj.commit()







# for introduction
def front_page():
    
    print("|_____________________________________________________________________________________________|")
    print("-------------------------------------------WELCOME TO------------------------------------------")
    print("|_____________________________________________________________________________________________|")
    print("--------------------------------**-HOSPITAL MANAGEMENT SYSTEM--**------------------------------")
    print("|_____________________________________________________________________________________________|")
    print("--------------------------------*--GUIDED BY: MRS. ANJU VERMA--*-------------------------------")
    print("|_____________________________________________________________________________________________|")
    print("--------------------------------*--SUBMITTED BY: HARSHITA BHINGARE--*--------------------------")
    print("|_____________________________________________________________________________________________|")
    print("\n\n\n")



    
   




# for admin
##showing menu


def admin():
    print("")
    print("Showing menu for admin:\n")
    n="n"
    while n=="n":
        print("")
        print("*"*15,"WELCOME TO ADMIN SECTION","*"*15)
        print("press 1 to ADD PATIENTS:\n")
        print("press 2 to ADD STAFF:\n")
        print("press 3 to DISPLAY PATIENTS RECORD:\n")
        print("press 4 to DISPLAY STAFF RECORD:\n")
        print("press 5 to CHANGE PASSWORD:\n")
        print("press 6 for REMOVE PATIENTS:\n")
        print("press 7 to REMOVE STAFF:\n")
        print("press 8 to UPDATE PATIENT:\n")
        print("press 9 to UPDATE STAFF:\n")
        print("press 10 to ADD DOCTOR:\n")
        print("press 11 to REMOVE DOCTOR:\n")
        print("press 12 for Approval required:\n")
        print("press 13 to LOGOUT:\n")

        print("enter your choice")

        choice=int(input())
        if choice==1:
            addpatients()
        elif choice==2:
            addstaff()
        elif choice==3:
            patientsrecord()
        elif choice==4:
            staffrecord()
        elif choice==5:
            changepassword()
        elif choice==6:
            removepatients()
        elif choice==7:
            removestaff()
        elif choice==8:
            update_patient()
        elif choice==9:
            update_staff()
        elif choice==10:
            add_doctor()
        elif choice==11:
            removedoctor()
        elif choice==12:
            Approvalrequired()
        elif choice==13:
            front()
        else:
            print("!"*15,"INVALID CHOICE","!"*15)

        


def addpatients():
    
    y="y"
    while y=="y": 
        p=0
        print("*"*17,"ENTER PATIENT DETAILS")
        patientname=input("enter patient name:")

        for item in patientname:
            if item.isdigit()==True: 
               p=p+1
            else:
                 pass
        if p==0:
            age=input("enter patient age:")
            if age.isdigit()!=True:
                print("\n!!!!!!!!!!!!!!!!!invalid age!!!!!!!!!!!!!!!!!!!")
                print("         please try again            ")
                addpatients()

        else:
            print("\n!!!!!!!!!!!!!!!!!INVALID NAME!!!!!!!!!!!!!!!!!!!")
            print("         please try again            ")
            
            addpatients()
            return

        print("*"*13,"select your gender","*"*13) 
        print("if patient is male then press 1")
        print("if patient is female then press 2")
        choice=int(input())
        if choice==1:
            gender="male"
            
        elif choice==2:
            gender="female"
            

        else:
            print("!"*15,"INVALID CHOICE","!"*15)
            addpatients()
            
        phnumber=input("enter the patient 10 digit phone number:")

        if len(phnumber)==10:
            if phnumber.isalpha():
                print("invalid mobile number")
                addpatients()

            else:
                if phnumber.isdigit()!=True:
                    print("!"*15,"invalid mobile number","!"*15)
                    addpatients()
                else:
                    if phnumber.startswith("0"):
                        print("!"*13,"mobile number can not start with 0","!"*13)
                        addpatients()
                        

                    else:
                        
                        print("*"*15,"enter patient problem","*"*15)
                        print("1. eye problem")
                        print("2. ear problem")
                        print("3. nose problem")
                        print("4. throat problem")
                        print("5. hormones problem")
                        print("6. mouth problem")
                        print("7. any surgiical")
                        print("8. bone problem")
                        print("9. sugar patient")
                        print("10. Skin problem")
                        print("11. child problem")
                        print("12. other problem")
                        ch=int(input("enter the choice:"))
                        q=0
                        if ch==1:
                            q="eye problem"
                            pass
                        elif ch==2:
                            q="ear problem"
                            pass
                        elif ch==3:
                            q="nose problem"
                            pass
                        elif ch==4:
                            q="throat problem"
                            pass
                        elif ch==5:
                            q="hormones problem"
                            pass
                        elif ch==6:
                            q="mouth problem"
                            pass
                        elif ch==7:
                            q="surgerical problem"
                            pass
                        elif ch==8:
                            q="bone problem"
                            pass
                        elif ch==9:
                            q="sugar problem"
                            pass
                        elif ch==10:
                            q="skin problem"
                            pass

                        elif ch==12:
                            q="other problem"
                            pass
                        else:
                            print("invalid choice")
                            addpatients()

                        # Insert the patient information with the new patient ID
                        a = "INSERT INTO patient (pname, page, pgender, phoneno, patient_problem, admitdate) VALUES (%s, %s, %s, %s, %s, CURDATE())"
                        values = (patientname, age, gender, phnumber,q)

                        mycursor.execute(a, values)
                        obj.commit()
                        print("\n*****patient added SUCCESSFUL*****")
                        print("\n*****Patient added SUCCESSFULLY and patient id is",mycursor.lastrowid, "*****")
                        y=input("to add more patients press y and n to exit: ")
                        if y=="y":
                            addpatients()
                        elif y=='n':
                            admin()

                        else:
                            print("invalid input")
                            admin()




# for add staff
def addstaff():
    y="y"
    while y=="y":
        p=0
        print("")
        print("*"*17,"ENTER STAFF DETAILS","*"*17)
        staffname=input("enter the staff name:")
        for item in staffname:
            if item.isdigit()==True:
                p=p+1
            else:
                pass
        if p==0:
            staffage=input("enter the age of staff:")

            if staffage.isdigit()!=True:
                print("!"*17,"invalid AGE","!"*17)
                print("please try again")
                addstaff()
            else:
                print("*"*13,"select gender","*"*13)
                print("if staff is male then press 1")
                print("if staff is female the press 2")
                
                choice=int(input())
                
                if choice==1:
                    gender="male"
                    pass
                
                elif choice==2:
                    gender="female"
                    pass
                
                else:
                    print("!"*15,"INVALID CHOICE","!"*15)
                    addstaff()
                    return
                
                staffphnumber=input("enter the staff phone number:")
                if len(staffphnumber)==10:
                    if staffphnumber.isalpha():
                        print("!"*15,"invalid mobile number","!"*15)
                        addstaff()
                    else:
                        

                        if staffphnumber.startswith("0"):
                            print("!"*13,"mobile number can not start with 0","!"*13)

                        else:
                            salary=input("enter the salary")
                            if salary.isdigit()!=True:

                                print("!"*15,"INVALID SALARY","!"*15)
                                addstaff()

                            else:
                                b = "INSERT INTO staff (staffname,staffage,staffgender,staffphoneno,dateofjoining,salary) VALUES (%s, %s, %s, %s, CURDATE(),%s)"
                                values = (staffname, staffage,gender, staffphnumber,salary)
                                mycursor.execute(b, values)
                                obj.commit()
                         
                                print("\n*****staff added SUCCESSFULLY and staff id is", mycursor.lastrowid, "*****")

                                y=input("Do you want to add more staff(y/n):")
                                print("")
                                if y=="y":
                                    addstaff()
                                else:
                                    admin()
                                
                                
                            


                              

        else:
            print("!"*17,"invalid PHONE NUMBER","!"*17)
            print("please try again")
            addstaff()
    else:
        print("!"*17,"invalid NAME","!"*17)
        print("please try again")
        addstaff()
        return



# for patient record
def patientsrecord():
    y="y"
    while y=="y":
        pid=input("enter patient ID:")
        if pid.isdigit()!=True:
            print("!"*15,"INVALID ID","!"*15)

        else:
            a="select patientid from patient where patientid={}".format(pid)
            mycursor.execute(a)
            b=mycursor.fetchall()

            if len(b)<1:
                a="select patientid from patientrecord where patientid={}".format(pid)
                mycursor.execute(a)
                b=mycursor.fetchall()

                if len(b)<1:
                    print("!"*17,"INVALID PATIENT ID","!"*17) 
                    print("OR".center(50))
    
                    print("!"*12," if ID is incorrect, please try again","!"*12)
                else:
                    result="select * from patientrecord where patientid={}".format(pid)
                    mycursor.execute(result)
                    result1=mycursor.fetchall()
                    print("*"*12,"PATIENT DETAILS ARE GIVEN BELOW:","*"*12)
                    print("\n patientid is:",result1[0][0])
                    print("\n patient name is:",result1[0][1])
                    print("\n patient age is:",result1[0][2])
                    print("\n patient gender is:",result1[0][3])
                    print("\n patient phone number is:",result1[0][4])
                    print("\n patient admit date:", result1 [0][5])
                    print("\n patient discharge date:",result1[0][6])
                    y=input("Do you want more patient record(y/n):")
            else:

                result="select * from patient where patientid={}".format(pid)
                mycursor.execute(result)
                result1=mycursor.fetchall()
                print("*"*12,"PATIENT DETAILS ARE GIVEN BELOW:","*"*12)
                print("\n patient id is:",result1[0][0])
                print("\n patient name is:",result1[0][1])
                print("\n patient age is:", result1[0][2])
                print("\n patient gender is:",result1[0][3])
                print("\n patient problem:",result1[0][6])
                print("\n patient phone number is:",result1[0][4])
                print("\n patient admit date:", result1[0][5])
                
                y=input("Do you want more patient record(y/n):")
                if y=="y":
                    patientsrecord()
                elif y=='n':
                    admin()
                else:
                    print("invalid input")
                    admin()


##for staff record
def staffrecord():
    y='y'
    while y=='y':
        sid=input("enter staff ID")
        if sid.isdigit()!=True:
            print("!"*15,"INVALID ID","!"*15)

        else:
            a="select staffid from staff where staffid={}".format(sid)
            mycursor.execute(a)
            b=mycursor.fetchall()
            
            if len(b)<1:
                a="select staffid from staffrecord where staffid=0}".format(sid)
                mycursor.execute(a)
                b=mycursor.fetchall()

                if len(b)<1:
                    print("!"*17,"INVALID PATIENT ID","!"*17)
                    print("OR".center(50))
                    print("*"*12,"CHECK IN PRESENT STAFF RECORD","*"*12)
                    print("!"*12," if ID is incorrect, please try again","!"*12)

                else:
                    result="select from staffrecord where staffid=".format(sid)
                    mycursor.execute(result)
                    result1=mycursor.fetchall()
                    print("*"*12,"STAFF DETAILS ARE GIVEN BELOW:","*"*12)
                    print("\n staff id is:", result1[0][0])
                    print("\n staff name is:", result1[0][1])
                    print("\n staff age is:",result1[0][2])
                    print("\n staff gender is:",result1[0][3])
                    print("\nstaff phone number is:", result1 [0][4]) 
                    print("\n staff date of joining:", result1[0][5])
                    print("\n staff salary: Rs", result1[0][6])
                    print("\n staff total working day:", result1[0][7])

                    y=input("Do you want more staff record(y/n):")

            else:
                result="select * from staff where staffid={}".format(sid)
                mycursor.execute(result)
                result1=mycursor.fetchall()
                print("*"*12,"STAFF DETAILS ARE GIVEN BELOW:","*"*12) 
                print("\n staff id is:",result1[0][0])
                print("\nstaff name is:", result1[0][1])
                print("\nataff age is:",result1[0][2])
                print("\nstaff gender is:",result1[0][3])
                print("\nstaff phone number is:", result1 [0][4])
                print("\nstaff date of joining:", result1 [0][5])
                print("\nstaff salary: Rs", result1[0][6])
                
                y=input("Do you want more staff record(y/n):")
                if y=='y':
                    staffrecord()

                elif y=="n":
                    admin()

                else:
                    print("invalid input")
                    admin()


# to change password
def changepassword():

    old=input("enter the old password:\n")
    password1="select * from password"
    mycursor.execute(password1)
    password2=mycursor.fetchall()
    if old==password2[0][0]:
        new=input("enter the new password:")
        new1=input("re-enter the new password:")
        if new==new1:
            a="insert into password values('{}')".format(new1)
            mycursor.execute(a)
            b="delete from password where password='{}'".format(old)
            mycursor.execute(b)
            obj.commit()
            print("*"*17,"\nPASSWORD CHANGE SUCCESSFUL","*"*17)
        else:
            print("\n*******INCORRECT PASSWORD!!!***********")
            print("***TRY AGAIN***")

    else:
        print("\n**********************WRONG PASSWORD!!!***********************\n")
        admin()




# to remove patient from hospital
def removepatients():
    y="y"
    while y=="y":
        ID=int(input("enter patient id "))
        a="select * from patient where patientid={}".format(ID)
        mycursor.execute(a) 
        result1=mycursor.fetchall()
        if len(result1)<1:
            b="select * from patientrecord where patientid={}".format(ID) 
            mycursor.execute(b)
            result2=mycursor.fetchall()
            if len(result2)<1:
                print("\n##########PATIENT ID ARE NOT CORRECT!!!!##########")
            else:
                print("############PATIENT IS ALREADY REMOVE!!!!!!########## ")
                admin()

        else:
            print("Do you confirm to remove this", ID, "if yes press(y) else press any key except(y)):") 
            ch=input("")
            if ch=="y":
                b="select * from patient where patientid={}".format(ID)
                mycursor.execute(b)
                result2=mycursor.fetchall()
                pname=result2[0][1]
                page=result2[0][2]
                pgender=result2[0][3]
                phoneno=result2[0][4]
                admitdate=result2[0][5]
                admitdate=str(admitdate)
                admitdate=admitdate.replace("-","")
                patientrecord="insert into patientrecord values({}, '{}',{},'{}',{},{},{})".format(ID,pname, page,pgender,phoneno, admitdate,"curdate()")
                mycursor.execute(patientrecord)
                deletepatient="delete from patient where patientid={}".format(ID)
                mycursor.execute(deletepatient)

                print("\n****DISCHARGE SUCCESSFUL*****")
                obj.commit()
                y=input("Do you want more remove patient(y/n):")
            else:
                print("you have declined to remove more patients\n")
                admin()



# to remove staff from hospital
def removestaff():
    while True:
        staff_id = int(input("Enter staff ID: "))
        # Check if the staff ID exists in the staff table
        select_staff_query = "SELECT * FROM staff WHERE staffid = %s"
        mycursor.execute(select_staff_query, (staff_id,))
        staff_data = mycursor.fetchone()

        if staff_data is None:
            print("*************************Staff with ID", staff_id, "not found****************************.")
        else:
            # Check if the staff ID exists in the staffrecord table
            select_staffrecord_query = "SELECT * FROM staffrecord WHERE staffid = %s"
            mycursor.execute(select_staffrecord_query, (staff_id,))
            staffrecord_data = mycursor.fetchone()

            if staffrecord_data is None:
                # If staff ID is found in staff table but not in staffrecord table
                # Move data from staff table to staffrecord table
                insert_record_query = "INSERT INTO staffrecord (staffid, staffname, staffage, staffgender, staffphoneno, joiningdate, salary, total_working_day) VALUES (%s, %s, %s, %s, %s, %s, %s, CURDATE())"
                values = (staff_data[0], staff_data[1], staff_data[2], staff_data[3], staff_data[4], staff_data[5], staff_data[6])
                mycursor.execute(insert_record_query, values)

            # Delete staff from the staff table
            delete_staff_query = "DELETE FROM staff WHERE staffid = %s"
            mycursor.execute(delete_staff_query, (staff_id,))

            obj.commit()
            print("Staff with ID", staff_id, "has been removed.")

        another = input("Do you want to remove another staff (y/n): ")
        if another.lower() != "y":
            break






# to update patient name
def update_patient_name(ID):
    p=0
    name=input("enter the corrected patient name:")
    for item in name:
        if item.isdigit()==True:
            p=p+1
        else:
            pass
    
    if p==0:
        up="update patient set pname='{}' where patientid={}".format(name,ID)
        mycursor.execute(up)
        obj.commit()
        print("*"*15,"PATIENT NAME UPDATE SUCCESSFUL","*"*15)
        patient_again(ID)
        y=input("Do you want to update the name of more patient??(y/n):")
        if y=="y":
            update_patient()
        else:
            admin()

    else:
        print("!"*15,"INVALID NAME","!"*15)

# to update patient age 
def update_patient_age(ID):
    age=input("enter patient age:")
    if age.isdigit()!=True:
        print("!"*15,"INVALID AGE","!"*15)
        update_patient_age(ID)
    
    else:
        up="update patient set page={} where patientid={}".format(age,ID)
        mycursor.execute(up)
        obj.commit()
        print("*"*15,"PATIENT AGE UPDATE SUCCESSFUL","*"*15)
        patient_again(ID)
        y=input("Do you want to update the age of more patient??(y/n):")
        if y=="y":
            update_patient()
        else:
            admin()

# to update patient gender if male
def update_patient_male(ID):
    gender="male"
    up="update patient set pgender='{}' where patientid={}".format(gender,ID)
    mycursor.execute(up)
    obj.commit()
    print("*"*15,"PATIENT GENDER UPDATE SUCCESSFUL","*"*15)
    patient_again(ID)
    y=input("Do you want to update the gender of more patient??(y/n):")

    if y=="y":
        update_patient()
    else:
        admin()

# to update patient gender if female
def update_patient_female(ID):
    gender="female"
    up="update patient set pgender='{}' where patientid={}".format(gender,ID)
    mycursor.execute(up)
    obj.commit()
    print("*"*15,"PATIENT GENDER UPDATE SUCCESSFUL","*"*15)
    patient_again(ID)
    y=input("Do you want to update the gender of more patient??(y/n):")

    if y=="y":
        update_patient()
    else:
        admin()



def update_patient_phone_number(ID):
    phone = input("Enter the patient 10-digit phone number: ")
    
    if len(phone) == 10 and phone.isdigit():
        # Correct phone number format
        up = "UPDATE patient SET phoneno='{}' WHERE patientid={}".format(phone, ID)
        mycursor.execute(up)
        obj.commit()
        print("*" * 15, "PATIENT PHONE NUMBER UPDATE SUCCESSFUL", "*" * 15)
        patient_again(ID)
        y = input("Do you want to update the gender of more patients? (y/n): ")
        
        if y.lower() == "y":
            update_patient()
        else:
            admin()
    else:
        print("!" * 15, "INVALID PHONE NUMBER", "!" * 15)
        update_patient_phone_number(ID)




def patient_again(ID):
    m = print("Do you want to update more details of the same patient?")
    n = int(input("Press 1 to approve or 2 to deny:\n"))

    if n == 1:
        print("What do you want to update:")
        print("Press 1 to update patient name")
        print("Press 2 to update patient age")
        print("Press 3 to update patient gender")
        print("Press 4 to update patient phone number\n")
        var_again = int(input("Enter your choice:\n"))
        if var_again == 1:
            update_patient_name(ID)
        elif var_again == 2:
            update_patient_age(ID)
        elif var_again == 3:
            print("If the patient is male, then press 1") 
            print("If the patient is female, then press 2\n") 
            choice = int(input())
            if choice == 1:
                update_patient_male(ID)
            elif choice == 2:
                update_patient_female(ID)
            else:
                print("!" * 15, "INVALID CHOICE", "!" * 15)
                update_patient()
        elif var_again == 4:
            update_patient_phone_number(ID)
        else:
            print("#########----INVALID CHOICE----##########")
    elif n == 2:
        print("-------- ALRIGHT-------")
        print("Do you wish to visit the main menu again?")
        print("Press 1 to approve or 2 to uptate details of any other patient:\n")
        menu_again_choice = int(input())
        if menu_again_choice == 1:
            admin()
            
        elif menu_again_choice == 2:
            update_patient()

        else:
            print("#########Invalid choice#########")
            admin()
            
            


# to update patient information
def update_patient():
    y="y"
    while y=="y":
        ID=input("------enter patient ID :-------\n")
        if ID.isdigit()!=True:
            print("!"*15,"INVALID ID","!"*15)

        else:
            a="select * from patient where patientid={}".format(ID)
            mycursor.execute(a)
            result1=mycursor.fetchall()
            if len(result1)<1:
                print("\n#### ##### -----PATIENT ID is INCORRECT!!!!------ ######## #####")
                print("-----please try again-----")

            else:
                print("______what do you want to update first??______\n")
                print("press 1 to update patient name")
                print("press 2 to update patient age")
                print("press 3 to update patient gender")
                print("press 4 to update patient phone number\n")

                ch=int(input(""))
                if ch==1:
                    update_patient_name(ID)
                elif ch==2:
                    update_patient_age(ID)

                elif ch==3:
                    print("if patient is male then press 1") 
                    print("if patient is female then press 2\n") 
                    choice=int(input())
                    if choice==1:
                        update_patient_male(ID)
                    elif choice==2:
                        update_patient_female(ID)
                    else:
                        print("!"*15,"INVALID CHOICE","!"*15)
                elif ch==4:
                    update_patient_phone_number(ID)
                
                else:
                    print("!"*15,"INVALID CHOICE","!"*15)

                patient_again(ID)
                




# to update staff name
def update_staff_name(ID):
    p=0
    name=input("enter updated staff name:")
    for item in name:
        if item.isdigit()==True:
            p=p+1
        else:
            if p==0:
                pass
                up="update staff set staffname='{}' where staffid={}".format(name,ID)
                mycursor.execute(up)
                obj.commit()
                print("*"*15,"STAFF NAME UPDATED SUCCESSFUL","*"*15)
                staff_again(ID)

                y=input("Do you want to update the details of more staff??(y/n):")
                if y=="y":
                    update_staff()
                else:
                    admin()

            else:
                print("!"*15,"INVALID NAME","!"*15) 
                print("!"*15,"TRY AGAIN","!"*15) 
                update_staff_name(ID)

# to update staff age
def update_staff_age(ID):
    age=input("enter staff new age:")
    if age.isdigit()!=True:
        print("!"*15,"INVALID AGE","!"*15)
        print("!"*15,"TRY AGAIN","!"*15)
        update_staff_age(ID)
    else:
        up="update staff set staffage={} where staffid={}".format(age, ID) 
        mycursor.execute(up)
        obj.commit()
        print("*"*15,"STAFF AGE UPDATED SUCCESSFUL","*"*15)
        staff_again(ID)
        y=input("Do you want to update the age of more staff??(y/n):")
        if y=="y":
            update_staff()
        else:
            admin()

# to update staff gender if male
def update_staff_male(ID):
    gender="male"
    up="update staff set staffgender='{}' where staffid={}".format(gender,ID)
    mycursor.execute(up)
    obj.commit()
    print("*"*15,"STAFF GENDER UPDATED SUCCESSFUL","*1"*5)
    staff_again(ID)
    y=input("Do you want to update the details of more staff??(y/n):")
    if y=="y":
        update_staff()
    else:
        admin()

# to update staff gender if female
def update_staff_female(ID):    
    gender="female"
    up="update staff set staffgender='{}' where staffid={}".format(gender,ID) 
    mycursor.execute(up)
    obj.commit()
    print("*"*15,"STAFF GENDER UPDATED SUCCESSFUL","*"*15)
    staff_again(ID)
    y=input("Do you want to update the details of more staff??(y/n):")
    if y=="y":
      update_staff()
    else:
        admin()

# for update staff phone number
def update_staff_phone(ID):
    phone-input("enter the staff 10 digit new phone number:")
    if len(phone)==10:
        if phone.isalpha():
            print("invalid mobile number")
            update_staff_phone(ID)
        else:
            if phone.isdigit()!=True:
                print("!"*15,"invalid mobile number","!"*15)
                update_staff_phone(ID)
            else:
                if phone.startsWith("0"):
                    print("!"*13,"mobile number can not start with 0","!"*13)
                    update_staff_phone(ID)

                else:
                    up="update staff set staffphoneno={} where staffid={}".format(phone,ID)
                    mycursor.execute(up)
                    obj.commit()
                    print("*"*15,"STAFF PHONE NUMBER UPDATED SUCCESSFUL","*"*15)
                    staff_again(ID)
                    y=input("Do you want to update the details of more staff??(y/n):")
            if y=="y":
                update_staff()
            else:
                admin()
    else:
        print("!"*15,"INVALID PHONE NUMBER","!"*15) 
        print("!"*15,"TRY AGAIN","!"*15)
        update_staff_phone(ID)

# to update staff salary
def update_staff_salary(ID):
    salary=input("enter the salary")
    if salary.isdigit()!=True:
        print("!"*15,"INVALID SALARY","!"*15)
        update_staff_salary(ID)

    else:
        up="update staff set salary={} where staffid={}".format(salary,ID)
        mycursor.execute(up)
        obj.commit()
        print("*"*15,"SALARY UPDATED SUCCESSFUL","*"*15)
        staff_again(ID)
        y=input("Do you want to update the details of more staff??(y/n):") 
        if y=="y":
            update_staff()
        else:
            admin()





def staff_again(ID):
    m = print("Do you want to update more details of the same staff?")
    n = int(input("Press 1 to approve or 2 to deny:\n"))

    if n == 1:
        print("----------------what do you want to update??----------------------/n")
        print("|_______________press 1 for update staff name____________________|")
        print("------------------------------------------------------------------")
        print("|_______________press 2 for update staff age_____________________|")
        print("------------------------------------------------------------------")
        print("|_______________press 3 for update staff gender__________________|")
        print("------------------------------------------------------------------")
        print("|_______________press 4 for update staff phone number____________|")
        print("------------------------------------------------------------------")
        print("|_______________press 5 for update staff salary__________________|")
        print("------------------------------------------------------------------")
        
        
        varstaff_again = int(input("Enter your choice:\n"))
        if varstaff_again == 1:
            update_staff_name(ID)
        elif varstaff_again == 2:
            update_staff_age(ID)
        elif varstaff_again == 3:
            print("If the staff is male, then press 1") 
            print("If the staff is female, then press 2\n") 
            choice = int(input())
            if choice == 1:
                update_staff_male(ID)
            elif choice == 2:
                update_staff_female(ID)
            else:
                print("!" * 15, "INVALID CHOICE", "!" * 15)
                update_staff()
        elif varstaff_again == 4:
            update_staff_phone_number(ID)

        elif varstaff_again == 5:
            update_staff_salary(ID)
            
        else:
            print("#########----INVALID CHOICE----##########")
    elif n == 2:
        print("-------- ALRIGHT-------")
        print("Do you wish to visit the main menu again?")
        print("Press 1 to approve or 2 to uptate details of any other staff:\n")
        menu_again_choice = int(input())
        if menu_again_choice == 1:
            admin()
            
        elif menu_again_choice == 2:
            update_staff()

        else:
            print("#########Invalid choice#########")
            admin()
            
            




            

# to update staff information
def update_staff():
    y="y"
    while y=="y":
        ID=input("enter staff id:")
        if ID.isdigit()!=True:
            print("!"*15,"INVALID ID","!"*15)

        else:
            a="select * from staff where staffid={}".format(ID)
            mycursor.execute(a)
            result1=mycursor.fetchall()
            
            if len(result1)<1:
                print("\n##########--------STAFF_ID is NOT CORRECT!!!!--------##########")
                print("---------please try again----------")
            
            else:
                print("----------------what do you want to update??----------------------/n")
                print("|_______________press 1 for update staff name____________________|")
                print("------------------------------------------------------------------")
                print("|_______________press 2 for update staff age_____________________|")
                print("------------------------------------------------------------------")
                print("|_______________press 3 for update staff gender__________________|")
                print("------------------------------------------------------------------")
                print("|_______________press 4 for update staff phone number____________|")
                print("------------------------------------------------------------------")
                print("|_______________press 5 for update staff salary__________________|")
                print("------------------------------------------------------------------")
                ch=int(input(""))

                if ch==1:
                    update_staff_name(ID)

                elif ch==2:
                    update_staff_age(ID)

                elif ch==3:
                    print("if staff is male then press 1")
                    print("if staff is female then press 2") 
                    choice=int(input())
                    if choice==1:
                        update_staff_male(ID)
                    elif choice==2:
                        update_staff_female(ID)
                    else:
                        print("!"*15,"INVALID CHOICE","!"*15) 
                        print("!"*15,"TRY AGAIN","!"*15)

                elif ch==4:
                    update_staff_phone(ID)
                elif ch==5:
                    update_staff_salary (ID)
                else:
                    print("!"*15,"INVALID CHOICE","!"*15) 
                    print("!"*15,"TRY AGAIN","!"*15)





def add_doctor():
    print("*" * 15, "ENTER DOCTOR DETAILS", "*" * 15)
    name = input("Enter doctor name: ")
    department = input("Enter the department: ")
    gender = input("Enter doctor's gender (male/female): ")

    if gender.lower() not in ['male', 'female']:
        print("Invalid gender. Please enter 'male' or 'female'.")
        add_doctor()

    work_experience = input("Enter the work experience (in years): ")
    if not work_experience.isdigit():
        print("Invalid work experience. Please enter a valid number.")
        add_doctor()

    phone_number = input("Enter the doctor's 10-digit phone number: ")
    if len(phone_number) != 10 or not phone_number.isdigit():
        print("Invalid phone number. Please enter a 10-digit number.")
        add_doctor()

    salary = input("Enter salary: ")
    if not salary.isdigit():
        print("Invalid salary. Please enter a valid number.")
        add_doctor()

    # Correct SQL query with placeholders
    sql = "INSERT INTO doctor (doctorname, department, gender, work_experience, phone_number, date_of_joining, salary) VALUES (%s, %s, %s, %s, %s, curdate(), %s)"
    values = (name, department, gender, work_experience, phone_number, salary)
    insert_login_query = "INSERT INTO login (name, mobile_number) VALUES (%s, %s)"
    login_values = (name, phone_number)
    mycursor.execute(insert_login_query, login_values)
    mycursor.execute(sql, values)
    obj.commit()

    # Get the newly inserted doctor's ID
    doctor_id = mycursor.lastrowid

    print("*" * 15, f"DOCTOR ADDED SUCCESSFULLY. DOCTOR ID: {doctor_id}", "*" * 15)
    chh = int(input("To add another doctor press 1 or to view the main menu press 2: \n"))
    if chh == 1:
        add_doctor()
    elif chh == 2:
        admin()
    else:
        print("###################invalid choice##################")
        admin()


# to Remove doctor
def removedoctor():
    y="y"
    while y=="y":
        ID=int(input("Enter doctor id: "))
        a="select * from doctor where doctorid={}".format(ID)
        mycursor.execute(a)
        result1=mycursor.fetchall()
        if len(result1)<1:
            b="select * from doctorrecord where doctorid={}".format(ID)
            mycursor.execute(b)
            result2=mycursor.fetchall()
            if len(result2)<1:
                print("\n##########DOCTOR ID IS NOT CORRECT!!!!##########")
            
            else:
                print("############ DOCTOR IS ALREADY REMOVED!!!!!!########## ")
    
        else:
            print("Do you confirm remove this ID",ID,"? \nif yes then press(y) else press any key except(y)):") 
            ch=input("")
            if ch=="y":
                b="select * from doctor where doctorid={}".format(ID)
                mycursor.execute(b)
                result2=mycursor.fetchall()
                doctorname=result2[0][1]
                dateofjoinig=result2[0][6]
                dateofjoinig=str(dateofjoinig)
                dateofjoinig=dateofjoinig.replace("-","")
                department=result2[0][2]
                gender=result2[0][3]
                phone_number=result2[0][5]

                doctorrecord="insert into doctorrecord values({},'{}','{}','{}',{},{},{})".format(ID, doctorname,
                                                                                                  department,gender,phone_number, dateofjoinig,"curdate()")
                mycursor.execute(doctorrecord)

                deletedoctor="delete from doctor where doctorid={}".format(ID)
                mycursor.execute(deletedoctor)
                print("\n***************REMOVE SUCCESSFUL****************\n")
                obj.commit()
                y=input("Do you want more remove doctors(y/n):")
                if y=='y':
                    removedoctor()
                else:
                    print("\n---------Heading you to the main menu---------")
                    admin()
                
            else:
                print("#######You have declined the conformation########\n\n---------Heading you to the main menu---------")
                admin()



## for the approval or rejection of doctor applications
           
def get_count_of_pending_approvals():
    approval_query = "SELECT COUNT(*) FROM job WHERE status = 'HOLD'"
    mycursor.execute(approval_query)
    count = mycursor.fetchone()[0]
    return count

def display_pending_approvals():
    details_query = "SELECT * FROM job WHERE status = 'HOLD'"
    mycursor.execute(details_query)
    applications = mycursor.fetchall()

    print("*" * 15, "Details of Doctors Applying for Jobs", "*" * 15)
    for application in applications:
        print("Apply ID:", application[0])
        print("Apply Date:", application[1])
        print("Dr. Name:", application[2])
        print("Department:", application[3])
        print("Work Experience in this Department:", application[4])
        print("Gender:", application[5])
        print("")

        what_to_do=int(input("enter 1 to reject application or 2 to approve any application: "))
        if what_to_do==1:
            reject_doctor_application()

        elif what_to_do==2:
            approve_doctor_application()
        else:
            print("invalid input")
            admin()
            
            
            


def approve_doctor_application():
    count = get_count_of_pending_approvals()
    if count < 1:
        print("No approvals pending.")
        return


    apply_id = int(input("Enter the Apply ID for approval: "))
    approve_query = f"SELECT * FROM job WHERE apply_id = {apply_id} AND status = 'HOLD'"
    mycursor.execute(approve_query)
    application = mycursor.fetchone()

    if application is None:
        print("Invalid Apply ID or the application is already processed.")
        return

    salary_query = f"SELECT salary FROM salary WHERE department = '{application[3]}'"
    mycursor.execute(salary_query)
    salary = mycursor.fetchone()

    if salary is None:
        print("Salary information not found for the specified department.")
        return

    insert_query = "INSERT INTO doctor VALUES (NULL, %s, %s, %s, %s, %s, CURDATE(), %s)"
    doctor_data = (application[2], application[3], application[5], application[4], application[6], salary[0])
    mycursor.execute(insert_query, doctor_data)
    obj.commit()

    update_query = f"UPDATE job SET status = 'APPROVED' WHERE apply_id = {apply_id}"
    mycursor.execute(update_query)
    obj.commit()
    print("")

    print("*" * 15, "APPROVAL SUCCESSFUL", "*" * 15)

def reject_doctor_application():
    count = get_count_of_pending_approvals()
    if count < 1:
        print("No rejections pending.")
        return

    

    apply_id = int(input("Enter the Apply ID for rejection: "))
    reject_query = f"UPDATE job SET status = 'REJECTED' WHERE apply_id = {apply_id} AND status = 'HOLD'"
    mycursor.execute(reject_query)
    obj.commit()
    print("")
    print("*" * 15, "REJECTION SUCCESSFUL", "*" * 15)

   


# to front page design
def front():
    print("OPENING MENU TO VISIT \n")
    print("-----------------------------------------------------------------")
    print("|                     press 1 for ADMIN:                        |")
    print("-----------------------------------------------------------------")
    print("|                     press 2 for PATIENT:                      |")
    print("-----------------------------------------------------------------")
    print("|                     press 3 For DOCTER:                       |")
    print("-----------------------------------------------------------------")
    print("|                     press 4 For EXIT:                         |")
    print("-----------------------------------------------------------------")

    ch = int(input())
    if ch == 1:
        password = input("Enter the password:")
        password1 = "SELECT * FROM password"
        mycursor.execute(password1)
        password2 = mycursor.fetchall()
        if password == password2[0][0]:
            admin()
        else:
            print("\n******* INCORRECT PASSWORD!!! *******")
            print("****** TRY AGAIN ******\n")
            front()
    if ch == 2:
        patient()
    elif ch == 3:
        doctor_create()
    elif ch == 4:
        print("*" * 16, "THANK YOU", "*" * 16)
        while True:
            break
    else:
        print("INVALID CHOICE")
        front()

# for patient use
def patient():
    print("*"*15,"WELCOME TO OUR MOBILE APPLICATION","*"*15)
    print("press 1 to book appointment")
    print("press 2 to see appointment prices")
    print("press 3 to visit the front menu again")
    ch=int(input(""))
    if ch==1:
        appointment()
    elif ch==2:
        treatment_price()
    elif ch==3:
        front()
    else:
        print("!!!!!!invalid choice!!!!!!\n")
        patient()

# for book appointment for patient
def appointment():
    print("#" * 15, "SELECT YOUR PROBLEM:", "#" * 15)
    print("1. For eye problem")
    print("2. For ear problem")
    print("3. For nose problem")
    print("4. For throat problem")
    print("5. For hormones problem")
    print("6. For mouth problem")
    print("7. For any surgical")
    print("8. For bone problem")
    print("9. For sugar patient")
    print("10. For Skin problem")
    print("11. For child problem")
    print("12. For other problem")
    print("13. for back again\n")

    ch = input("enter the choice:")
    if ch == "1":
        print("\nThese are the doctors that are specialists in Eye")
        q = "Eye"
        app(q)

    elif ch == "2":
        q = "ear"
        app(q)
    elif ch == "3":
        q = "nose"
        app(q)
    elif ch == "4":
        q = "throat"
        app(q)
    elif ch == "5":
        q = "hormones"
        app(q)
    elif ch == "6":
        q = "mouth"
        app(q)
    elif ch == "7":
        q = "surgical"
        app(q)
    elif ch == "8":
        q = "bone"
        app(q)
    elif ch == "9":
        q = "sugar"
        app(q)
    elif ch == "10":
        q = "Skin"
        app(q)
    elif ch == "11":
        q = "child"
        app(q)
    elif ch == "12":
        q = "other"
        app(q)
    elif ch == "13":
        patient()
    else:
        print("invalid choice\n")
        appointment()


def app(q):
    a = "SELECT department FROM symptoms_and_dept WHERE symptoms LIKE '%{}%'".format(q)
    mycursor.execute(a)
    department_result = mycursor.fetchall()

    if not department_result:
        print("No department found for the given symptom.")
        return

    department = department_result[0][0]

    b = "SELECT * FROM doctor WHERE department = '{}'".format(department)
    mycursor.execute(b)
    doctor_list = mycursor.fetchall()
    print("Department:", department)

    if not doctor_list:
        print("No doctors found for the given department.")
        return

    print("There are {} doctors".format(len(doctor_list)))

    for doctor in doctor_list:
        print("Doctor ID:", doctor[0])
        print("Doctor name:", doctor[1])
        print("Department:", doctor[2])
        print("Gender:", doctor[3])
        print("Work experience:", doctor[4])
        print("")

    y = "y"
    while y == "y":
        book = input("Do you want to book an appointment? (y/n): ")
        if book.lower() == "y":
            p_name = input("Enter patient name: ")
            p_age = int(input("Enter patient age: "))
            gender=int(input('press 1 if gender of patient is female or 2 if gender is male: '))
            if gender==1:
                gender='Female'
            elif gender==2:
                gender='Male'
            else:
                print('Invalid input')
                front()
            phone_no = int(input("Enter patient's phone number: "))

            if len(str(phone_no)) != 10 or str(phone_no)[0] == '0':
                print("Invalid phone number!!!!!!!")
                front()
            else:
                ID = int(input('Enter id of doctor whose appointment you want: '))
                if ID not in [doc[0] for doc in doctor_list]:
                    print("Invalid id!!!!!!!!!!")
                    app(q)
                else:
                    print('Doctor selected: ', [doc[1] for doc in doctor_list if doc[0] == ID][0])
                    s = int(input(f'Press 1 to book an appointment with doctor {ID} or any other integer to deny appointment: '))
                    if s == 1:
                        insert_query = f"INSERT INTO APPOINTMENT (patient_name, age, gender, mobile_number, doctorid, department) " \
                                       f"VALUES ('{p_name}', {p_age}, '{gender}', {phone_no}, {ID}, '{department}')"
                        mycursor.execute(insert_query)
                        obj.commit()
                        print("\nAppointment added successfully!")
                    else:
                        print('Appointment not booked')
                        front()

# for treatment price
def treatment_price():
    a = "select * from treatment_price"
    mycursor.execute(a)
    treatment_prices = mycursor.fetchall()

    for i in treatment_prices:
        print("        ", "--" * 28)
        print("     |", f"{i[0]} price are: Rs {i[1]} per appointment|")

    print("        ", "--" * 28)
    print("")

    ch = input("Do you want to book an appointment? (y/n):")
    if ch.lower() == "y":
        print("Okay")
        appointment()
    else:
        print("")
        patient()


# for create account as a doctor
# for create account as a doctor
def signin():
    mobile_number = input("Enter your mobile number: ")

    # Check if the doctor exists in the doctor table
    check_doctor_query = "SELECT * FROM doctor WHERE phone_number = %s"
    check_doctor_values = (mobile_number,)

    mycursor.execute(check_doctor_query, check_doctor_values)
    existing_doctor = mycursor.fetchall()

    if not existing_doctor:
        print("You are not added as a doctor by the admin. Contact the admin to create an account.")
        return

    # Check if the doctor exists in the login table
    check_login_query = "SELECT * FROM login WHERE mobile_number = %s"
    check_login_values = (mobile_number,)

    mycursor.execute(check_login_query, check_login_values)
    existing_login = mycursor.fetchall()

    if not existing_login or existing_login[0][2] is None:
        print("Your account does not have a password set. Please set up your password.")
        new_password = input("Enter your new password: ")
        confirm_password = input("Re-enter to confirm your password: ")
        

        if new_password == confirm_password:
            # Update the existing record in the login table with the new password
            update_password_query = "UPDATE login SET password = %s, password_set = 'y' WHERE mobile_number = %s"
            update_password_values = (new_password, mobile_number)
            mycursor.execute(update_password_query, update_password_values)
            obj.commit()
            print("-------Password set-up succesful-----")
            doctor_create()
            
        else:
            print("Password confirmation does not match. Try again.")
            signin()
    else:
        print("You are already logged in.")
        front()





# for doctor login

def login_doctor():
    mobile_number = input("Enter your mobile number: ")
    password = input("Enter your password: ")

    # Check if credentials exist in the login table
    login_query = "SELECT * FROM login WHERE mobile_number = %s AND password = %s"
    mycursor.execute(login_query, (mobile_number, password))
    login_result = mycursor.fetchone()

    if login_result:
        # Check if the doctor is present in the doctor table
        doctor_query = "SELECT * FROM doctor WHERE phone_number = %s"
        mycursor.execute(doctor_query, (mobile_number,))
        doctor_result = mycursor.fetchone()

        if doctor_result:
            print("Login successful!")
            doctor(mobile_number)
            # Proceed with whatever actions you need for a logged-in doctor
        else:
            print("Invalid entry. Doctor not found.")
    else:
        print("Invalid credentials. Login failed.")



# to login to doctor section
def doctor_create():
    print("press 1 for create account")
    print("press 2 for login")
    print("press 3 for back")
    choice=int(input(""))
    if choice==1:
        signin()
    elif choice==2:
        login_doctor()
    elif choice==3:
        front()
    else:
        print("*"*12,"INVALID CHOICE!!!","*"*12)
        print("")
        doctor_create()

# for doctor section
def doctor(mobile_number):
    print("*"*15,"WELCOME TO DOCTOR SECTION","*"*15)
    print("press 1 for apply job")
    print("press 2 for view appointment")
    print("press 3 for view salary department wise")
    print("press 4 for exit")
    ch=int(input(""))
    if ch==1:
        apply_job(mobile_number)
    elif ch==2:
        view_appointment(mobile_number)
    elif ch==3:
        salary()
    elif ch==4:
        doctor_create()
    else:
        print("*"*12,"INVALID CHOICE!!!",'*'*12)
        print("")
        doctor(mobile_number)

# to apply job as a doctor
def apply_job(mobile_number):
    select="select * from doctor where phone_number={}".format(mobile_number)
    mycursor.execute(select)
    select=mycursor.fetchall()
    if len(select)<1:
        name=input("enter your name")
        p=0
        for item in name:
            if item.isdigit()==True:
                p=p+1
            else:
                pass

        if p==0:
            print("*"*15,"SELECT YOUR DEPARTMENT","*"*15)
            print("1.Medicine")
            print("2.Eye")
            print("3.Gynecology")
            print("4.Dental")
            print("5.surgical")
            print("6.Orthopedic")
            print("7.ENT") 
            print("8.Diabetic")
            print("9.Child")
            print("10.Skin")
            ch=int(input("enter your choice:"))
            if ch==1:
                department="Medicine"
            elif ch==2:
                department="Eye"
            elif ch==3:
                department="Gynecology"
            elif ch==4:
                department="Dental"
            elif ch==5:
                department="surgiical"
            elif ch==6:
                department="Orthopedic"
            elif ch==7:
                department="ENT"
            elif ch==8:
                department="Diabetic"
            elif ch==9:
                department="Child"
            elif ch==10:
                department="Skin"
            else:
                print("!"*15,"INVALID CHOICE","!"*15)
                apply_job(mobile_number)
                pass
            work_experience=input("enter your work experience in this field (like year,month)")
            if work_experience.isalnum():
                print("if you are male then press 1")
                print("if you are female the press 2")
                choice=int(input())
                if choice==1:
                    gender="male"
                    pass
                elif choice==2:
                    gender="female"
                    pass
                else:
                    print("!"*15,"INVALID CHOICE","!"*15)
                    apply_job(mobile_number)
                #phone_number="select * from login where mobile_number={}".format(mobile_number) 
                if len(mobile_number)==10:
                    a="insert into job values({},{},'{}','{}',{},'{}',{},'{}')".format('apply_id=apply_id+1000',"curdate()",name,department,work_experience,gender,mobile_number,'HOLD')
                    mycursor.execute(a)
                    obj.commit()
                    apply_id="SELECT apply_id FROM job WHERE dname = '{}' AND department = '{}'".format(name, department)
                    mycursor.execute(apply_id)
                    apply_id=mycursor.fetchall()
                    print("Thank you for apply in ABC hospital and your apply ID is:",apply_id[0][0])
                    front()
                else:
                    print("\n!!!!!!!!!!!!!!!!!invalid phone number!!!!!!!!!!!!!!!!!!!")
                    print("please try again")
            else:
                print("*"*12,"INVALID NAME!!!","*"*12) 
                apply_job(mobile_number)
        else:
            print("*"*14,"You are already doctor in this hospital","*"*14)
            print("*"*16,"You can not apply for job","*"*16) 
            doctor(mobile_number)

# for check appointment
def view_appointment(mobile_number):
    # Using parameterized query to avoid SQL injection
    query = """
    SELECT * FROM doctor
    INNER JOIN appointment ON doctor.doctorid = appointment.doctorid
    WHERE doctor.phone_number = %s
    """
    
    mycursor.execute(query, (mobile_number,))
    appointments = mycursor.fetchall()

    if not appointments:
        print("*" * 15, "NO APPOINTMENT", "*" * 15)
        doctor_create()
    else:
        total_appointments = len(appointments)
        print("Total number of appointments:", total_appointments)
        print("")

        for appointment in appointments:
            print("Patient name:", appointment[8])
            print("Patient age:", appointment[9])
            print("Patient gender:", appointment[10])
            print("Patient mobile number:", appointment[11])
            print("")
        print("\n\n")

        doctor_create()


# To check salary of doctor
def salary():
    a="select * from salary"
    mycursor.execute(a)
    result1=mycursor.fetchall()
    for i in range (len(result1)):
        print("DEPARTMENT:", result1 [i][0], "," "SALARY:","Rs", result1 [i][1])
        




##FRONT PAFE and front FUNCTION CALLING
front_page()


front()



     









                            

                    
