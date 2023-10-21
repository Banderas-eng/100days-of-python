print("Seconds in A Year")
print()

#number of seconds in a day
seconds_in_a_minute = int(60)
seconds_in_an_hour = int(seconds_in_a_minute * 60)
seconds_in_a_day = int(seconds_in_an_hour * 24)

#calculating the number of days in a year
normal_days_in_a_month = int(31 * 7)
fourMonths = int(30 * 4)
monthOfFeb = int(28)
total_days_in_year = normal_days_in_a_month + fourMonths + monthOfFeb

#number of days in a leap year
days_in_a_leapyear = int(total_days_in_year + 1)

#seconds in a normal year and in a leap year
seconds_in_a_year = seconds_in_a_day * total_days_in_year
seconds_in_a_leapyear = seconds_in_a_day * days_in_a_leapyear

normal_year = '{:,}'.format(seconds_in_a_year)
leap_year = '{:,}'.format(seconds_in_a_leapyear)

#to check if its a leap year or not
check_leap_year = input("Is it a leap year? (y/n) ")
if check_leap_year == "y":
    print(leap_year, "seconds")
else:
    print(normal_year, "seconds")