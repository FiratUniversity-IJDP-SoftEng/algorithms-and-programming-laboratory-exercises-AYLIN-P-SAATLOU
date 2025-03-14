# Your Student ID: 240543604
# Your Name and Surname: Aylin-P-Saatlou

user_input = input("Enter a string: ")

char_frequency = {}
for char in user_input:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

sorted_frequency = dict(sorted(char_frequency.items()))

print("Character frequencies: ")
for char, count in sorted_frequency.items():
    print(f"{char}: {count}")
