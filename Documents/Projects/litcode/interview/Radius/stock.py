prices = [7,1,5,3,6,4]

total_max_profit = 0

j = 0

for i in range(0, len(prices)-1):
    curr = prices[i]
    print("i", i)

    temp_max_profit = 0
    hey = i+1
    for j in range(hey, len(prices)):
        today = prices[j]
        if today - curr > 0:
            temp_max_profit += today-curr
            curr = prices[j+1]
            j +=1
    if temp_max_profit > total_max_profit:
        total_max_profit = temp_max_profit
