from django import forms
from .models import Currency, FavCurrencies

class UpadateCurrencyForm(forms.ModelForm):
    # meta class beacuse that's how django can do it
    class Meta:
        # which model
        model = FavCurrencies
        fields = ['alert_price']

# add fav curr form
class FavCurrenciesForm(forms.ModelForm):
    class Meta:
        model = FavCurrencies
        fields = ['symbol', 'alert_price']