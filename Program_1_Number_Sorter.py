
# # Print the 4 numbers from highest to lowest using only if-else statement.

# Steps
#Ask the user 4 number

def Ask4Numbers():
    F = float(input("Enter first number: "))
    S = float(input("Enter second number: "))
    T = float(input("Enter third number: "))
    P = float(input("Enter fourth number: "))
    return F, S, T, P

F, S, T, P = Ask4Numbers()

# Arrange from high to lowest
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
                HighNum = T
            else: 
                if T > F and T > S:
                    HighNum = P
        return HighNum
                        
High = HighNumber()



def DisplayOutput():
    print(f"Highest number is {Highest}. ")
    print(f"Second to the highest number is {High}. ")
    # print(f"Third to the highest number is {Low}. ")
    # print(f"Lowest number is {Lowest}. ")

DisplayOutput()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   





