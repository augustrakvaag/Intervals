import time
import eel

eel.init('web')

filename = "5x5.txt"

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