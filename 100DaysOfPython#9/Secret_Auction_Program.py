import os
import Secret_Auction_Program_art

def add(user_name, user_bid):
    user_dict = {"name":user_name,"bid":user_bid}
    auction_list.append(user_dict)

user_dict = {}
auction_list = []
reply = "yes"
highest = 0
final_bid_list = []

print(Secret_Auction_Program_art.logo)
print("Welcome to secret auction program.")
while (reply == "yes"):
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    add(user_name,user_bid)
    reply = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if (reply == "yes"):
        os.system('clear')
    else:
        for dict in auction_list:
            final_bid_list.append(dict["bid"])
            highest = max(final_bid_list)
        for key,value in dict.items():
            if value == highest:
                winner = dict["name"]
        print("The winner is '{0}'!!! Congratulations!".format(winner))