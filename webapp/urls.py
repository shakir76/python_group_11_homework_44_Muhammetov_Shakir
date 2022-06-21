from django.urls import path

from webapp.views import form_vie, history

urlpatterns = [
    path('', form_vie),
    path('history/', history),
]
