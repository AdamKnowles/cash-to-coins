total_amount = 150.29

piggyBank = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0
}

def cash_to_coins(amount):
    quarters = amount // .25
    piggyBank["quarters"] = quarters
    difference = amount - (quarters * .25)

    dimes = difference // .1
    piggyBank["dimes"] = dimes
    difference = difference - (dimes * .1)

    nickels = difference // .05
    piggyBank["nickels"] = nickels
    difference = difference - (nickels * .05)

    pennies = difference // .01
    piggyBank["pennies"] = pennies
    difference = difference - (pennies * .01)

    print(piggyBank)

cash_to_coins(total_amount)