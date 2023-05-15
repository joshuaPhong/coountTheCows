print("\033[33mLets count the cows!")
print("Each row has thirty six cups. Lets count row by row")
total_cows = 0
while True:
    row = input("\033[36mTell me how many cups are left hanging?\n")
    print(f"there are {row} cups left hanging")
    cows_in_row = 36-int(row)
    print(f"There are {cows_in_row} cows in this row")
    total_cows += cows_in_row
    print(f"There are {total_cows} in total")
    finish = input("Do you want to add another row? Y/n\n")
    if finish.lower() == "n":
        break
    print("Lets add the next row.")
print(f"There are {total_cows} cows in total")