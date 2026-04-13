def calculate_restaurant_bill(meal_cost) :
    Service_Charge = meal_cost * 0.10
    Amount_After_Service = meal_cost + Service_Charge
    Tax = Amount_After_Service * 0.05
    Tip = Amount_After_Service * 0.05
    Total_Bill = meal_cost + Service_Charge + Tax + Tip
    print(f"Meal Cost: {meal_cost} \n Service Charge: {Service_Charge} \n Tax: {Tax} \n Tip: {Tip} \n Total Bill: {Total_Bill}")



Meal_Cost = float(input("Please enter the meal cost:"))
calculate_restaurant_bill(Meal_Cost)
    