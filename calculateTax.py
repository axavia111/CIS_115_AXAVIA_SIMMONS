#This program calculates the sale tax of an item

item_price = 75.34
tax = .0725

sales_tax = item_price * tax

total_cost = item_price + sales_tax

print(f'The item cost is: ${item_price}')
print(f'The sales tax is: ${sales_tax:,.2f}')
print(f'The total cost is: ${total_cost:,.2f}')