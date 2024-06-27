def bullsCows(secert,guess):
   digitSecert = {}
   digitGuess = {}
   cows = 0
   bulls = 0
   for i in range(4):
    digitSecert[i] = (int(secert) % 10)
    secert = (int(secert) // 10)
    digitGuess[i] = (int(guess) % 10)
    guess = (int(guess) // 10)
   for i in range(4):
    if digitGuess[i]==digitSecert[i]:
      bulls+=1
    elif digitGuess[i] in digitSecert.values():
      cows+=1
   string = str(bulls)+"A"+str(cows)+"B"
   return string 
print(bullsCows("1123","0111"))