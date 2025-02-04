#Travel Planner (assignment 1 lab (4))

class TravelPlanner:
    def __init__(self, budget):
        self.budget = budget
        self.travel_plan = {"flights": [], "hotels": [], "activities": []}
        self.available_flights = {'flight1': 200, 'flight2': 350, 'flight3': 500}
        self.available_hotels = {'hotel1': 150, 'hotel2': 250, 'hotel3': 400}
        self.available_activities = {'activity1': 50, 'activity2': 120, 'activity3': 200}

    def display_available_options(self):
        print("\nAvailable options:")
        print("Flights:")
        for idx, (flight, price) in enumerate(self.available_flights.items(), start=1):
            print(f"{idx}. {flight} - ${price}")
        print("Hotels:")
        for idx, (hotel, price) in enumerate(self.available_hotels.items(), start=1):
            print(f"{idx}. {hotel} - ${price}")
        print("Activities:")
        for idx, (activity, price) in enumerate(self.available_activities.items(), start=1):
            print(f"{idx}. {activity} - ${price}")

    def add_to_travel_plan(self, category, option_idx):
        if category == "flight":
            available_options = list(self.available_flights.items())
        elif category == "hotel":
            available_options = list(self.available_hotels.items())
        elif category == "activity":
            available_options = list(self.available_activities.items())
        else:
            print("Invalid category.")
            return
        
        if 1 <= option_idx <= len(available_options):
            selected_option, price = available_options[option_idx - 1]
            if self.budget >= price:
                self.travel_plan[category + "s"].append((selected_option, price))
                self.budget -= price
                print(f"{selected_option} added to your {category}. Remaining budget: ${self.budget}")
            else:
                print(f"Not enough budget for {selected_option}. Remaining budget: ${self.budget}")
        else:
            print("Invalid option index.")

    def view_travel_plan(self):
        print("\nYour travel plan:")
        for category, items in self.travel_plan.items():
            print(f"{category.capitalize()}:")
            if items:
                for item, price in items:
                    print(f"- {item} for ${price}")
            else:
                print("None selected.")
        print(f"Remaining budget: ${self.budget}")

# Create a travel planner instance with an initial budget
budget = float(input("Enter your travel budget: $"))
planner = TravelPlanner(budget)

# Main loop
while True:
    print("\nWhat would you like to do?")
    print("1. Display available options (flights, hotels, activities)")
    print("2. Add option to travel plan")
    print("3. View travel plan")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        planner.display_available_options()
    elif choice == '2':
        category = input("Which category would you like to choose (flight, hotel, activity)? ").lower()
        planner.display_available_options()
        option_idx = int(input(f"Enter the option number to add to {category}: "))
        planner.add_to_travel_plan(category, option_idx)
    elif choice == '3':
        planner.view_travel_plan()
    elif choice == '4':
        print("Thank you for using the travel planner!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
