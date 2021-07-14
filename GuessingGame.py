""" Ch3: The Guessing Game
"""
from random import randint
def input_integer(prompt):
	while True: # While not zero and not null
		try:
			inp = input(prompt) # Take the input and store it
			i = int(inp) # Make it an integer
			return i # Return the integer
		except Exception:
			print(inp, "is not a valid integer") # Exception


n = randint(1, 21	)
guess = input_integer("Make a guess> ")
while guess != n: # As long as the input is not n
	if guess > n:
		print("Too high")
	else:
		print("Too low")
	guess = input_integer("Make a guess> ") # Update new input
print("You got it!") # Final execution


# Having the computer guess starting from 1
def input_selection(prompt, options):
	modified_prompt = "{} [{}]: ".format(
		prompt.strip(), ", ".join(options)
	)
	while True:
		inp = input(modified_prompt)
		if inp in options:
			return inp
		print("Invalid choice! Must be in [{}]".format(
			", ".join(options)
			))


for guess in range(1, 21):
	result = input_selection(
		"How is my guess {}".format(guess),
		["low", "hit", "high"]
	)
	if result == "hit":
		print("Wuhuu!")
		break
	else:
		print("I must have been too low, right?", result)

# Starting from 20 going down one step each time!
for guess in range(1, 21)[::-1]:
	result = input_selection(
		"How is my guess {}".format(guess),
		["low", "hit", "high"]
	)
	if result == "hit":
		print("Wuhuu!")
		break
	else:
		print("I must have been too high, right?", result)

# Guessing in the middle!
low_lim = 1
high_lim = 21

while guess != "hit":
	midpoint = low_lim + (high_lim - low_lim) // 2
	guess = midpoint

	result = input_selection(
		"How is my guess: {}".format(guess),
		["low", "hit", "high"]
	)

	if result == "high": 
	# If 10 is too high, we want to set the max to 10
		high_lim = midpoint

	# If 10 is too low, we want to set the max to 10
	elif result == "low":
		low_lim = midpoint

	elif result == "hit":
		print("Wuhuu!")
		break
