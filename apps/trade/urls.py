from django.urls import path, include
from . import views
app_name = 'trade'

urlpatterns = [
    path('<int:pk>/', views.OrderCreateView.as_view(), name='create_order'),
    path('pay-back/', views.PayBackView.as_view(), name='payback'),
]