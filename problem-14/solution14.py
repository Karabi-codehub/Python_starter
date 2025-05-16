list_1 = [4, 9, 8, 7, 5, 2, 13]

#at first we sorted it and then descending the list
sorted_list=sorted(list_1,reverse=True)

max_value=sorted_list[0] # The first item in the list = biggest number (because it's sorted descending)
min_value=sorted_list[-1] # The last item in the list = smallest number
#Positive indices start at 0 from the left (start) of the list.
#Negative indices start at -1 from the right (end) of the list.

difference = max_value - min_value

print("📋 Original List:", list_1)
print("⬇️ Sorted (Descending):", sorted_list)
print(f"🔢 Max: {max_value}, Min: {min_value}")
# f ->Tells Python to evaluate inside {}
#It tells Python:"Hey, this string might have variables inside {} — so replace them with their real values!"
                 # It means:You can put a variable or a calculation inside {}, and Python will replace it with the actual result.
#example:name = "Alice".print("Hello, {name}").Output:Hello, {name}   ❌ (doesn't work as expected)
         #name = "Alice".print(f"Hello, {name}"). output:Hello, Alice 

print(f"➖ Subtraction: {difference}")