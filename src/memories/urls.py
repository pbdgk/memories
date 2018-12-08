from django.urls import path
from . import views

app_name = "memories"

urlpatterns = [
    path('', views.Index.as_view(), name='main'),

]