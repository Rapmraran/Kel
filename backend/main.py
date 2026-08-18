from services.trip_service import (
    recommended_places, 
    trip_category,
    transportation,
    calculate_daily_budget, 
    get_trip_category, 
    get_travel_season, 
    recommended_transportation
)
from fastapi import FastAPI
from pydantic import BaseModel


class TripRequest(BaseModel):
    destination: str
    days: int
    budget: float
    travel_style: str

# FastAPI validates the JSON body against this model
# If a field is missing or wrong type, it returns 422 automatically



app = FastAPI()


# a GET endpoint at the root path
@app.get("/")
def home():
    return {
        "message" : "Welcome to KelanaAI"
    }

@app.get("/health")
def health():
    return {
        "status" : "OK"
    }
    
@app.get("/api/v1/trip-categories")
def get_trip_categories():
    list_category = trip_category
    return list_category

@app.get("/api/v1/recommendations")
def get_recomendation_places():
    list_place = recommended_places
    return list_place

@app.get("/api/v1/transportations")
def get_transportations():
    list_transport = transportation
    return list_transport
    


# POST endpoint — receives JSON, returns JSON
@app.post("/api/v1/trips")
def create_trip(request: TripRequest):
    daily_budget = calculate_daily_budget(
        request.budget, request.days
    )
    category = get_trip_category(
        request.budget
    )
    recommendation_transport = recommended_transportation(
        category
    )
    return {
        "destination" : request.destination,
        "budget" : request.budget,
        "daily_budget" : daily_budget,
        "category" : category,
        "recommendation_transport" : recommendation_transport
    }









# Initialize empty list for inputs
list_destination = []

# Ask the user for trip details
destination = input("Destination  : ")
days = int(input("Days         : "))
budget = float(input("Budget       : "))
travel_style = input("Travel Style : ")
travel_month = input("Travel Month : ")

# Split input string into a list and remove unnecessary spaces
for place in destination.split(','):
    list_destination.append(place.strip().title())

print('')

hotel_cost = float(input("Hotel Cost          : "))
transportation_cost = float(input("Transportation Cost : "))
food_cost = float(input("Food Cost           : "))
miscellaneous_cost = float(input("Miscellaneous Cost  : "))
total_cost = hotel_cost + transportation_cost + food_cost + miscellaneous_cost

if total_cost > budget :
    print("")
    print("Budget exceeded.")


def print_trip_summary(
    list_destination, 
    days, 
    budget, 
    travel_style, 
    travel_month,
    category,
    daily,
    season,
    transportation
):
    
    print('')
    print("========================" )
    print("KelanaAI" )
    print("========================" )
    print(f"Destination                :", end=" " )
    
    # Check if the list contains only one item
    if len(list_destination) == 1:
        print(list_destination[0])
    # If there is more than one item, use enumerated numbering
    else:
        for number, place in enumerate(list_destination, start=1):
            print(f"{number}. {place}", end=" ")
        print('')

    print(f"Days                       : {days}" )
    print(f"Budget                     : {budget}" )
    print(f"Travel Style               : {travel_style}" )
    print(f"Travel Month               : {travel_month}" )
    print(f"\nCategory                   : {category}")
    print(f"Daily Budget               : {daily} USD/day")
    print(f"\nSeason Category            : {season}")
    print(f"Recommended Transportation : {transportation}\n")
    # print(f"\nCategory : {category} · Daily Budget : {daily} USD/day")
    
category = get_trip_category(budget)
daily = calculate_daily_budget(budget, days)
season = get_travel_season(travel_month)
recomendation_transport = recommended_transportation(category)

# Call it with any trip
print_trip_summary(
    list_destination, 
    days, 
    budget, 
    travel_style, 
    travel_month,
    category,
    daily,
    season,
    recomendation_transport
)


# Loop through the list
print('Recommended Places :')
for place in recommended_places :
    print(f" - {place}")