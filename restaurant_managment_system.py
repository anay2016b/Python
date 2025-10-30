from tkinter import *
from tkinter import messagebox, ttk

class RestaurantManagementSystem:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        
        self.menu.items = {
            "Chicken Burger": 4.99,
            "Veg Burger": 5.99,
            "Fish Burger": 6.99,
            "Beef Burger": 7.99,
            "Fries": 2.49,
            "Onion Rings": 2.99,
            "Coke": 1.49,
            "Sprite": 1.99,
            "Water": 1.99,
            "Apple pie": 2.99,
         }
        self.exchange_rate1 = 0.66  # Example exchange rate to EUR
        self.exchange_rate2 = 0.58  # Example exchange rate to GBP
        self.exchange_rate3 = 0.77  # Example exchange rate to USD
        self.exchange_rate4 = 119  # Example exchange rate to JPY
        self.exchange_rate5 = 68.25  # Example exchange rate to INR