data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]

# Create a new list with only integer values
cleaned_list=[item for item in data_list if type(item)==int]

print("data_list",data_list)
print("cleaned_list",cleaned_list)