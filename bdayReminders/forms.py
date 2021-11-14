from django import forms
from .models import BDayReminders


class BDayRemindersForm(forms.ModelForm):
  class Meta:
    model = BDayReminders
    fields = [
      'name',
      'email',
      'dateofbirth'
    ]