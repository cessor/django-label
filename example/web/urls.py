from django.views.generic import ListView
from django.urls import path
from . import models
urlpatterns = [
    path('', ListView.as_view(model=models.Article))
]
