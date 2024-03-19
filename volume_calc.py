length = float(input("length:"))
width  = float(input("width:"))
height = float(input("height:"))

volume = length * width * height

print("Volume: ", volume)

total_length = length + width + height

if total_length <= 80:
    charge = 5000
elif total_length <= 100:
    charge = 8000
elif total_length <= 120:
    charge = 10000
elif total_length <= 160:
    charge = 13000
else:
    charge = "unavailable"

print("Total length: ", total_length)
print("Charge: ",charge)
