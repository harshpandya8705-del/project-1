# ===== PERSONAL DATA COLLECTOR =====
# simple project based on fundamental concepts

print("Welcome to the Personal Data Collector!\n")

# ---- taking input from user ----
name = input("Enter your name: ")
age = int(input("Enter your age: "))   # type casting
height = float(input("Enter your height (in meters): "))
fav_number = int(input("Enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

# ---- using string methods ----
name = name.title()   # capitalize name

# ---- display data ----
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Favourite Number:", fav_number)

# ---- using operators + conditional statements ----
birth_year = 2025 - age   # simple calculation

# condition to check adult or minor
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# another condition example
if fav_number % 2 == 0:
    number_type = "Even"
else:
    number_type = "Odd"

# ---- output results ----
print("\n--- Analysis ---")
print("You are an", status)
print("Your favourite number is", number_type)
print("Your birth year is approximately:", birth_year)

# ---- string formatting ----
message = "Hello " + name + ", you are " + str(age) + " years old."
print("\n" + message)

# ---- final message ----
print("\nThank you for using the program. Goodbye!")
