import time

age=int(input("Enter your age: "))
salary=int(input("Enter your salary(Per Month) please: " ))
expenses=int(input("Enter your expenses per month:" ))
expected_retire=int(input("When do you wish to retire? "))
time.sleep(2)
print("Your savings are " + str((expected_retire-age)*12*(salary-expenses)) + "!")