#Step 1: Hotel cost!
def hotel_cost(nights):
    return 140 * nights
#Step 2: Flight cost!
def plane_ride_cost(city):
    if city == "Charlotte" :
        return 183
    elif city == "Tampa" :
        return 220
    elif city == "Pittsburgh" :
        return 222
    elif city == "Los Angeles" :
        return 475
#Step 3: Rental car cost!        
def rental_car_cost(days):
    rent = 40 * days
    if days >= 7:
        rent -= 50
    elif days >= 3:
        rent -= 20
    return rent
#Step 4: Total cost of trip!!
def trip_cost(city, days, spending_money):
    sum = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + (spending_money)
    return sum
print (trip_cost("Los Angeles", 5, 600))