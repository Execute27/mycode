#!usr/bin/env python3

# Range (99, 0(means 99 to 0) (-1)) count down. 

for num_bottles in range(99, 0, -1):
    print(f"{num_bottles} bottles of beer on the wall!, {num_bottles} bottles of beer! You take one down, pass it around!")
    if num_bottles - 1 > 0:
        print(f"{num_bottles - 1} bottles of beer on the wall!")
    else:
        print("No more bottles of beer on the wall!")
    print()

