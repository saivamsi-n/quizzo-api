def number_year(number):
    import calendar
    a = {k: v for k, v in enumerate(calendar.month_abbr)}
    return a[int(number)]


def format_date_string(string):
    if string is None:
        return "Not scheduled"
    else:
        hours,meridiem = format_hours(int(string[11:13]))
        return ("" + number_year(string[0:2]) + "  " + string[3:5] + " " + hours +":"+string[14:16]+" "+meridiem+", "+ string[6:10])

def format_hours(number):
    if number <12:
        return str(number), "AM"
    elif number>12:
        return  str(number-12), "PM"
    else:
        return str(12), "PM"