age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
    has_ticket = input("Do you have a valid ticket? (yes/no): ")
    if has_ticket.lower() =="yes":
        print("You can watch the movie.")
    else:
        print("you cannot watch the movie without a valid ticket.")
else:
    print("you arenot allowed to watch a movie")
