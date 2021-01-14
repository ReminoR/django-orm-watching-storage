from datacenter.models import Passcard
from datacenter.models import Visit, format_duration
from django.shortcuts import render
import django



def storage_information_view(request):
    non_closed_visits = []

    active_visits = Visit.objects.filter(leaved_at=None)

    for visit in active_visits:
      non_closed_visit = {
        'who_entered': visit.passcard,
        'entered_at': visit.entered_at,
        'duration': format_duration(visit.get_duration()),
        'is_strange': visit.is_visit_long()
      }

      non_closed_visits.append(non_closed_visit)

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
