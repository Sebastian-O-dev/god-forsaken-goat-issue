import random

attempt_number = 0
car_counter_switch = 0
car_counter_no_switch = 0
goat_counter_switch = 0
goat_counter_no_switch = 0
attempt_iteration = range(6000)

while True:
    # BASE VALUES
    doors = ["1", "2", "3"]
    options = ["goat", "goat", "car"]
    assigned_doors = []
    switch_y_n = ["y", "n"]

    for door in doors:
        random_option = random.choice(options)
        assigned_doors.append([door, random_option])
        options.remove(random_option)

    merged_assigned_doors = [f"Door {door}: {random_option}" for door, random_option in assigned_doors]

    # player_choice = int(input(f"Pick a door: 1, 2 or 3... => "))
    # DOOR RANDOMISATION CHOICE
    if 0 <= attempt_number < 1000 or 3000 <= attempt_number < 4000:
        player_choice = 1
    elif 1000 <= attempt_number < 2000 or 4000 <= attempt_number < 5000:
        player_choice = 2
    elif 2000 <= attempt_number < 3000 or 5000 <= attempt_number <= 6000:
        player_choice = 3

    player_pick = merged_assigned_doors[player_choice - 1]
    merged_assigned_doors.remove(player_pick)
    for element in merged_assigned_doors:
        if "goat" in element:
            host_pick = element
            merged_assigned_doors.remove(host_pick)
            break
    left_door = merged_assigned_doors[0]
    merged_assigned_doors.remove(left_door)

    # print(f"\nPlayer pick: {player_pick}")
    # print(f"\nHost picks => {host_pick}")

    while True:

        # switch = input("\nDo you want to switch your pick to the leftover door? (y/n) => ")
        # SIMULATION BLOCK
        for attempt in attempt_iteration:
            if attempt_number < 3000:
                switch = "y"
                attempt_number += 1
                break
            else:
                switch = "n"
                attempt_number += 1
                break

        # SWITCH BLOCK
        if switch not in switch_y_n:
            # print("\nNot a valid answer")
            continue
        elif switch == "y":
            temp = player_pick
            player_pick = left_door
            left_door = temp
            break
        else:
            break

    # PLAYER PICK REVEAL + PRIZE TALLY
    # print(f"\nPlayer pick: {player_pick}")
    if "car" in player_pick and switch == "y":
        car_counter_switch += 1
    elif "car" in player_pick and switch == "n":
        car_counter_no_switch += 1
    elif "goat" in player_pick and switch == "y":
        goat_counter_switch += 1
    elif "goat" in player_pick and switch == "n":
        goat_counter_no_switch += 1

    if 0 <= attempt_number < 6000:
        continue
    else:
        break

print(f"CAR won SWITCH: {str(car_counter_switch)}")
print(f"CAR won NO SWITCH: {str(car_counter_no_switch)}")
print(f"GOAT won SWITCH: {str(goat_counter_switch)}")
print(f"GOAT won NO SWITCH: {str(goat_counter_no_switch)}")

car_percentage_win_switch = car_counter_switch/6000 * 100
print(f"CAR percentage win SWITCH: {car_percentage_win_switch:.2f}")

car_percentage_win_no_switch = car_counter_no_switch/6000 * 100
print(f"CAR percentage win NO SWITCH: {car_percentage_win_no_switch:.2f}")

# print(f"#Door left over/player optional switch: {left_door}")
