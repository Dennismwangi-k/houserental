from django.urls import path
from .views import HomeView,AboutView,ContactView,PropertyView,AgentView

urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("about/",AboutView.as_view(),name="about"),
    path("contact/",ContactView.as_view(),name="contact"),
    path("property/",PropertyView.as_view(),name="property"),
    path("agent/",AgentView.as_view(),name="agent"),

]
