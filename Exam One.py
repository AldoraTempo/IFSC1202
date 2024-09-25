import random

# Scores for both players
hs = 0
cs = 0
rounds = 5
print("Winners and Losers - Human is Even Computer is Odd")
print("You have 5 rounds to play. Guess a number between 1 and 5.")

# Game loop for 5 rounds
for round in range(1, 6):
  print(round)
  if round == 6:
      break
# Prompt human 1 for a number between 1 and 5
  hg = int(input("Enter your guess: "))
  while hg < 1 or hg > 5:
    hg = int(input("Invalid number. Please enter a number between 1 and 5: "))

# Human 2 (computer) generates a random number between 1 and 5
  cg = random.randint(1, 5)
  print(f"Round {round}: Computer chooses {cg}")

# Calculate the sum of both choices
  total = hg + cg
  print(f"Total of both picks is: {total}")

# Determine the winner of this round
  if total % 2 == 0:  # Even
    hs += 1
    print("Human Wins this round!")
  else:  # Odd
    cs += 1
    print("Computer wins this round!")

# Final results
print("\nFinal Scores:")
print(f"Human: {hs} points")
print(f"Computer: {cs} points")

if hs > cs:
  print("Human Wins!")
else:
  print("Computer Wins!")