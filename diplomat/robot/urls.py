from django.urls import path

from . import views

urlpatterns = [
    path("snapshot_webhook_callback", views.snapshot_webhook_callback),
]
