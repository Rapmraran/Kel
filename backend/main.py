from services.trip_service import (
    recommended_places, 
    trip_category,
    transportation,
    calculate_daily_budget, 
    get_trip_category, 
    get_travel_season, 
    recommended_transportation
)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.trip import Trip
from database import SessionLocal, init_db


class TripRequest(BaseModel):
    destination: str
    days: int
    budget: float
    travel_style: str

# FastAPI validates the JSON body against this model
# If a field is missing or wrong type, it returns 422 automatically

app = FastAPI()

init_db()

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
@app.post("/api/v1/trips2")
def create_trip2(request: TripRequest):
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
    


# DB Get
@app.get( "/api/v1/trips")
def list_trips():
    db = SessionLocal()
    trips = db.query(Trip).all()
    db.close()
    return trips

@app.get( "/api/v1/trips/{trip_id}")
def get_trip(trip_id: int):
    db = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    db.close()
    # handling not found
    if trip is None:
        raise HTTPException(status_code=404, detail=f"Trip with id {trip_id} not found")
    return trip


# DB Post
@app.post("/api/v1/trips")
def create_trip(request: TripRequest):
    # reuse Session 2 business logic
    daily_budget = calculate_daily_budget(
        request.budget, request.days
    )
    category = get_trip_category(
        request.budget
    )
    # create a Trip ORM object
    trip = Trip(
        destination = request.destination,
        days = request.days,
        budget = request.budget,
        category = category,
        daily_budget = daily_budget,
    )
    # save to PostgreSQL
    db = SessionLocal()
    db.add(trip)
    db.commit()
    db.refresh(trip) # get the auto-generated id
    db.close()
    return trip


# DB Put
@app.put("/api/v1/trips/{trip_id}")
def update_trip(trip_id: int, request: TripRequest):
    db = SessionLocal() # Open database connection
    
    # Find the data first
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    
    # If not found, return a 404 error
    if trip is None:
        db.close()
        raise HTTPException(status_code=404, detail=f"Trip with id {trip_id} not found")
        
    # Recalculate daily budget and category
    new_daily_budget = calculate_daily_budget(request.budget, request.days)
    new_category = get_trip_category(request.budget)
    
    # Overwrite old database data with new data from the request
    trip.destination = request.destination
    trip.days = request.days
    trip.budget = request.budget
    trip.daily_budget = new_daily_budget
    trip.category = new_category
    
    # Save permanent changes
    db.commit()
    db.refresh(trip) # Get the latest version
    db.close()       # Close connection
    
    return trip


# DB Delete
@app.delete("/api/v1/trips/{trip_id}")
def delete_trip(trip_id: int):
    db = SessionLocal()
    
    # Find the data first
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    
    # If data is not found, return a 404 error
    if trip is None:
        db.close()
        raise HTTPException(status_code=404, detail=f"Trip with id {trip_id} not found")
        
    # If found, delete the data
    db.delete(trip)
    db.commit() # Save permanent changes
    db.close()  # Close connection
    
    return {"message": f"Trip {trip_id} has been deleted successfully"}







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