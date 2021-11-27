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


#Program will ask the user 10 addition operation and user will answer it.
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
    print("\nLevel 1 failed. ")
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
    print("\nLevel 2 failed. ")
    print(f"Your current score is {Score}. ")
    
Score = Score

Value5 = random.randint(0,99)
Value6 = random.randint(0,99)


print("\n\nLevel 3")

Level3 = int(input(f"\nSum of {Value5} and {Value6}.\nEnter your answer: " ))
CorrectAnswer = Value5 + Value6

if CorrectAnswer == Level3:
    print("\nLevel 3 passed. ")
    Score = Score + 1
    print(f"Your current score is {Score}. ")
else:
    CorrectAnswer != Level3
    print("\nLevel 3 failed. ")
    print(f"Your current score is {Score}. ")

Score = Score

Value7 = random.randint(0,99)
Value8 = random.randint(0,99)


print("\n\nLevel 4 ")

Level4 = int(input(f"\nSum of {Value7} and {Value8}.\nEnter your answer: " ))
CorrectAnswer = Value7 + Value8

if CorrectAnswer == Level4:
    print("\nLevel 4 passed. ")
    Score = Score + 1
    print(f"Your current score is {Score}. ")
else:
    CorrectAnswer != Level4
    print("\nLevel 4 failed. ")
    print(f"Your current score is {Score}. ")

Score = Score

Value9 = random.randint(0,99)
Value10 = random.randint(0,99)


print("\n\nLevel 5 ")

Level5 = int(input(f"\nSum of {Value9} and {Value10}.\nEnter your answer: " ))
CorrectAnswer = Value9 + Value10

if CorrectAnswer == Level5:
    print("\nLevel 5 passed. ")
    Score = Score + 1
    print(f"Your current score is {Score}. ")
else:
    CorrectAnswer != Level5
    print("\nLevel 5 failed. ")
    print(f"Your current score is {Score}. ")

Score = Score

Value11 = random.randint(0,99)
Value12 = random.randint(0,99)


print("\n\nLevel 6 ")

Level6 = int(input(f"\nSum of {Value11} and {Value12}.\nEnter your answer: " ))
CorrectAnswer = Value11 + Value12

if CorrectAnswer == Level6:
    print("\nLevel 6 passed. ")
    Score = Score + 1
    print(f"Your current score is {Score}. ")
else:
    CorrectAnswer != Level6
    print("\nLevel 6 failed. ")
    print(f"Your current score is {Score}. ")

Score = Score

Value13 = random.randint(0,99)
Value14 = random.randint(0,99)


print("\n\nLevel 7 ")

Level7 = int(input(f"\nSum of {Value13} and {Value14}.\nEnter your answer: " ))
CorrectAnswer = Value13 + Value14

if CorrectAnswer == Level7:
    print("\nLevel 7 passed. ")
    Score = Score + 1
    print(f"Your current score is {Score}. ")
else:
    CorrectAnswer != Level7
    print("\nLevel 7 failed. ")
    print(f"Your current score is {Score}. ")

Score = Score

Value15 = random.randint(0,99)
Value16 = random.randint(0,99)


print("\n\nLevel 8 ")

Level8 = int(input(f"\nSum of {Value15} and {Value16}.\nEnter your answer: " ))
CorrectAnswer = Value15 + Value16

if CorrectAnswer == Level8:
    print("\nLevel 8 passed. ")
    Score = Score + 1
    print(f"Your current score is {Score}. ")
else:
    CorrectAnswer != Level8
    print("\nLevel 8 failed. ")
    print(f"Your current score is {Score}. ")

Score = Score

Value17 = random.randint(0,99)
Value18 = random.randint(0,99)


print("\n\nLevel 9 ")

Level9 = int(input(f"\nSum of {Value17} and {Value18}.\nEnter your answer: " ))
CorrectAnswer = Value17 + Value18

if CorrectAnswer == Level9:
    print("\nLevel 9 passed. ")
    Score = Score + 1
    print(f"Your current score is {Score}. ")
else:
    CorrectAnswer != Level9
    print("\nLevel 9 failed. ")
    print(f"Your current score is {Score}. ")

Score = Score

Value19 = random.randint(0,99)
Value20 = random.randint(0,99)


print("\n\nLevel 10 ")

Level10 = int(input(f"\nSum of {Value19} and {Value20}.\nEnter your answer: " ))
CorrectAnswer = Value19 + Value20

if CorrectAnswer == Level10:
    print("\nLevel 10 passed. ")
    Score = Score + 1
    print(f"Your current score is {Score}. ")
else:
    CorrectAnswer != Level10
    print("\nLevel 10 failed. ")
    print(f"Your current score is {Score}. ")

Score = Score
print("\nYour score will release in:")
import time
seconds = int(3)
for i in range(seconds):
    print(str(seconds - i ) +  " second(s). ")
    time.sleep(1)

if Score >= 5:
    print(f"\nCongrats, you passed the evaluation.\nYour score is {Score}/{GameLevel}.") 
else:
    if Score < 5:
        print(f"\nAww, you need to practice more to ehnace your skills in math.\nYour score is {Score}/{GameLevel}. ")

