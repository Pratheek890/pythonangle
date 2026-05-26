# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
customer_name = str(input("Enter the customer's name: "))
number_of_passes = int(input("Enter the number of passes bought: "))
token_per_pass = 100
price_per_pass = 50
token_required_per_game = 10
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
total_tokens = number_of_passes * token_per_pass
total_cost = number_of_passes * price_per_pass
games_available = total_tokens // token_required_per_game
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available
print(customer_name , number_of_passes , total_tokens, total_cost , games_available)