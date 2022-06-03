from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    # Q How can i make view empty?, is this a good practce
    path("admin", views.empty, name="admin"),
    path("add", views.add_note, name="add"),
    path("notes", views.notes, name="notes"),
]
