import pandas as pd 


df = pd.read_csv(r"C:\Users\HH-Com\Desktop\student result projesct\student result.csv")


num = len(df)


while True:
   
    exc = input("Enter 'q' to quit: ")
    if exc == "q":
        break
    else:
        name = input("Enter student name: ")
        rollno = int(input("Enter student roll number: "))
        sub1 = int(input("Enter your marks for subject 1: "))
        sub2 = int(input("Enter your marks for subject 2: "))
        sub3 = int(input("Enter your marks for subject 3: "))
        sub4 = int(input("Enter your marks for subject 4: "))
        sub5 = int(input("Enter your marks for subject 5: "))

        # Calculate total marks and percentage
        total_marks = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = (total_marks / 500) * 100
        
        # Determine pass/fail status
        if percentage >= 50:
            status = "Pass"
        else:
            status = "Fail"

        df.loc[num] = [name, rollno, sub1, sub2, sub3, sub4, sub5, percentage, status]

       
        num=num+1

        df.to_csv(r"C:\Users\HH-Com\Desktop\student result projesct\student result.csv", index=False)

        print("Student data saved successfully.")

