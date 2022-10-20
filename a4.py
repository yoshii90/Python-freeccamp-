sh = input("Enter Hours:")
sr = input("Enter Rate:")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()
# print(fh, fr)
if fh > 40 :
    print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    oth = (fh - 40)
    print("Regular hours:", fh)
    print("Overtime hours:", oth)
    print("Regular pay:", reg)
    print("Overtime pay:", otp)
    xp = reg + otp
else:
    print("Regular")
    xp = fh * fr
print("Total pay:", xp)
