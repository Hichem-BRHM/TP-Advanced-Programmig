name1 = input("enter name of first runner :")
time1 = float(input("enter Time (in seconds) of first runner :"))

name2 = input("enter name of second runner :")
time2 = float(input("enter Time (in seconds) of second runner :"))


print("Runner 1 :")
print(f"Name: {name1}")
print(f"Time (in seconds): {time1}")
print("Runner 2 :")
print(f"Name: {name2}")
print(f"Time (in seconds): {time2}")

if time1 < time2 :
    print(f"The faster runner is {name1}")
elif time2 < time1 :
    print(f"The faster runner is {name2}")
else :
    print(f"{name1} et {name2} have the same time")