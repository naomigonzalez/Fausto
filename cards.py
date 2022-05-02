import random 
regresar = True 

score = 300 
while regresar: 
  regresar = False
  card1 = random.randint(1, 13)
  card2 = random.randint(1,13)

  print(f"The card is: {card1} {card2}")
  user_response = input("Higher or lower? [h/l] ") 
  print(f"The card is: {card2}") 

  if card1 > card2:
    correct_response = "l"
  else:
    correct_response = "h" 

  if correct_response == user_response: 
    score += 100
  else:
    score -= 75

  print(f"Your score is: {score}")

  if score >= 0:
    play_again = input("Play again? [y/n] ")
    if play_again == "y":
      regresar = True 

