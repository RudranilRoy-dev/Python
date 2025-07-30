tasks = [("A", 4), ("B", 3), ("C", 5)]
time_slice = 2

while tasks:
    task, time_left = tasks.pop(0)  # First task comes out
    print(f"{task} runs for {min(time_slice, time_left)} mins")

    time_left -= time_slice  # Reduce remaining time

    if time_left > 0:
        tasks.append((task, time_left))  # Still needs time, go to back
    else:
        print(f"{task} is done ✅")
