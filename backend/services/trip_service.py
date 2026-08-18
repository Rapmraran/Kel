# A list holds multiple values
recommended_places = [
    "Tokyo Tower",
    "Shibuya",
    "Mount Fuji"
]

def get_trip_category(budget):
    # Translate business rules into code
    if budget < 1000:
        category = "Backpacker"
    elif budget <= 3000:
        category = "Standard"
    else:
        category = "Luxury"
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
    if category == "Backpacker":
        transportation = "Bus"
    elif category == "Standard":
        transportation = "Train"
    elif category == "Luxury":
        transportation = "Flight"
    return transportation