from django.db import models


class BDayReminders(models.Model):

  class Meta:
    verbose_name_plural = 'Birthday-Reminders'

  name = models.CharField(max_length=100, null=False, blank=False)
  email = models.EmailField(max_length=150, null=False, blank=False)
  dateofbirth = models.DateTimeField()
