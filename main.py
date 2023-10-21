# context manager
with open("mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

# initialization
letters = 0
numbers = 0

for line in data.split("\n"):
    for char in line:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            numbers += 1

print(f"letter count: {letters}")
print(f"Number count: {numbers}")
