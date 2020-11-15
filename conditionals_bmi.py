print("This program calculate the BMI of a person")

user_height = float( input("Please type your height in meters:(ex:1.70m)"))
user_weight = float( input("Please type your weight in kg: (ex:65.5)"))

BMI = user_weight/(user_height*user_height)

print("Your BMI is:",round(BMI,2))
      
if(BMI <= 18.5):
   classification = "Underweight"
   
elif(BMI > 18.5 and BMI<= 24.9):
     classification = "Normal weight"
    
elif(BMI > 24.9 and BMI <= 29.9):
     classification = "Overweight"
    
else:
    classification = "Obesity"
    
print("Your classification is", classification) 
    
