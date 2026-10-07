import json
import os
file_path=os.path.join(os.path.dirname(__file__),"expenses.txt")

with open(file_path, "r") as file:
   data=file.read()


expenses=json.loads(data)
print(expenses)

choice="yes"

while choice=="yes":
    expense_name= input("Enter the expense name:")
    expense_amount=int(input("Enter the amount:"))
    expense_category=input("Enter the category:")

    expense={
        "name":expense_name,
        "amount":expense_amount,
        "category":expense_category
    }
    expenses.append(expense)   
    print(expenses)
    choice=input("Do you want to add another expense?")

total=0
for expense in expenses:
    total=total+expense["amount"]

    print(expense["name"],expense["amount"],expense["category"])


print("Total spending", total)

del_name=input("Enter the expense you want to delete:")

index=0

for expense in expenses:
    if expense["name"]==del_name:
     
     expenses.pop(index)

index =index+1

print(expenses)

with open(file_path, "w") as file:
   file.write(json.dumps(expenses))



