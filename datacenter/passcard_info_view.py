from django.shortcuts import render, get_object_or_404

from datacenter.models import Passcard, Visit
from datacenter.time_conversion import format_duration, format_time
from datacenter.visit_utils import get_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        entered_at = format_time(visit.entered_at)
        duration = format_duration(get_duration(visit))
        this_passcard_visits.append(
            {
                'entered_at': entered_at,
                'duration': duration,
                'is_strange': is_visit_long(visit, 60),
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
