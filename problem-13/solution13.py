dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

# Print the original dictionaries
print("\n📘 Original Dictionaries:")
print("dict1 =", dict1)
print("dict2 =", dict2)
print("\n")

# Find common keys using set intersection
Common_keys= set(dict1.keys()) & set(dict2.keys())

print("🔁 Common keys with their values from both dictionaries:")
# Display values for each common key
for key in Common_keys:
    print(f"{key}:dict1={dict1[key]},dict2={dict2[key]}")
    

