from django.urls import path, include

from . import views


# URLConfiguration
urlpatterns = [
    path('', views.index),
  #  path('', include('SkillsConnect.urls'))
]