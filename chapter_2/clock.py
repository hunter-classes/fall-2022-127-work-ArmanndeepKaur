hour = input("What's the time now? (in hours) ")
alarm = input("How many hours until the alarm goes off? ")

hour = int(hour)
alarm = int(alarm)

alarmTime = hour + alarm

print(alarmTime % 24)
