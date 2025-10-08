#Name:Shourya Awasthi
#Date: 08/10/2025
# Daily Calorie RECORDER
# WELCOME MESSAGE
print("WELCOME TO DAILY CALORIE TRACKER")
print("THIS PROGRAM IS DESIGNED TO CALCULATE TOTAL CALORIES COMPARE WITH YOUR DAILY LIMIT, AND OPTIONALLY SAVE YOUR SESSION")
# INPUT OF MEALS AND CALORIES
ITEM = []
Calorie_amount = []
NO_OF_MEALS = int(input("How many meals did you have today ?  "))
for i in range(NO_OF_MEALS):
    print(f"\nEnter details for meal {i + 1}:")
    name_of_meals = str(input("Meal name which you have today : "))
    calorie_amount = float(input("Calories  in meal which you have today (in kcal): "))
    ITEM.append(name_of_meals)
    Calorie_amount.append(calorie_amount)
#  Calorie Calculation
total_no_of_calories = sum(Calorie_amount)
average_calories = total_no_of_calories / len(Calorie_amount)
daily_limit_of_calories = float(input("\nEnter your daily calorie limit: "))
 # Task 4: Exceed Limit Warning System
if total_no_of_calories > daily_limit_of_calories:
    Alert_message = " You have exceeded your daily calorie limit! "
else:
    Alert_message = " You are within your daily calorie limit. "
# Formatted Output
print("\n\n----------- DAILY SUMMARY REPORT -----------\n")
print("Meal Name\t\tCalories")
print("--------------------------------------------")

for i in range(len(ITEM)):
    print(f"{ITEM[i]}\t\t{Calorie_amount[i]}")

print("--------------------------------------------")
print(f"Total:\t\t\t{total_no_of_calories}")
print(f"Average:\t\t{average_calories:}")
print(f"Status:\t\t\t{Alert_message}")
print("\n--------------------------------------------")