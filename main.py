import random
from data import*

#compare accounts
def gameselect(data):
    Name = data["name"]
    Description = data["description"]
    Country = data["country"]
    return f"{Name} a {Description} from {Country}"

def followercount(data):
    followercount = int(data["follower_count"])
    return followercount


def higherlowergame():
    #generate random name and account
    account_a = (random.choice(data))
    account_b = (random.choice(data))

    if account_a == account_b:
        account_b = (random.choice(data))

    print(f"{gameselect(account_a)}")
    print("VS")
    print(f"{gameselect(account_b)} ")

    return account_a,account_b


account_a,account_b = higherlowergame()

followercount_A = followercount(account_a)
followercount_B = followercount(account_b)

switchcounter = 0
counter = 0

while (True):
    userI = input("Higher or Lower Select A or B: ").upper()
    if followercount_A >= followercount_B and userI == 'A':
        counter += 1
        print(f"You're right! Current Score: {counter}")
        account_b = (random.choice(data))
        switchcounter +=1
        if (switchcounter >= 2):
            account_a = (random.choice(data))
            switchcounter = 0

        print(f"{gameselect(account_a)} (A)")
        print("VS")
        print(f"{gameselect(account_b)} (B)")
    elif followercount_B >= followercount_A and userI == 'B':
        counter += 1
        print(f"You're right! Current Score: {counter}")
        account_a = (random.choice(data))
        switchcounter +=1
        if (switchcounter >= 2):
            account_a = (random.choice(data))
            switchcounter = 0
        print(f"{gameselect(account_b)} (B)")
        print("VS")
        print(f"{gameselect(account_a)} (A)")
    else:
        print("You've Lost")
        print(f"Final Score: {counter}")
        newgame= input("Would you like to continue 'Y' or 'N': ").lower()
        if newgame == 'n':
            break
        else:
            account_a, account_b = higherlowergame()
            followercount_A = followercount(account_a)
            followercount_B = followercount(account_b)
            switchcounter = 0
            counter = 0






