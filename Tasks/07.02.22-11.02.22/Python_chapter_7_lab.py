# 1.
room_list = []

# 2., 3., 4.
# 0. Room: Bedroom 2
# 1. Room: South Hall
# 2. Room: Dining Room
# 3. Room: Bedroom 1
# 4. Room: North Hall
# 5. Room: Kitchen
room = ['Bedroom 2 (N, E)', 1, 3, None, None]
room_list.append(room)
room = ['South Hall (W, N, E)', 0, 2, 4, None]
room_list.append(room)
room = ['Dining Room (W, N)', 1, 5, None, None]
room_list.append(room)
room = ['Bedroom 1 (E, S)', 0, 4, None, None]
room_list.append(room)
room = ['North Hall (W, E, S)', 1, 3, 5, None]
room_list.append(room)
room = ['Kitchen (W, S)', 2, 4, None, None]
room_list.append(room)

# 5.
current_room = 0

# 6., 7.
print(room_list[0])

# 10.
done = False
while not done:
    # 11.
    print("------------------------")

    # 8., 9.
    print(room_list[current_room][0])

    # 12.
    direction = input("What direction? ")

    # 13.
    if(direction.upper() == "N"):
        # 14.
        next_room = room_list[current_room][1]
        #15.
        if(next_room == None):
            print("You can't go that way.")
        else:
            current_room = next_room
    # 17.
    elif(direction.upper() == "E"):
        # 14.
        next_room = room_list[current_room][2]
        #15.
        if(next_room == None):
            print("You can't go that way.")
        else:
            current_room = next_room
    elif(direction.upper() == "S"):
        # 14.
        next_room = room_list[current_room][3]
        #15.
        if(next_room == None):
            print("You can't go that way.")
        else:
            current_room = next_room
    elif(direction.upper() == "W"):
        # 14.
        next_room = room_list[current_room][4]
        #15.
        if(next_room == None):
            print("You can't go that way.")
        else:
            current_room = next_room
    elif direction.upper() == "Q":
        done = True
    else:
        print("Your Input could not be interpreted!")