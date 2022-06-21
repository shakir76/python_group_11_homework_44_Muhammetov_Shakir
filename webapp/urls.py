from django.urls import path

from webapp.views import form_vie

urlpatterns = [
    path('', form_vie),
]
