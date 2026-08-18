# Ask the user for trip details
destination = input("Destination  : ")
days = int(input("Days         : "))
budget = float(input("Budget       : "))
travel_style = input("Travel Style : ")

print('')

hotel_cost = float(input("Hotel Cost          : "))
transportation_cost = float(input("Transportation Cost : "))
food_cost = float(input("Food Cost           : "))
miscellaneous_cost = float(input("Miscellaneous Cost  : "))
total_cost = hotel_cost + transportation_cost + food_cost + miscellaneous_cost

if total_cost > budget :
    print("")
    print("Budget exceeded.")



# # Hard to read
# print(destination)
# print(days)
# print(budget)
# print(travel_style)

# # Readable, labeled
# print(f"Destination : {destination}")
# print(f"Days : {days}")
# print(f"Budget : {budget}")
# print(f"Style : {travel_style}")




def print_trip_summary(destination, days, budget, travel_style):
    print('')
    print("========================" )
    print("KelanaAI" )
    print("========================" )
    print(f"Destination  : {destination}" )
    print(f"Days         : {days}" )
    print(f"Budget       : {budget}" )
    print(f"Travel Style : {travel_style}" )
# Call it with any trip
print_trip_summary(destination, days, budget, travel_style)

