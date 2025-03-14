# Your Student ID: 240543604
# Your Name and Surname: Aylin-P-Saatlou

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
