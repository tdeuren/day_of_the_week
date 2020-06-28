def day_of_the_week(day, month, year):
    """The function returns the day of the week for a given date."""
    a = (year//100)%4
    if a == 0:
        a = 2
    elif a == 1:
        a = 0
    elif a == 2:
        a = 5
    b = (year - (year//100)*100)//12
    c = (year - (year//100)*100)%12
    d = c//4
    e = a+b+c+d
    f = e%7
    l = [3,28,14,4,9,6,11,8,5,10,7,12]
    z = l[month-1]
    if year%4 == 0:
        if year%400 == 0 and month < 3:
            z += 1
        if year%100 != 0 and month < 3:
            z += 1
    x = abs(z - day)
    y = (f+x)%7
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[y]

if __name__ == "__main__":
    print(day_of_the_week(11, 8, 2020))