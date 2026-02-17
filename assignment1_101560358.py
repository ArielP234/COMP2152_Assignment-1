"""
Author: Ariel Pokutinsky
Assignment: #1
"""

# Step b: Create 4 variables (with data type comments)
gym_member = "Eric Ben Haim"        # str
preferred_weight_kg = 20.5          # float
highest_reps = 25                   # int
membership_active = True            # bool

# Step c: Create a dictionary named workout_stats (dict data type)
# Keys: friend names (str), Values: tuple (yoga, running, weightlifting)
workout_stats = {
    "Alex": (30, 45, 20),
    "Raz": (40, 35, 50),
    "Taylor": (25, 30, 60),
    "Amir": (50, 40, 45)
}

# Step d: Calculate total workout minutes and add new key-value pairs
for friend, minutes in list(workout_stats.items()):
    total = sum(minutes)
    workout_stats[f"{friend}_Total"] = total

# Step e: Create a 2D nested list called workout_list (list of lists)
# Each row = a friend, each column = activity (yoga, running, weightlifting)
workout_list = [list(minutes) for minutes in workout_stats.values() if isinstance(minutes, tuple)]

# Step f: Slice the workout_list
# Extract and print yoga and running minutes for all friends
yoga_running = [row[:2] for row in workout_list]
print("Yoga and Running minutes for all friends:", yoga_running)

# Extract and print weightlifting minutes for the last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for last two friends:", weightlifting_last_two)

# Step g: Use an if-statement within a loop to check totals >= 120
for key, value in workout_stats.items():
    if key.endswith("_Total") and value >= 120:
        friend_name = key.replace("_Total", "")
        print(f"Great job staying active, {friend_name}!")

# Step h: Allow user input to look up a friend's name
search_name = input("Enter a friend's name to look up their workout stats: ")

if search_name in workout_stats and isinstance(workout_stats[search_name], tuple):
    minutes = workout_stats[search_name]
    total = workout_stats.get(f"{search_name}_Total", sum(minutes))

    print(f"{search_name}'s workout minutes:")
    print(f"Yoga: {minutes[0]}")
    print(f"Running: {minutes[1]}")
    print(f"Weightlifting: {minutes[2]}")
    print(f"Total workout minutes: {total}")
else:
    print(f"Friend {search_name} not found in the records.")

# Step i: Print friend with highest and lowest total workout minutes
totals = {k.replace("_Total", ""): v for k, v in workout_stats.items() if k.endswith("_Total")}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("Friend with the highest total workout minutes:", highest_friend)
print("Friend with the lowest total workout minutes:", lowest_friend)
