from my_function import list_dir
from my_function import update_app

print("Enter any choice: ")
print("1. List all directories.")
print("2. Update App")

option = int(input())
if(option == 1):
    first()
elif(option == 2):
    update_app()
else:
    print("invalid entry")
