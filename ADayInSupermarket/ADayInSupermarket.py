#Fruits Prices
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
#Fruits in Stock
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

total = 0
#Print Fruits, Prices, Stock
for key in prices:
    print (key)
    print ("price: %s" % prices[key])
    print ("stock: %s" % stock[key])
#Total Value of inventory
    value = prices[key] * stock[key]
    print (value)
    total += value
print (total)



    