from replit import clear
bids = {}

bidding_finished = False


def find_highest_bidder(bidding_record):
    # bidding_records = {"Sveta": 100, "Vik": 200}
    heights_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > heights_bid:
            heights_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a heights bid {heights_bid}")


while not bidding_finished:
    name = input("enter a name: ")
    price = int(input("enter a bid: $"))
    bids[name] = price
    # print(bids)
    should_continue = input("Are there are any bidders? 'yes' or 'no'")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()























