# Ask the user to enter 5 temperatures (one each day), store them in a list using a loop, and print the average temperature.
temperature = []

for i in range (1,6):
    temp = float(input(f"Day {i} temperature (°C): "))
    temperature.append(temp)

average = sum(temperature)/5

print("\nThe average temperature of 5 days:",average,"°C")