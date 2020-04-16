#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # make a loop to find the lowest buying price
  # store the lowest buying and highest selling price in seperate variable as the index
  # make a loop to the find the highest profit price
  # store the max profit in a variable and check if it's the highest
  # buying_index = 0
  # selling_index = buying_index += 1

  current_min_price_so_far = 0
  max_profit_so_far = 0
  
  for price in range(current_min_price_so_far, len(prices)):
    profit = prices[price] - prices[current_min_price_so_far]
   
    if prices[current_min_price_so_far] > prices[price]:
      current_min_price_so_far = price

    if profit > max_profit_so_far:
      max_profit_so_far = profit
    elif profit < max_profit_so_far and max_profit_so_far == 0:
      max_profit_so_far = profit 

  return max_profit_so_far
    
    


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))