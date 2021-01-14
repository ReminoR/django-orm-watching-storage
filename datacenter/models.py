from django.db import models
from datetime import datetime, timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
      return "{user} entered at {entered} {leaved}".format(
          user=self.passcard.owner_name,
          entered=self.entered_at,
          leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
      )

    def get_duration(self):
      if self.leaved_at:
        return self.leaved_at - self.entered_at
      else:
        return datetime.now(tz = timezone.utc) - self.entered_at

    def is_visit_long(self, minutes=60):
      duration = self.get_duration().total_seconds() // 60
      return duration >= minutes

def format_duration(duration):
    duration_seconds = duration.total_seconds()
    result = str(round(duration_seconds // 3600)) + ':' + str(round(duration_seconds % 3600 / 60)) + ':' + str(round(duration_seconds % 3600 % 60))
    return result
