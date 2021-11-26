
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


    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   





