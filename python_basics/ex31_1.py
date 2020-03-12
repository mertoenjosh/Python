print('''You are on a cliff with your friend,
suddenly your friend slips but manage to hold on to something at the end of the cliff
what do you do?..
*1* Pull her up
*2* Walk away
''')

decision = input('> ')

if decision == '1':
    print("""As you are pulling her the cliff start cracking...what do you do
    *1* Leave her hanging
    *2* Stay with her""")

    dilema = input('> ')

    if dilema == '1':
        print("""She cries for you not to leave and tells you that she is afraid to die alone... What do you do?
        *1* Run without looking back
        *2* Stay and die together
        """)

        final = input("> ")

        if final == '1':
            print("Dude!!! was she even your friend...????")
        elif final == '2':
            print("WTF.. Bro you nuts or what??")
        else:
            print("I said follow instructions bruh..")

    elif dilema == '2':
        print("""She begs you to leave and hands you a letter...
        *1* Take the letter read it and leave.
        *2* Take the letter light it and stay.
        """)

        final2 = input('> ')
        if final2 == '1':
            print("Sorry for your loss bruh.")
        elif final2 == '2':
            print("Bro you really loved her man... but you stupid.")
        else:
            print("I said follow instructions bruh..")

    else:
        print("Dude whats up with you and instructions..")

elif decision == '2':
    print("How dare you walk away on your friend man...??")

else:
    print("wise man but I only gave you two choices.")
