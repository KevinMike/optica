from django.shortcuts import render
from django.views.generic import View, ListView, DeleteView

# Create your views here.
class Index(View):
    def get(request,self):
        template_name="index.html"
        return render(request,template_name)