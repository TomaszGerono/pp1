def f(amount_to_pay):
    coin_values = [5, 2, 1]
    num_coins = 0
    for coin in coin_values:
        num_of_coins = amount_to_pay // coin
        
        amount_to_pay -= num_of_coins * coin
        
    
        num_coins += num_of_coins

    return num_coins


print(f(23))