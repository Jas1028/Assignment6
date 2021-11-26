# Print the 4 numbers from highest to lowest using only if-else statement.

# Steps
#Ask the user 4 number

def Ask4Numbers():
    F = float(input("Enter first number: "))
    S = float(input("Enter second number: "))
    T = float(input("Enter third number: "))
    P = float(input("Enter fourth number: "))
    return F, S, T, P

F, S, T, P = Ask4Numbers()

# Arrange from highest to lowest
def HighestNumber():
    if F > S and F > T and F > P:
        HighestNum = F
    else:
        if S > F and S > T and S > P: 
            HighestNum = S
        else:
            if T > F and T > S and T > P:
                HighestNum = T
            else:
                HighestNum = P
    return HighestNum

Highest = HighestNumber()

def HighNumber():
    if Highest == F:
        if S > T and S > P:
            HighNum = S
        else:
            if T > S and T > P:
                HighNum = T
            else:
                if P > S and P > T:
                    HighNum = P 
        return HighNum
    elif Highest == S:
        if F > T and F > P:
            HighNum = F
        else:
            if T > F and T > P:
                HighNum = T
            else: 
                if P > F and P > T:
                    HighNum = P
        return HighNum
    elif Highest == T:              
        if F > S and F > P:
            HighNum = F
        else:
            if S > F and S > P:
                HighNum = S
            else: 
                if P > F and P > S:
                    HighNum = P
        return HighNum
    elif Highest == P:    
        if F > S and F > T:
            HighNum = F
        else:
            if S > F and S > T:
                HighNum = S
            else: 
                if T > F and T > S:
                    HighNum = T
        return HighNum
                        
High = HighNumber()

def LowNumber():
    if Highest == F and High == S:
        if T > P:
            LowNum = T
        else:
            if P > T:
                LowNum = P
        return LowNum
    elif Highest == F and High == T:
        if S > P:
            LowNum = S
        else:
            if P > S:
                LowNum = P
        return LowNum
    elif Highest == F and High == P:
        if S > T:
            LowNum = S
        else:
            if T > S:
                LowNum = T
        return LowNum
    elif Highest == S and High == F:
        if T > P:
            LowNum = T
        else:
            if P > T:
                LowNum = P
        return LowNum
    elif Highest == S and High == T:
        if F > P:
            LowNum = F
        else:
            if P > F:
                LowNum = P
        return LowNum
    elif Highest == S and High == P:
        if F > T:
            LowNum = F
        else:
            if T > F:
                LowNum = T
        return LowNum
    elif Highest == T and High == F:
        if S > P:
            LowNum = S
        else:
            if P > S:
                LowNum = P
        return LowNum
    elif Highest == T and High == S:
        if F > P:
            LowNum = F
        else:
            if P > F:
                LowNum = P
        return LowNum
    elif Highest == T and High == P:
        if F > S:
            LowNum = F
        else:
            if S > F:
                LowNum = S
        return LowNum  
    elif Highest == P and High == F:
        if S > T:
            LowNum = S
        else:
            if T > S:
                LowNum = T
        return LowNum
    elif Highest == P and High == S:
        if F > T:
            LowNum = F
        else:
            if T > F:
                LowNum = T
        return LowNum
    elif Highest == P and High == T:
        if F > S:
            LowNum = F
        else:
            if S > F:
                LowNum = S
        return LowNum                                     
        
        
Low = LowNumber()   

def LowestNumber():
    if Highest == F and High == S:
        if Low == T:
            LowestNum = P
        else: 
            LowestNum = T
        return LowestNum
    elif Highest == F and High == T:
        if Low == S:
            LowestNum = P
        else:
            LowestNum = S
        return LowestNum
    elif Highest == F and High == P:
        if Low == S:
            LowestNum = T
        else:
            LowestNum = S
        return LowestNum
    elif Highest == S and High == F:
        if Low == T:
            LowestNum = P
        else: 
            LowestNum = T
        return LowestNum
    elif Highest == S and High == T:
        if Low == F:
            LowestNum = P
        else:
            LowestNum = F
        return LowestNum
    elif Highest == S and High == P:
        if Low == F:
            LowestNum = T
        else:
            LowestNum = F
        return LowestNum    
    elif Highest == T and High == F:
        if Low == S:
            LowestNum = P
        else: 
            LowestNum = S
        return LowestNum
    elif Highest == T and High == S:
        if Low == F:
            LowestNum = P
        else:
            LowestNum = F
        return LowestNum
    elif Highest == T and High == P:
        if Low == F:
            LowestNum = S
        else:
            LowestNum = F
        return LowestNum
    if Highest == P and High == F:
        if Low == S:
            LowestNum = T
        else: 
            LowestNum = S
        return LowestNum
    if Highest == P and High == S:
        if Low == F:
            LowestNum = T
        else:
            LowestNum = F
        return LowestNum
    elif Highest == P and High == T:
        if Low == F:
            LowestNum = S
        else:
            LowestNum = F
        return LowestNum                   
                   

Lowest = LowestNumber()

# Display the output
def DisplayOutput():
    print(f"Highest number is {Highest}. ")
    print(f"Second to the highest number is {High}. ")
    print(f"Third to the highest number is {Low}. ")
    print(f"Lowest number is {Lowest}. ")
    print(f"In order: {Highest}, {High}, {Low}, {Lowest}. ")

DisplayOutput()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   





