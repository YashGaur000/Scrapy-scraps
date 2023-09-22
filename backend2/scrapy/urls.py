from django.urls import path
from .views import DisplayData


urlpatterns = [
    path("", DisplayData.as_view(), name="ToDo")

]