from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Visit
from datacenter.time_conversion import format_duration, format_time
from datacenter.visit_utils import get_duration, is_visit_long


def storage_information_view(request):
    non_closed_visits = []
    current_visits = Visit.objects.filter(leaved_at=None)

    for current_visit in current_visits:
        visitor_name = current_visit.passcard.owner_name
        entered_time = localtime(current_visit.entered_at)
        str_entered_time = format_time(entered_time)
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
