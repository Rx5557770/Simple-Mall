from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('orders/', include('apps.trade.urls')),
]