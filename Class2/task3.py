age=int(input("enter your age"))
if age >0 and age < 13:
    print("Child")
elif age >=13 and age < 18:
    print("Teenager")
elif age >= 18 and age < 65
    print("Adult")

# def determine_age_group(age):
#     if age < 13:
#         return "Child"
#     elif 13 <= age < 18:
#         return "Teenager"
#     elif 18 <= age < 65:
#         return "Adult"
#     else:
#         return "Elder"

# def main():
#     try:
#         age = int(input("Please enter your age: "))
#         if age < 0:
#             print("Age cannot be negative. Please try again.")
#         else:
#             age_group = determine_age_group(age)
#             print(f"You are categorized as: {age_group}")
#     except ValueError:
#         print("Invalid input. Please enter a valid number for age.")

# if __name__ == "__main__":
#     main()