from datetime import timedelta

def format_duration(duration):
    total_seconds = duration.total_seconds()
    seconds = int(total_seconds % 60)
    minutes = int((total_seconds % 3600) / 60)
    hours = int(total_seconds / 3600)
    str_duration = f'{hours:02}:{minutes:02}:{seconds:02}'
    return str_duration

def test_format_duration():
    test_values = [
        timedelta(seconds=1),
        timedelta(seconds=45),
        timedelta(minutes=2),
        timedelta(hours=1, minutes=15, seconds=45),
        timedelta(days=1, hours=5, minutes=10, seconds=30),
        timedelta(weeks=2),
        timedelta(microseconds=123456),
        timedelta(days=-1, hours=3),
    ]
    
    for value in test_values:
        print(f"Input: {value}, Output: {format_duration(value)}")

test_format_duration()