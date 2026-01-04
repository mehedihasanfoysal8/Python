weather = input("Enter weather Activity : ")

if weather != "Sunny" and weather != "Rainy" and weather != "Snowy":
    print("Please provide valid weather activity")
    exit()

if weather == "Sunny":
    print("Go for a walk")

elif weather == "Rainy":
    print("Read a book")

elif weather == "Snowy":
    print("Build a snowman")
