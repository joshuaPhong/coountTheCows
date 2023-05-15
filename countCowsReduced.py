print("\033[33mLet's count the cows!")
total_cows = 0

while True:
    row = int(input("\033[36mHow many cups are left hanging?\n"))
    cows_in_row = 36 - row
    total_cows += cows_in_row
    print(f"There are {cows_in_row} cows in this row, and {total_cows} cows in total.")
    if input("Do you want to add another row? (y/n)\n").lower() == "n":
        break

print(f"There are {total_cows} cows in total.")
