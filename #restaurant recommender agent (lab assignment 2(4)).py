#restaurant recommender agent (lab assignment 2(4))

class RestaurantRecommender:
    def __init__(self, user_prefs):
        self.user_prefs = user_prefs
        self.restaurants = [
            {"name": "Pasta Palace", "cuisine": "Italian", "distance": 2, "rating": 4.5, "price": 3},
            {"name": "Sushi Spot", "cuisine": "Japanese", "distance": 5, "rating": 4.8, "price": 4},
            {"name": "Curry House", "cuisine": "Indian", "distance": 3, "rating": 4.2, "price": 2},
            {"name": "Burger Barn", "cuisine": "American", "distance": 1, "rating": 4.0, "price": 1}
        ]

    def calculate_utility(self, restaurant):
        """Calculate utility score based on user preferences and restaurant attributes."""
        utility = (
            self.user_prefs["rating"] * restaurant["rating"] -  
            self.user_prefs["distance"] * restaurant["distance"] - 
            self.user_prefs["price"] * restaurant["price"] + 
            (self.user_prefs["preferred_cuisine"] == restaurant["cuisine"]) * 5  
        )
        return utility

    def recommend_restaurant(self):
        """Find the restaurant with the highest utility score."""
        best_restaurant = None
        max_utility = float("-inf")

        for restaurant in self.restaurants:
            utility = self.calculate_utility(restaurant)
            if utility > max_utility:
                max_utility = utility
                best_restaurant = restaurant

        return best_restaurant

user_preferences = {
    "rating": 0.6,  
    "distance": 0.2, 
    "price": 0.2,     
    "preferred_cuisine": "Italian" 
}

restaurant_agent = RestaurantRecommender(user_preferences)

recommended_restaurant = restaurant_agent.recommend_restaurant()

print("Recommended Restaurant:", recommended_restaurant["name"])
