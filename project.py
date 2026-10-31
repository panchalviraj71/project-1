print("=======================================================")
print("wlecome to the Interactive personal data collector!")
print("=======================================================")

name = input("Enter your Name:")
age = int(input("Enter your age:"))
height = float(input("Enter your height in meters:"))
fav_number = int(input("Enter your Favourite number:"))


current_year = 2026
birth_year = current_year - age
height_meters = height * 100

print("=======================================================")
print("Thank you! Here is the information we collected:")
print("=======================================================")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Height in cm: {height_meters}")
print(f"Favourite Number: {fav_number}")
print(f"Approximate Birth Year: {birth_year}")


print(f"name {name}, Type: {type(name)}, Memory Address: {id(name)}")
print(f"age {age}, Type: {type(age)}, Memory Address: {id(age)}")
print(f"height {height}, Type: {type(height)}, Memory Address: {id(height)}")
print(f"fav_number {fav_number}, Type: {type(fav_number)}, Memory Address: {id(fav_number)}")
print(f"birth_year {birth_year}, Type: {type(birth_year)}, Memory Address: {id(birth_year)}")
print(f"height_meters {height_meters}, Type: {type(height_meters)}, Memory Address: {id(height_meters)}")
