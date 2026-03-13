from django.urls import path
from .views import landing_page, vote_page

urlpatterns = [
    path("", landing_page, name="home"),
    path("vote/<uuid:token>/", vote_page, name="vote"),
]