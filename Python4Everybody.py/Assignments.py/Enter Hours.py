sd = input("Enter Hours: ")
ls = input("Enter Rate: ")
try:
    gg = float(sd)
    ts = float(ls)
except: 
    print("Error, please enter numeric input")
quit()
print(gg, ts)
if gg > 40:
    reg = ts * gg
    otp = (gg - 40.0) * (ts * 0.5)
    xp = ref + otp
else:
    xp = gg * ts
print("Pay:",xp)
    