from collections import Counter 
rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!. python code easily, explain code easily.'
# Count all characters
char_count = Counter(rhyme)
#find most common charactrt

most_common_char=char_count.most_common(1)[0] #Index 0: the character (e.g., ' ' for space)
                                              #Index 1: the frequency (e.g., 15 times)
# Check if the character is a space
if most_common_char[0]==' ':
    char_name="space"
else:
    char_name=most_common_char[0] #most_common_char[0] → ' ' → the character itself
print("Rhyme:",rhyme)
print("Most Common Character:",char_name) 
print("Frequency",most_common_char[1]) #most_common_char[1] → 15 → how many times it appears


