
intro = """
__        __   _                            _          
\\ \\      / /__| | ___ ___  _ __ ___   ___  | |_ ___    
 \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\   
  \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |  
   \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/   

       🎉 Welcome to the Age-Based Party 🎉
"""
print(intro.strip())


# User interaction ka weeyaan qaybtani
user_age = int(input("Enter your age please:\n"))

if user_age < 18:
    user_guardian = input("Are you with a guardian? (yes/no)\n").lower()
    if user_guardian == "yes":
        user_ticket = input("Do you want to buy a ticket? (yes/no)\n").lower()
        if user_ticket == "yes":
            print("✅ You and your guardian are welcome. Enjoy the party!")
        else:
            print("❌ No ticket, no entry.")
    else:
        print("❌ You are not allowed to enter the party without a guardian.")

elif 18 <= user_age < 30:
    user_ticket = input("You are allowed to enter. Do you want to buy a ticket? (yes/no)\n").lower()
    if user_ticket == "yes":
        print("✅ You have bought a ticket. Enjoy the party!")
    else:
        print("❌ No ticket, no entry.")

else:
    print("❌ You're over 30. This party is for under-30s only.")
