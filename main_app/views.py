from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponse, HttpResponseRedirect
# bring in some things to make auth easier
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# bring in decorator
from django.contrib.auth.decorators import login_required


# attempt form
from django.forms.models import model_to_dict

# import models
from .models import Currency, FavCurrencies
# access the FeedingForm
from .forms import FavCurrenciesForm

# import Django form classes
# these handle CRUD for us
# we will comment this one out
# class FavCurrenciesCreate(CreateView):
#   model = FavCurrencies
#   fields = '__all__'s
#   success_url = '/'

# # changed to use custom FavCurrencies_update function with decorator
class FavCurrenciesUpdate(UpdateView):
  model = FavCurrencies
  fields = ['alert_price']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/omni-dashboard')


class FavCurrenciesDelete(DeleteView):
  model = FavCurrencies
  success_url = '/omni-dashboard'


# Create your views here.
def index(request):
    currencies = Currency.objects.values()
    return render(request, 'index.html', {"currencies": currencies})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# def add_to_favorites(request):
#   print(request.POST)
#   return render(request, 'index.html')

@login_required()
def add_to_favorites(request):
  # this time we are passing the data from our request in that form
  form = FavCurrenciesForm(request.POST)
  # validate form.is_valid built in
  print(form.is_valid())
  if form.is_valid():
    # don't save yet!! First lets add out cat_id
    new_curr = form.save(commit=False)
    new_curr.user_id = request.user.id
    # cats been added we can save
    new_curr.save()
    print(new_curr)
  return redirect('omni_dashboard')

# render user's favorite currencies/watchlist
@login_required()
def favorites_index(request):
    # we have access to the user request.user
    # FavCurrencies contains symbol && alert_price
    print(FavCurrencies)
    fav_currencies = FavCurrencies.objects.filter(user= request.user)
    return render(request, 'omni-dashboard.html', { 'favorites': fav_currencies })

def sign_up(request):
  error_message= ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # ok user created log them in
      login(request, user)
      return redirect('index')
    else:
      error_message='That was a no go. Invalid signup'
  # this will run after if it's not a POST or it was invalid
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {
    'form': form,
    'error_message': error_message
  })

def dashboard(request):
  return render(request, 'omni-dashboard.html')


# Instrcutions
# 1. Update index view function to look similar to the contact view function
# 2. Add a index.html page with the current HTML that is displayed
# 3. Update about view function to look similar to the contact view function
# 4. Add a about.html page with the current HTML that is displayed
# 5. Update your urls.py file (main_app) to look similar to the contact path

# 1. Make a view function
# 2. Make the html page
# 3. Add the view to the urls.py inside of main_app.urls

# In browser
# When I go to localhost:8000/contact
# Django -> urls -> /contact -> vews.contact (runs function) -> templates -> contact.html
