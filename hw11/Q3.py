from datetime import datetime, date
import jdatetime

time_inp1 = input('enter date and time: ')
time_inp2 = input('enter date and time: ')

time_as_object1 = datetime.strptime(time_inp1, '%Y %m %d %H %M %S')
time_as_object2 = datetime.strptime(time_inp2, '%Y %m %d %H %M %S')

""" I have used timestamp to convert the input to seconds. 
    Then I used absolute value of their minus to return a meaningful value."""


def time_delta(time_object1: datetime, time_object2: datetime):
    time_object1_secs = time_object1.timestamp()
    time_object2_secs = time_object2.timestamp()
    time_delta.secs = abs(time_object1_secs - time_object2_secs)
    return f'time delta is {time_delta.secs} seconds.'


""" To calculate leap years I did following steps:
    1. get the years of two inputs
    2. add up with 1 the greater input
    3. convert these two years to days
    4. minus these two outputs
    5. then I have calculated the remaining of the output divided into 365 days of a year"""


def leap_year(time_object1: datetime, time_object2: datetime):
    time_object1_year = date(time_object1.year, 1, 1)
    time_object2_year = date(time_object2.year, 1, 1)
    delta_days = abs(time_object1_year - time_object2_year)

    if delta_days.days != 0 and (delta_days.days // 365) % 365 == 0:
        leap = ((delta_days.days // 365) * 365) + delta_days.days % 365
    else:
        leap = delta_days.days % 365
    return f'leap years count is {leap}'


""" to calculate number of changes for time these steps were followed:
    1. if date was after 6th month, we do not have any time change
    2. if date was before 6th month we have one change
    3. between these two years we have 2 changes"""


def change_time(time_object1: datetime, time_object2: datetime):
    t_change = abs((time_object1.year - time_object2.year - 1)) * 2
    if time_object1.month <= 6:
        t_change += 1
    elif time_object2.month <= 6:
        t_change += 1
    return f'time has been changed {t_change} times between these two dates'


def jalali_calendar(time_object1: datetime, time_object2: datetime):
    first_jalali_date = jdatetime.date.fromgregorian(day=time_object1.day, month=time_object1.month,
                                                     year=time_object1.year)
    second_jalali_date = jdatetime.date.fromgregorian(day=time_object2.day, month=time_object2.month,
                                                      year=time_object2.year)
    print(first_jalali_date)
    return f'Jalali dates are {first_jalali_date} and {second_jalali_date}'


print(time_delta(time_as_object1, time_as_object2))
print(leap_year(time_as_object1, time_as_object2))
print(change_time(time_as_object1, time_as_object2))
print(jalali_calendar(time_as_object1, time_as_object2))
