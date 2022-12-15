#AMELIORABLE

i = 0
while i < 3 :
    nombre = float(input("Choose a number between 1 and 3."))
    if nombre < 1 or nombre > 3:
        print("That's not between 1 and 3.")
    else :
        print("Thank you.")

i = i + 1
