def computepay(h, r):
    pay = 0
    if h <= 40:
        pay = float(h*r)
    else:
        pay = float((h-40)*1.5*r) + float(40*r)
    return pay
           

h = float(input("Enter Hours: "))
r = float(input("Enter Rate of hours: " ))
p = computepay(h, r)
print("Pay", p)