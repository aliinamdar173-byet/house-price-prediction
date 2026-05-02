# House Price Prediction
# Author: Inamdar Mohammad Ali

# Simple linear regression from scratch (no external libraries needed)
# Predicts house price based on area, bedrooms, and location score

def mean(values):
    return sum(values) / len(values)

def predict_price(area, bedrooms, location_score, age):
    """
    Simple weighted formula simulating a trained regression model.
    Weights derived from a sample Mumbai housing dataset.
    """
    base_price = 500000  # base price in INR

    area_weight      = 4500    # per sq ft
    bedroom_weight   = 75000   # per bedroom
    location_weight  = 120000  # per location score point (1-10)
    age_penalty      = 8000    # per year of age

    price = (base_price
             + (area * area_weight)
             + (bedrooms * bedroom_weight)
             + (location_score * location_weight)
             - (age * age_penalty))

    return max(price, 300000)  # minimum price floor

def get_location_score():
    locations = {
        "1": ("Bandra / Juhu / Marine Lines", 9),
        "2": ("Andheri / Byculla / Dadar", 7),
        "3": ("Thane / Kurla / Ghatkopar", 5),
        "4": ("Navi Mumbai / Mira Road", 4),
        "5": ("Outskirts / Rural", 2),
    }
    print("\nSelect location area:")
    for key, (name, score) in locations.items():
        print(f"  {key}. {name} (Score: {score}/10)")
    choice = input("Enter choice (1-5): ").strip()
    if choice in locations:
        name, score = locations[choice]
        return name, score
    else:
        print("Invalid choice. Defaulting to Andheri/Byculla.")
        return "Andheri / Byculla / Dadar", 7

def format_price(price):
    if price >= 10000000:
        return f"₹{price/10000000:.2f} Crore"
    elif price >= 100000:
        return f"₹{price/100000:.2f} Lakh"
    else:
        return f"₹{price:,.0f}"

def main():
    print("=" * 48)
    print("       HOUSE PRICE PREDICTION TOOL")
    print("       (Mumbai Region Estimator)")
    print("=" * 48)

    try:
        area = float(input("\nEnter house area (in sq ft): "))
        bedrooms = int(input("Enter number of bedrooms: "))
        location_name, location_score = get_location_score()
        age = int(input("Enter age of property (in years): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    predicted = predict_price(area, bedrooms, location_score, age)
    low  = predicted * 0.90
    high = predicted * 1.10

    print("\n" + "=" * 48)
    print("         PREDICTION RESULT")
    print("=" * 48)
    print(f"  Area             : {area} sq ft")
    print(f"  Bedrooms         : {bedrooms} BHK")
    print(f"  Location         : {location_name}")
    print(f"  Property Age     : {age} years")
    print("-" * 48)
    print(f"  Estimated Price  : {format_price(predicted)}")
    print(f"  Price Range      : {format_price(low)} – {format_price(high)}")
    print("=" * 48)
    print("  Note: Estimate based on weighted regression model.")

if __name__ == "__main__":
    main()
