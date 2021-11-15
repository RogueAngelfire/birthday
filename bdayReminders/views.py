from django.http.request import HttpRequest
from django.shortcuts import render, HttpResponse
from .forms import BDayRemindersForm
from django.core.mail import send_mail

def index(request):

  if request.method == 'POST':
    form = BDayRemindersForm(request.POST)
    if form.is_valid():
      form.save()
  template = 'bdReminders/index.html'
  context = {

  }

# Start 
#def contact(request):
 # if request.method == "POST":
  #  message_name = request.POST['message-name']
  #  message_email = request.POST['message-email']
  #  message = request.POST['message']

    # send an email on Birthday!
  #  send_mail(
  #    message_name, # subject
   #   message, # message
  #    message_email, # from email
  #    ['rogueangelimage@gmail.com'], # to email
  #  )

  #return render(request, 'contact.html', {'message_name': message_name,})
# End
  
  return render(request, template, context)
