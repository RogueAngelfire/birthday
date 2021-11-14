from django.http.request import HttpRequest
from django.shortcuts import render, HttpResponse
from .forms import BDayRemindersForm

def index(request):

  if request.method == 'POST':
    form = BDayRemindersForm(request.POST)
    if form.is_valid():
      form.save()
  template = 'bdReminders/index.html'
  context = {

  }
  return render(request, template, context)
