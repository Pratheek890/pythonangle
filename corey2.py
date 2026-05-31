#conditional statement
# 1
language = "Python"
value = 5
if language == "Java" or language == "Python":
    print("This is it")
    if value <= 10:
        print("YEppp")
else:
    print("Another ")        

# 2 
user_name =  "Speed"
user_id = 2022
if user_name == "Ishoe" and user_id == 2025:
    print("Welcome, Login successful")
elif user_name == "Speed" and user_id == 2022: 
    print("You are in different block")   

else:
    print("Please report to Security \n you are not allowed") 

# 3 
logging_in = True
if not logging_in:
    print("LoooooooooLLLL")
else:
    print("NOOOOOO")   

# 4
print(id(user_id))   

condition = [1,2]

print(condition is True)
