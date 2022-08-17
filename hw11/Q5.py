import jdatetime

time_inp1 = input('enter date and time: ')
time_inp2 = input('enter date and time: ')
a_day = int(input('enter a day between 0 and 6: '))

time_as_object1 = jdatetime.datetime.strptime(time_inp1, '%Y %m %d')
time_as_object2 = jdatetime.datetime.strptime(time_inp2, '%Y %m %d')


def earlier_date(inp_date1: jdatetime, inp_date2: jdatetime):
    if inp_date1.timestamp() > inp_date2.timestamp():
        first_date = inp_date2
        second_date = inp_date1
    else:
        first_date = inp_date1
        second_date = inp_date2
    return [first_date, second_date]


""" to calculate the date between these two, below steps are followed
    1. calculate the first date in order to get a  start point with earlier_date function
    2. calculate the difference between the day given and the day the user wants to know it's date
    3. switch the first date to the first date of user's day and add up 1 week to that
    4. print the date finally.
    variables are:
    - specific_date: the date should be be printed as the user ordered
    - time_delta: is a week to add up to the created first date
    - diff: differences between the date's day and user's day"""


def get_date(inp_date1: jdatetime, inp_date2: jdatetime, time_inp3):
    """ I ran the earlier_date function 1 time in order to show my best practice code"""

    first_date = earlier_date(inp_date1, inp_date2)[0]
    second_date = earlier_date(inp_date1, inp_date2)[1]
    if time_inp3 < first_date.weekday():
        diff = abs(time_inp3 - first_date.weekday())
        time_delta1 = jdatetime.timedelta(days=diff)
        specific_date = first_date - time_delta1
        time_delta2 = jdatetime.timedelta(weeks=1)
        while specific_date < second_date - time_delta2:
            specific_date += time_delta2
            yield specific_date

    elif time_inp3 > first_date.day:
        diff = (time_inp3 + 1) - first_date.day  # add up 1 is because of the day 0 in days!
        time_delta1 = jdatetime.timedelta(days=diff)
        specific_date = first_date + time_delta1
        time_delta2 = jdatetime.timedelta(weeks=1)
        while specific_date < second_date - time_delta2:
            specific_date += time_delta2
            yield specific_date

    else:
        specific_date = first_date
        time_delta = jdatetime.timedelta(weeks=1)
        while specific_date < second_date - time_delta:
            specific_date += time_delta
            yield specific_date


gt = get_date(time_as_object1, time_as_object2, a_day)
print(next(gt))
print(next(gt))
