list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]
#using set funtion,"Common:", set1 & set2
                   #"Uncommon:", set1 ^ set2
                   #union: set1 | set2
                   #difference = set1 - set2
# Find common items using set intersection and took it in to a list
common_items= list(set(list1) & set(list2))

# Calculate the sum of common items

sum_common=sum(common_items)
print("List1:",list1)
print("List2:",list2)
print("Common items:", common_items)
print("Sum of common items:", sum_common)