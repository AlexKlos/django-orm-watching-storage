def format_duration(duration):
    total_seconds = duration.total_seconds()
    seconds = int(total_seconds % 60)
    minutes = int((total_seconds % 3600) / 60)
    hours = int(total_seconds / 3600)
    str_duration = f'{hours:02}:{minutes:02}:{seconds:02}'
    return str_duration

def format_time(time):
    formated_time = time.strftime('%d %B %Y %H:%M')
    return formated_time