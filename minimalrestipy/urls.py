from django.urls import path

from restipy import views

urlpatterns = [
    path("env", views.Environment.as_view(), name='env_view'),
    path("info", views.Info.as_view(), name='info_view'),
    path("health", views.Health.as_view(), name='health_view'),
    path("endpoint0", views.Endpoint0.as_view(), name='endpoint0_view'),
]
