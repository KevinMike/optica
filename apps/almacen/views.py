from django.shortcuts import render
from django.views.generic import View, ListView, DeleteView
from django.template.loader import get_template
import os
# Create your views here.
class Index(View):
    template_name = 'index.html'
    def get(self,request):
        return render(request,self.template_name)
