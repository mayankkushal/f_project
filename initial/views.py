from django.shortcuts import render
from django.views.generic import FormView

from .forms import BasicForm
# Create your views here.

class BasicView(FormView):
	form_class = BasicForm
	template_name = "initial/form.html"
	success_url = "/"

	def form_valid(self, form):
		form.save()
		return super(BasicView, self).form_valid(form)


