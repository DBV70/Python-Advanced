from collections import deque

def time_to_seconds(time_str):
    parts = list(map(int, time_str.split(':')))
    return parts[0] * 3600 + parts[1] * 60 + parts[2]

def seconds_to_time(seconds):
    seconds %= 24 * 3600
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

robots_data = input().split(';')
robots = []
for r in robots_data:
    name, process_time = r.split('-')
    robots.append({'name': name, 'time': int(process_time), 'free_at': 0})

start_time = time_to_seconds(input())
products = deque()

while True:
    line = input()
    if line == "End":
        break
    products.append(line)

current_time = start_time
while products:
    current_time += 1
    current_product = products.popleft()

    robot_found = False
    for robot in robots:
        if robot['free_at'] <= current_time:
            robot['free_at'] = current_time + robot['time']
            print(f"{robot['name']} - {current_product} [{seconds_to_time(current_time)}]")
            robot_found = True
            break

    if not robot_found:
        products.append(current_product)