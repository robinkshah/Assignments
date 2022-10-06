seconds = float(input("Enter time in seconds= "))
if seconds >= 60 and seconds < 3600:
    m = int(seconds // 60)
    s = int(seconds % 60)
elif seconds >= 3600 and seconds < 86400:
    h = int(seconds // 3600)
    m = int(( seconds % 3600 ) // 60)
    s = int(( seconds % 3600 ) % 60)
elif seconds >= 86400:
    d = int(seconds // 86400)
    h = int((seconds % 86400) // 3600)
    m = int(((seconds % 86400) % 3600) // 60)
    s = int(((seconds % 86400) % 3600) % 60)
elif seconds < 60:
    s = int(seconds)
else:
    exit()
#print
if seconds >= 60 and seconds < 3600:
    print(f"The time is:\t{m} min(s) and {s} sec(s)")
elif seconds >= 3600 and seconds < 86400:
    print(f"The time is:\t{h} hour(s), {m} min(s) and {s} sec(s)")
elif seconds >= 86400:
    print(f"The time is:\t{d} day(s), {h} hour(s), {m} min(s) and {s} sec(s)")
elif seconds < 60:
    print(f"The time is:\t{s} sec(s)")
else: 
    exit()

