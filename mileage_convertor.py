print("How many km did you run today?")
kms = input()


conversion_factor = 1.60934
miles = float(kms) / conversion_factor

print(f"You ran {round(miles, 2)} miles.")