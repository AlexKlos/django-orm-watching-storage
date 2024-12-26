from django.shortcuts import render
from django.utils.timezone import localtime, now

from datacenter.models import Visit


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


def storage_information_view(request):
    non_closed_visits = []
    current_visits = Visit.objects.filter(leaved_at=None)

    for current_visit in current_visits:
        visitor_name = current_visit.passcard.owner_name
        entered_time = localtime(current_visit.entered_at).replace(microsecond=0)
        str_entered_time = entered_time.strftime('%d %B %Y %H:%M')
        duration = format_duration(get_duration(current_visit))
        non_closed_visits.append(
            {
                'who_entered': visitor_name,
                'entered_at': str_entered_time,
                'duration': duration,
                'is_strange': is_visit_long(current_visit)
            }
        )

    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
