row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
tresure_map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
print("Where do you want to put the tresure???: ")
location = list(input())
location = list(map(int,location))
tresure_map[location[1]-1][location[0]-1] = "X"
print(f"{row1}\n{row2}\n{row3}")

