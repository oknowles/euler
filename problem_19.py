days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return (year % 4 == 0) or ((year % 100) + (year % 400) == 0)

def increment_date(day, month, year):
    if (day < days_in_month[month - 1]):
        return day + 1, month, year
    if (month < 12):
        return 1, month + 1, year

    # dec 31st so new year
    days_in_month[1] = 29 if is_leap_year(year + 1) else 28
    return 1, 1, year + 1

def parse_date_string(date_string):
    day = int(date_string[0:2])
    month = int(date_string[3:5])
    year = int(date_string[6:11])
    return day, month, year

def sunday_on_first(day_of_week, cur_day):
    return (cur_day == 1) and (day_of_week == 6)

def first_sunday_count(from_date, to_date, start_day_of_week):
    cur_day, cur_month, cur_year = parse_date_string(from_date)
    to_day, to_month, to_year = parse_date_string(to_date)
    day_of_week = start_day_of_week
    sunday_count = 0

    while ((cur_day != to_day) or (cur_month != to_month) or (cur_year != to_year)):
        sunday_count += 1 if sunday_on_first(day_of_week, cur_day) else 0
        cur_day, cur_month, cur_year = increment_date(cur_day, cur_month, cur_year)
        day_of_week = (day_of_week + 1) % 7

    sunday_count += 1 if sunday_on_first(day_of_week, cur_day) else 0

    return sunday_count, day_of_week


start_date = '01-01-1901'
end_date = '31-12-2000'

# start counting from monday 01/01/1900 to get current day of the week
_, from_day_of_week = first_sunday_count('01/01/1900', start_date, 0)
sunday_count, _ = first_sunday_count(start_date, end_date, from_day_of_week)

print 'number of sundays between {} and {} = {}'.format(start_date, end_date, sunday_count)
