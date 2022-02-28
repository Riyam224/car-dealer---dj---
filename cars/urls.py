from django.urls import path
from . import views 


urlpatterns = [
    path('' , views.index , name='index'),
    path('about/' , views.about , name='about'),
    path('filter_results/' , views.filter_results , name='filter_results'),
    path('<int:car_id>/' , views.car_detail , name='car_detail'),
    path('inventory/' , views.inventory , name='inventory_cars'),
    path('dealers/' , views.dealers , name='dealers'),
    path('contact/' , views.contact , name='contact'),
]
