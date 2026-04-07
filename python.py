name = input("Enter Name: ")
birth_year = int(input("Enter Year of Birth: "))

current_year = 2026

age = current_year - birth_year

print("\nName:", name)
print("Age:", age)

if age >= 60:
    print("Senior Citizen")
else:
    print("Not a Senior Citizen")