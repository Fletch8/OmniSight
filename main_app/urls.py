from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('accounts/signup', views.sign_up, name='sign_up'),
    path('omni-dashboard/', views.favorites_index, name='omni_dashboard'),
    path('add_currency/', views.add_to_favorites, name='add_to_favorites'),
    path('currecy/<int:pk>/delete/', views.FavCurrenciesDelete.as_view(), name='currency_delete'),
    path('currency/<int:pk>/update/', views.FavCurrenciesUpdate, name='currency_update'),
]

# path('cats/', views.cats_index, name='cats'),
# path('cats/<int:cat_id>/', views.cats_show, name='cats_show'),
# path('cats/create/', views.cats_new, name='cats_create'),
# path('cats/<int:pk>/update/', views.cats_update, name='cats_update'),

# path('cats/<int:pk>/add_feeding/', views.add_feeding, name='add_feeding'),
