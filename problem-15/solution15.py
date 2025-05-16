student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46]

def check_marks(marks,student_name):
      
    print(f"\n📄 Result for {student_name}:") #f"..." = lets you use the variable student_name inside the string
                                              #{student_name} will be replaced with the actual name
    if any(mark < 40 for mark in marks):
        print("❌ FAILED (One or more marks are below 40)")
    else:
        average=sum(marks)/len(marks)
        print(f"✅ PASSED. Average Marks: {average:.2f}") #.2f	Formats the number to show 2 decimal places only.Average Marks: 73.46
                                                          #:.2f means:-    : → Start formatting,.2 → Show 2 digits after the decimal,f → Treat the number as a float
                                                          

check_marks(student_1,"Student 1")
check_marks(student_2,"Student 2")                                              

