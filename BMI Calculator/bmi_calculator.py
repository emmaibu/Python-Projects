print('Welcome to The BMI Calculator!')

while True:

    try:        
        weight_kg = -1
        while weight_kg <= 0:
            weight_kg =  float(input('Eneter your weight in kilograms: '))
            if weight_kg <= 0:
                print('Weight must be a positive.')
                
        height_meters = -1
        while height_meters < 0:
            height_meters = float(input('Enter your height in meters: '))
            if height_meters < 0:
                print('Height must be a positive.')
        

        bmi = weight_kg/(height_meters ** 2)
        bmi = round(bmi, 2)
        
       
        if bmi < 18.5:
            category = "underweight"
        elif 18.5 <= bmi <= 24.9:
            category = "optimum range"
        elif 25 <= bmi <= 29.9:
            category = "overweight"
        elif 30 <= bmi <= 34.9:
            category = "Class I obesity"
        elif 35 <= bmi <= 39.9:
            category = "Class II obesity"
        else:
            category = "Class III obesity"


        print(f"\nYour BMI is {bmi}.")
        print(f"You fall into the {category} category.\n")

            
        print('Do you want to calculate another BMI? (yes/no)')
        if not input('> ').lower().startswith('y'):
            break
            
    except ValueError:
        print('Invalid input. Please enter numeric values.')
        
        
print('Goodbye!')
