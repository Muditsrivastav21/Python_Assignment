"""Q2.You are a sports coach and you have the heights of your players in centimeters. The heights are stored in a list. Your task is to write a Python program to calculate 
the average height and find out how many players are taller than the average."""

height_list = [155, 167, 180, 169, 173, 158, 188, 190, 176]
count = 0

for height in height_list:
    if len(height_list) > 0:
        count += 1

total_height = 0
for i in range(0, count):
    total_height += height_list[i]

average_height = float(total_height / count)
print(f"The average height is: {average_height:.2f}")

taller_count = 0
for height in height_list:
    if height > average_height:
        taller_count += 1

print(f"Number of players taller than the average height: {taller_count}")
