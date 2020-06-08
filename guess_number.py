num = [1, 11, 12, 23, 33, 34]

while True:
    a = input("Guess a number or type q to quit.")
    if a == 'q':
        break
    try:
        a = int(a)
    except ValueError:
        print("please type a valid number or q to quit.")
    if a in num:
        print("Your guess is correct!")
    else:
        print("You guess is incorrect")
    