from django.shortcuts import render
from django.views import generic
from .forms import FormExemple
from django.http import HttpResponse


# Create your views here.


class HomeView(generic.TemplateView):
    template_name = "forms/index.html"


class FormView(generic.FormView):
    template_name = "forms/test_modal.html"
    form_class = FormExemple

    def form_valid(self, form):
        return HttpResponse("Form valid")

    def form_invalid(self, form):
        return HttpResponse("Form invalid")
