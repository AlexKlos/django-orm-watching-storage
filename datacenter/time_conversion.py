def format_duration(duration):
    str_duration = str(duration).split('.')[0]
    return str_duration

def format_time(time):
    formated_time = time.strftime('%d %B %Y %H:%M')
    return formated_time