from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('patrons/', views.patrons_index, name="patrons_index"),
    path('patrons/<int:patron_id>/', views.patrons_detail, name="patrons_detail"),
    path('patrons/create', views.PatronCreate.as_view(), name="patron_create"),
    path('patrons/<int:pk>/update/', views.PatronUpdate.as_view(), name="patron_update"),
    path('patrons/<int:pk>/delete/', views.PatronDelete.as_view(), name="patron_delete")
]