a = input("Enter Your Choice Either -Rock,Paper,scissor= ")
b = ['Rock','Paper','sissor']
import random
c = random.choice(b)
print("User Input:",a)
print("Computer Input:",c)
if a==c:
    print("Tie.")
elif a=="Rock" and c=="Scissor":
    print("You Win")
elif a=="Rock" and c=="Paper":
    print("Computer Win")
elif a=="Paper" and c=="Scissor":
    print("Computer win")
elif a=="Paper" and c=="Rock":
    print("You Win")
elif a=="Scissor" and c=="Paper":
    print("You win")
elif a=="Scissor" and c=="Rock":
    print("Computer Win")
else:
    print("Invalid Input")