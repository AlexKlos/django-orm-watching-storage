from django.utils.timezone import now


def get_duration(visit):
    if visit.leaved_at == None:
        duration = now().replace(microsecond=0) - visit.entered_at.replace(microsecond=0)
    else:
        duration = visit.leaved_at.replace(microsecond=0) - visit.entered_at.replace(microsecond=0)
    return duration


def format_duration(duration):
    str_duration = str(duration)
    return str_duration


def is_visit_long(visit, minutes=60):
    return get_duration(visit).total_seconds() > minutes * 60