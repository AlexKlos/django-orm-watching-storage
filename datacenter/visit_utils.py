from django.utils.timezone import now


def get_duration(visit):
    if visit.leaved_at is None:
        duration = now() - visit.entered_at
    else:
        duration = visit.leaved_at - visit.entered_at
    return duration


def is_visit_long(visit, minutes=60):
    return get_duration(visit).total_seconds() > minutes * 60