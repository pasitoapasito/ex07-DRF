from django.urls import path

from api.views import DataRequestView


urlpatterns = [
    path('', DataRequestView.as_view())
]