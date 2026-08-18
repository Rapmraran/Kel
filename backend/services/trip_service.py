# A list holds multiple values
recommended_places = [
    "Tokyo Tower",
    "Shibuya",
    "Mount Fuji"
]

trip_category = [
    "Backpacker",
    "Standard",
    "Luxury"
]

transportation = [
    "Bus",
    "Train",
    "Flight"
]

def get_trip_category(budget):
    # Translate business rules into code
    if budget < 1000:
        category = trip_category[0]
    elif budget <= 3000:
        category = trip_category[1]
    else:
        category = trip_category[2]
    return category


def calculate_daily_budget(budget, days):
    # Arithmetic operators: + - * / //
    daily_budget = budget/days
    return daily_budget


def get_travel_season(travel_month):
    if travel_month == "December":
        season = "Peak Season"
    elif travel_month == "June":
        season = "Holiday Season"
    else:
        season = "Regular Season"
    return season

def recommended_transportation(category):
    if category == trip_category[0]:
        recommendation_transport = transportation[0]
    elif category == trip_category[1]:
        recommendation_transport = transportation[1]
    elif category == trip_category[2]:
        recommendation_transport = transportation[2]
    return recommendation_transport