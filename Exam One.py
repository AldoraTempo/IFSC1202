import random

# Scores for both players
hs = 0
cs = 0
print("Winners and Losers - Human is Even Computer is Odd")
    
# Prompt human 1 for a number between 1 and 5
hc = int(input("Enter your guess: "))
while hc < 1 or hc > 5:
hc = int(input("Invalid number. Please enter a number between 1 and 5: "))

# Game loop for 5 rounds
for round in range(5):
# Human 2 (computer) generates a random number between 1 and 5
cc = random.randint(1, 5)
print(f"Round {round + 1}: Computer chooses {cc}")

# Calculate the sum of both choices
total = hc + cc
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
print(f"Human 1: {human1_score} points")
print(f"Human 2: {human2_score} points")

if hs > cs:
  print("Human Wins!")
else:
  print("Computer Wins!")
