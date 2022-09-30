from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('patrons/', views.patrons_index, name="patrons_index"),
    path('patrons/<int:patron_id>/', views.patrons_detail, name="patron_detail"),
    path('patrons/<int:patron_id>/add_mealset/', views.add_mealset, name='add_mealset'),
    path('services/', views.services_index, name="services_index"),
    path('services/<int:service_id>/', views.services_detail, name="service_detail"),
    path('patrons/create', views.PatronCreate.as_view(), name="patron_create"),
    path('patrons/<int:pk>/update/', views.PatronUpdate.as_view(), name="patron_update"),
    path('patrons/<int:pk>/delete/', views.PatronDelete.as_view(), name="patron_delete"),
    path('services/create', views.ServiceCreate.as_view(), name='service_create'),
    path('services/<int:pk>/update/', views.ServiceUpdate.as_view(), name='service_update'),
    path('services/<int:pk>/delete/', views.ServiceDelete.as_view(), name='service_delete')
]