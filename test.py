from datetime import timedelta

def format_duration(duration):
    str_duration = str(duration).split('.')[0]
    return str_duration

def test_format_duration():
    test_values = [
        timedelta(seconds=1),
        timedelta(seconds=45),
        timedelta(seconds=3600),
        timedelta(minutes=2),
        timedelta(hours=1, minutes=15, seconds=45),
        timedelta(days=1, hours=5, minutes=10, seconds=30),
        timedelta(weeks=2),
        timedelta(microseconds=123456),
        timedelta(days=-1, hours=3),
    ]
    
    for value in test_values:
        print(f"Input (duration): {value}, Output (str_duration): {format_duration(value)}")

test_format_duration()
