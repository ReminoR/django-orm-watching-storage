from datacenter.models import Passcard
from datacenter.models import Visit, format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    passcard_by_passcode = Passcard.objects.get(passcode=passcode)
    all_visits_by_passcard = Visit.objects.filter(passcard=passcard_by_passcode)

    this_passcard_visits = []

    for visit in all_visits_by_passcard:
      this_passcard_visit = {
        'entered_at': visit.entered_at,
        'duration': visit.get_duration() if visit.leaved_at else format_duration(visit.get_duration()),
        'is_strange': visit.is_visit_long()
      }

      this_passcard_visits.append(this_passcard_visit)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
