
numDays = int(input("How many day's temperature?"))
temps = []
for i in range(1, numDays+1):
    nextDay = int(input("Day " + str(i) + " 's high temp: "))
    temps.append(nextDay)

avg = round(sum(temps)/len(temps), 2)
print("Average = " + str(avg))

above = 0
for i in temps:
    if i > avg:
        above += 1

print(f"{above} day(s) above average")
