hours = 36
minutes = 99
second = 160

while second > 60:
    second -= 60
    minutes += 1
    
print(minutes)

while minutes > 60:
    minutes -= 60
    hours += 1

print(hours, minutes, second)