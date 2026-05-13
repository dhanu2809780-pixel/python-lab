name = input("enter the name")
year = int(input("enter year of birth"))
age = 2026 - int(year)
if age >= 60:
    print("He is a senior citizen")
else:
    print("Not a senior citizen")