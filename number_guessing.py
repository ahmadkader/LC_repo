import random
number = random.randint(1, 100)
score = 0
win = False
while win==False:
   guess_the_number = input("enter a number between 1 and 100: ")
   score += 1
   if number == int(guess_the_number):
     print("You guessed it right! congrats")
     print('number of attempts i.e. score', score)
     win == True
     break
   else: 
      if number > int(guess_the_number):
       print("Your guess is too low")
      else:
        print('your guess is too high')
        
       

        

  