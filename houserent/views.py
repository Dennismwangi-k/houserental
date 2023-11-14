from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,"index.html")
    

class AboutView(View):
    def get(self,request):
        return render(request,"about.html")
    

class ContactView(View):
    def get(self,request):
        return render(request,"contact-us.html")

class PropertyView(View):
    def get(self,request):
        return render(request,"property.html")
class AgentView(View):
    def get(self,request):
        return render(request,"agency.html")