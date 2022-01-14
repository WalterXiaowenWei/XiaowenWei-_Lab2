#1) Take a variable with distance in kilometres as input and output the same distance converted to miles.

x = 1 
while x > 0:
    x += 1
    input_kilometres = int(input("please input the distance in kilometres: "))
    input_miles = input_kilometres * 0.621371
    print("Your input kilometres is equal to ", input_miles, "miles")
    
        
