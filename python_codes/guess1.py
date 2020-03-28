secret_word = "mertoe"
guess_count = 0
guess_limit = 3
out_of_guesses = False
guess = ""

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter my nicknane: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Looser")
else:
    print("Correct")
