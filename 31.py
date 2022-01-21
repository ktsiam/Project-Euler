import functools
     
@functools.lru_cache(maxsize=None)  # functools.cache
def coin_sum(n, coins=(200,100,50,20,10,5,2,1)):
    c_sum = 0
    for i, coin in enumerate(coins):
        if coin > n:
            continue
        c_sum += 1 if coin == n else coin_sum(n-coin, coins[i:])
    return c_sum

print(coin_sum(200)) # $2
print(coin_sum(10000)) # $100
