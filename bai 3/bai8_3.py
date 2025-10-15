import math

pos = [0, 0]

while True:
    s = input("Nhập di chuyển enter để dừng: ")
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0].upper()
    steps = int(movement[1])

    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps

distance = math.sqrt(pos[0]**2 + pos[1]**2)
print("Khoảng cách là:", round(distance))
