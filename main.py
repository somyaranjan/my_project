from secrets import choice


from my_function import first

print("Enter any choice: ")
choice = int(input())
if(choice == 1):
    first()
else:
    print("other")
