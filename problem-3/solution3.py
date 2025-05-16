def find_elder_brother(age1,age2):
    if age1 > age2:
        return("The 1st brother is elder.")
    elif age1 < age2:
        return("The 2nd brother is elder.")
    else:
        return("Both brothers are of the same age.")
age1=int(input("Enter the age of Brother 1:"))
age2=int(input("Enter the age of Brother 2:"))
result=find_elder_brother(age1,age2)
print(result)