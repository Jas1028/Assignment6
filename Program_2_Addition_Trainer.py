# # Program 2: Addition Trainer
# # Create a program that automatically generate two random numbers to add (0 to 99)
# # Let the user answer and evaluate if the user has the correct answer
# # The program will ask the user 10 addition operation
# # Display the result summary of the 10 operations (ex 9/10)



# It will generate two random numbers
import random

# In this game, there are 10 levels.
GameLevel = 10
#Your score will increase if you will answer it correctly.
Score = 0



Value1 = random.randint(0,99)
Value2 = random.randint(0,99)

print("Level 1")

Level1 = int(input(f"\nSum of {Value1} and {Value2}.\nEnter your answer: " ))
CorrectAnswer = Value1 + Value2

if CorrectAnswer == Level1:
    print("\nLevel 1 passed. ")
    Score = Score + 1
    print(f"Your current score is {Score}. ")
else:
    CorrectAnswer != Level1
    print("Level 1 failed. ")
    print(f"Your current score is {Score}. ")

Score = Score

Value3 = random.randint(0,99)
Value4 = random.randint(0,99)


print("\n\nLevel 2")

Level2 = int(input(f"\nSum of {Value3} and {Value4}.\nEnter your answer: " ))
CorrectAnswer = Value3 + Value4

if CorrectAnswer == Level2:
    print("\nLevel 2 passed. ")
    Score = Score + 1
    print(f"Your current score is {Score}. ")
else:
    CorrectAnswer != Level2
    print("Level 2 failed. ")
    print(f"Your current score is {Score}. ")
    

