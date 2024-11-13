# Convert a given number of seconds to hours, minutes and seconds

total_seconds = input("Please type the number of seconds: \n")
hours = int(total_seconds) // 3600
minutes = (int(total_seconds) % 3600) // 60
seconds = int (total_seconds) % 60
print (f"The duration is: {hours} hours, {minutes} minutes and {seconds} seconds.")