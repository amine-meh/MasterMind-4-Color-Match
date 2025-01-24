import random 

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
  code = []
  for _ in range(CODE_LENGTH):
    color = random.choice(COLORS)
    code.append(color)
  return code

def guess_code():
  while True:
    guess = input(f'Enter {CODE_LENGTH} colors from the following list {COLORS}: ').upper().split(" ")
    if len(guess) != CODE_LENGTH:
      print(f'Please enter exactly {CODE_LENGTH} colors.')
      continue
    for color in guess:
      if color not in COLORS:
        print(f'Invalid color: {color}. Please enter colors from the following list {COLORS}.')
        break
      
    else :
      break
  return guess

def check_code(real_code, guess):
  color_count = {}
  correct_pos = 0
  incorrect_pos = 0

  for color in real_code:
    if color not in color_count:
      color_count[color] = 0
    color_count[color] += 1

  for real_color, guess_color in zip(real_code, guess):
    if guess_color == real_color:
      correct_pos += 1
      color_count[guess_color] -= 1
  
  for real_color, guess_color in zip(real_code, guess):
    if guess_color != real_color and guess_color in color_count and color_count[guess_color] > 0:
      incorrect_pos += 1
      color_count[guess_color] -= 1
  
  return correct_pos, incorrect_pos
  
def main():
  print(f"Welcome to mastermind, you have {TRIES} tries to guess the {CODE_LENGTH} color code.")
  print("The valid colors are: ", *COLORS)
  code = generate_code()
  for attempts in range (1, TRIES + 1):
    user_guess = guess_code()
    correct, misplaced = check_code(code, user_guess)
    
    if correct == CODE_LENGTH:
      print(f"Congratulations! You have guessed the code in {attempts} tries.")
      break

    print(f"Correct position: {correct} || Wrong position: {misplaced}")
  else:
    print(f"Sorry! You have run out of tries. The correct code was {code}")

if __name__ == "__main__":
  main()