def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI) and determine the health category.
    """
    try:
        bmi = weight_kg / (height_m ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25.0:
            category = "Normal weight"
        elif 25.0 <= bmi < 30.0:
            category = "Overweight"
        else:
            category = "Obese"
            
        return bmi, category
    except ZeroDivisionError:
        return None, "Height cannot be zero."

# Example usage:
try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters (e.g., 1.75): "))
    
    bmi_value, health_status = calculate_bmi(weight, height)
    
    if bmi_value is not None:
        print(f"\nYour BMI is: {bmi_value:.2f}")
        print(f"Health Category: {health_status}")
    else:
        print(health_status)
except ValueError:
    print("Please enter valid numeric values for weight and height.")
