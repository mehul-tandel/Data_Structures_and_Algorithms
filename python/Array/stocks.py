# Buy and sell stocks only for once for maximum profit

def buy_sell_stock_once(prices):

    min_price_so_far = float('inf')
    max_profit = 0.0

    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit  


# Buy and sell stocks atmost twice for maximum profit

def buy_sell_stocks_twice(prices):
    


# Buy and sell stocks for maximum profit

def buy_sell_stocks(prices):

    n = len(prices)
    i = 0
    while i < n-1 :
        while (i < n-1) and (prices[i+1] <= prices[i]):
            i += 1
          
        if i == n-1:
            break
        
        buy = i
        print('buy=',buy)
        i += 1
      
        while(i < n) and (prices[i] >= prices[i-1]):
            i += 1
          
        sell = i-1
        print('sell=',sell)
        
#test code
price = [100, 180, 260, 310, 40, 535, 695]
buy_sell_stocks(price)