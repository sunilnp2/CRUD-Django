from django.urls import path
from data.views import *
app_name = 'data'

urlpatterns = [
    #  path('', HomeView.as_view(), name='home'),
    path('', home, name='home'),
    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:id>', update, name='update'),
 ]
 