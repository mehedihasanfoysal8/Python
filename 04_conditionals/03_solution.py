score = int(input("Enter your score : "))


if score >= 101:
    print("Please verify your grade: ")
    exit()


if score > 90 and score < 100:
    print("You have grade A")

elif score > 80 and score < 89:
    print("You have grade B")

elif score > 70 and score < 79:
    print("You have grade C")

elif score > 60 and score < 69:
    print("You have grade D")

else:
    print("You gave grade F")