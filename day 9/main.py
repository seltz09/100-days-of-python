from art import logo

print(logo)
print("Welcome to the Secret auction program.")

data_dict = {}


name = input("What is your name?: ")
bid = int(input("What is your Bid?: "))
data_dict[name] = bid

y_or_n = input("Are there any other Bidders? Type 'yes' or 'no': ").lower()


while y_or_n != "no":
    print("\n" * 100)
    name = input("What is your name?: ")
    bid = int(input("What is your Bid?: "))
    data_dict[name] = bid
    y_or_n = input("Are there any other Bidders? Type 'yes' or 'no': ").lower()


def find_highest_bidder(bidding_dictionary):
    winner = ''
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f'The winner is {winner} with a bid of ${highest_bid}')

find_highest_bidder(data_dict)