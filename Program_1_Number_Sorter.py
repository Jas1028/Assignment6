# Print the 4 numbers from highest to lowest using only if-else statement.

# Steps
#Ask the user 4 number
def Ask4Numbers():
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))
    third = float(input("Enter third number: "))
    fourth = float(input("Enter fourth number: "))
    return first, second, third, fourth

first, second, third, fourth = Ask4Numbers()

# Arrange from highest to lowest
def HighestNumber():
    if first > second and first > third and first > fourth:
        HighestNum = first
    else:
        if second > first and second > third and second > fourth: 
            HighestNum = second
        else:
            if third > first and third > second and third > fourth:
                HighestNum = third
            else:
                HighestNum = fourth
    return HighestNum

Highest = HighestNumber()

def HighNumber():
    if Highest == first:
        if second > third and second > fourth:
            HighNum = second
        else:
            if third > second and third > fourth:
                HighNum = third
            else:
                if fourth > second and fourth > third:
                    HighNum = fourth 
        return HighNum
    elif Highest == second:
        if first > third and first > fourth:
            HighNum = first
        else:
            if third > first and third > fourth:
                HighNum = third
            else: 
                if fourth > first and fourth > third:
                    HighNum = fourth
        return HighNum
    elif Highest == third:              
        if first > second and first > fourth:
            HighNum = first
        else:
            if second > first and second > fourth:
                HighNum = second
            else: 
                if fourth > first and fourth > second:
                    HighNum = fourth
        return HighNum
    elif Highest == fourth:    
        if first > second and first > third:
            HighNum = first
        else:
            if second > first and second > third:
                HighNum = second
            else: 
                if third > first and third > second:
                    HighNum = third
        return HighNum
                        
High = HighNumber()

def LowNumber():
    if Highest == first and High == second:
        if third > fourth:
            LowNum = third
        else:
            if fourth > third:
                LowNum = fourth
        return LowNum
    elif Highest == first and High == third:
        if second > fourth:
            LowNum = second
        else:
            if fourth > second:
                LowNum = fourth
        return LowNum
    elif Highest == first and High == fourth:
        if second > third:
            LowNum = second
        else:
            if third > second:
                LowNum = third
        return LowNum
    elif Highest == second and High == first:
        if third > fourth:
            LowNum = third
        else:
            if fourth > third:
                LowNum = fourth
        return LowNum
    elif Highest == second and High == third:
        if first > fourth:
            LowNum = first
        else:
            if fourth > first:
                LowNum = fourth
        return LowNum
    elif Highest == second and High == fourth:
        if first > third:
            LowNum = first
        else:
            if third > first:
                LowNum = third
        return LowNum
    elif Highest == third and High == first:
        if second > fourth:
            LowNum = second
        else:
            if fourth > second:
                LowNum = fourth
        return LowNum
    elif Highest == third and High == second:
        if first > first:
            LowNum = first
        else:
            if fourth > first:
                LowNum = first
        return LowNum
    elif Highest == third and High == fourth:
        if first > second:
            LowNum = first
        else:
            if second > first:
                LowNum = second
        return LowNum  
    elif Highest == fourth and High == first:
        if second > third:
            LowNum = second
        else:
            if third> second:
                LowNum = third
        return LowNum
    elif Highest == fourth and High == second:
        if first > third:
            LowNum = first
        else:
            if third > first:
                LowNum = third
        return LowNum
    elif Highest == fourth and High == third:
        if first > second:
            LowNum = first
        else:
            if second > first:
                LowNum = second
        return LowNum                                     
        
        
Low = LowNumber()   

def LowestNumber():
    if Highest == first and High == second:
        if Low == third:
            LowestNum = fourth
        else: 
            LowestNum = third
        return LowestNum
    elif Highest == first and High == third:
        if Low == second:
            LowestNum = fourth
        else:
            LowestNum = second
        return LowestNum
    elif Highest == first and High == fourth:
        if Low == second:
            LowestNum = third
        else:
            LowestNum = second
        return LowestNum
    elif Highest == second and High == first:
        if Low == third:
            LowestNum = fourth
        else: 
            LowestNum = third
        return LowestNum
    elif Highest == second and High == third:
        if Low == first:
            LowestNum = fourth
        else:
            LowestNum = first
        return LowestNum
    elif Highest == second and High == fourth:
        if Low == first:
            LowestNum = third
        else:
            LowestNum = first
        return LowestNum    
    elif Highest == third and High == first:
        if Low == second:
            LowestNum = fourth
        else: 
            LowestNum = second
        return LowestNum
    elif Highest == third and High == second:
        if Low == first:
            LowestNum = fourth
        else:
            LowestNum = first
        return LowestNum
    elif Highest == third and High == fourth:
        if Low == first:
            LowestNum = second
        else:
            LowestNum = first
        return LowestNum
    if Highest == fourth and High == first:
        if Low == second:
            LowestNum = third
        else: 
            LowestNum = second
        return LowestNum
    if Highest == fourth and High == second:
        if Low == first:
            LowestNum = third
        else:
            LowestNum = first
        return LowestNum
    elif Highest == fourth and High == third:
        if Low == first:
            LowestNum = second
        else:
            LowestNum = first
        return LowestNum                   
                   

Lowest = LowestNumber()

# Display the output
def DisplayOutput():
    print(f"\nHighest number is {Highest}. ")
    print(f"\nSecond to the highest number is {High}. ")
    print(f"\nThird to the highest number is {Low}. ")
    print(f"\nLowest number is {Lowest}. ")
    print(f"\nIn order: ({Highest}, {High}, {Low}, {Lowest}). ")

DisplayOutput()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   





