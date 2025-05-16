#a function that takes 1 number as argument
#Return "FizzBuzz" → if the number is divisible by both 3 and 5
#Return "Fizz" → if it's divisible by 3 only
#Return "Buzz" → if it's divisible by 5 only
#Otherwise, return "Not a Fizz-buzz number"

def Fizz_Buzz(number):
    if number % 3==0 and number % 5==0:
        return"FizzBuzz" 
    elif number % 3==0:
        return"Fizz"
    elif number % 5==0:
        return"Buzz"
    else:
        return "Not a Fizz-buzz number"
    
number=int(input("Enter a Number:"))
result=Fizz_Buzz(number)
print(result)
    
        
    