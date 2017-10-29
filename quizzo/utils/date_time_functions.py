def format_quiz_obj_string(string):
    result = {}
    result['month'] = int(string[0:2])
    result['date'] = int(string[3:5])
    result['year'] = int(string[6:10])
    result['hours'] = int(string[11:13])
    result['mintues'] = int(string[14:16])
    result['seconds'] = int(string[17:19])


def format_input_obj_string(string):
    result = {}
    result['month'] = int(string[5:7])
    result['date'] = int(string[8:10])
    result['year'] = int(string[0:4])
    result['hours'] = int(string[11:13]) + 5
    result['mintues'] = int(string[14:16]) + 30
    result['seconds'] = int(string[17:19])

    if result['mintues'] >= 60:
        result['mintues'] = result['mintues'] % 60
        result['hours'] += result['mintues'] / 60

    if result['hours'] >= 24:
        result['hours'] = result['hours'] % 24
        result['date'] += result['hours'] / 24


def number_year(number):
    import calendar
    a = {k: v for k, v in enumerate(calendar.month_abbr)}
    return a[int(number)]


def format_date_string(string):
    if string is None:
        return "Not scheduled"
    else:
        return ("" + number_year(string[0:2]) + "  " + string[3:5] + ", " + string[6:10])
