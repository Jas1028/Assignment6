
# # Print the 4 numbers from highest to lowest using only if-else statement.

# Steps
#Ask the user 4 number

def Ask4Numbers():
    F = float(input("Enter first number: "))
    S = float(input("Enter second number: "))
    T = float(input("Enter third number: "))
    P = float(input("Enter fourth number: "))
    return F, S, T, F

F, S, T, P = Ask4Numbers()

# Arrange from high to lowest
def HighestNumber():
    if F > S and F > T and F > P:
        HighestNum = F
        return HighestNum
    else:
        if S > F and S > T and S > P: 
            HighestNum = S
            return HighestNum
        else:
            if T > F and T > S and T > P:
                HighestNum = T
                return HighestNum
            else:
                if P > F and P > S and P > T:
                    HighestNum = P
                    return HighestNum

Highest = HighestNumber()

def HighNumber():
    if Highest == F:
        if S > T and S > P:
            HighNum = S
            return HighNum
        else:
            if T > S and T > P:
                HighNum = T
                return HighNum
            else:
                if P > S and P > T:
                    HighNum = P 
                    return HighNum
    if Highest == S:
        if F > T and F > P:
            HighNum = F
            return HighNum
        else:
            if T > F and T > P:
                HighNum = T
                return HighNum
            else: 
                if P > F and P > T:
                    HighNum = P
                    return HighNum
    if Highest == T:              
        if F > S and F > P:
            HighNum = F
            return HighNum
        else:
            if S > F and S > P:
                HighNum = S
                return HighNum
            else: 
                if P > F and P > S:
                    HighNum = P
                    return HighNum
    if Highest == P:    
        if F > S and F > T:
            HighNum = F
            return HighNum
        else:
            if S > F and S > T:
                HighNum = T
                return HighNum
            else: 
                if T > F and T > S:
                    HighNum = P
                    return HighNum
                        
High = HighNumber()

def LowNumber():
    if Highest == F:
        if High == S:
            if T > P:
                LowNum = T
                return LowNum
            else:
                if P > T:
                    LowNum = P
                    return LowNum
        if High == T:
            if S > P:
                LowNum = S
                return LowNum
        else:
            if P > S:
                LowNum = P
                return LowNum
        if High == P:
            if S > T:
                LowNum = S
                return LowNum
            else:
                if T > S:
                    LowNum = T
                    return LowNum
    if Highest == S:
        if High == F:
            if T > P:
                LowNum = T
                return LowNum
            else:
                if P > T:
                    LowNum = P
                    return LowNum
        if High == T:
            if F > P:
                LowNum = F
                return LowNum
        else:
            if P > F:
                LowNum = P
                return LowNum
        if High == P:
            if F > T:
                LowNum = F
                return LowNum
            else:
                if T > F:
                    LowNum = T
                    return LowNum
    if Highest == T:
        if High == F:
            if S > P:
                LowNum = S
                return LowNum
            else:
                if P > S:
                    LowNum = P
                    return LowNum
        if High == S:
            if F > P:
                LowNum = F
                return LowNum
        else:
            if P > F:
                LowNum = P
                return LowNum
        if High == P:
            if F > S:
                LowNum = F
                return LowNum
            else:
                if S > F:
                    LowNum = S
                    return LowNum  
    if Highest == P:
        if High == F:
            if S > T:
                LowNum = S
                return LowNum
            else:
                if T > S:
                    LowNum = T
                    return LowNum
        if High == S:
            if F > T:
                LowNum = F
                return LowNum
        else:
            if T > F:
                LowNum = T
                return LowNum
        if High == T:
            if F > S:
                LowNum = F
                return LowNum
            else:
                if S > F:
                    LowNum = S
                    return LowNum                                     
        
        
Low = LowNumber()   
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   





