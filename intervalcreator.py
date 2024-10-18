import eel
import os

eel.init('web')

filename = "3x12.txt"

@eel.expose
def get_all_intervals():
    return os.listdir("sessions")


@eel.expose
def create_intervals():
    interval_set = []
    with open("sessions/" + filename, 'r') as file:
        for index,line in enumerate(file):
            if index == 0:
                title = line.strip()
            else:
                line = line.strip()
                duration_power = line.split(",")
                interval_set.append(duration_power)
    return [title,interval_set]

eel.start('index.html')