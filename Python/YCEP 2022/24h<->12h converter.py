hh12 = int
hh24 = int
mm = int
ss = int

time12 = (f"{hh12}:{mm}:{ss}")
time24 = (f"{hh24}:{mm}:{ss}")

def convertTo24(hh12):
    hh24 = hh12 + 12
    print(time24)

def convertTo12(hh24):
    if hh24 > 12:
        hh12 = hh24 - 12
        print(time12)
    else:
        print(time24)


timeFormat = str(input("Choose time format to input: \n1) 12h\n2) 24h\nOption: "))

if timeFormat == "1":
    print("12 hour format has been selected.")
    hh12 = int(input("Input hour: "))
    if hh12 >= 12: 
        print("Time format must be 12 hours!")
    mm = int(input("Input hour (Type 00 if you don't wish to type in minutes): "))
    ss = int(input("Input seconds (Type 00 if you don't wish to type in seconds): "))
    convertTo24(hh12)
elif timeFormat == "2":
    print("24 hour format has been selected.")
    hh24 = int(input("Input hour: "))
    mm = int(input("Input hour (Type 00 if you don't wish to type in minutes): "))
    ss = int(input("Input seconds (Type 00 if you don't wish to type in seconds): "))
    convertTo12(hh24)
else:
    print("?!?!@#)!_*#!")