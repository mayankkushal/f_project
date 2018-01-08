from django.shortcuts import render
from django.views.generic import FormView

from .forms import BasicForm
# Create your views here.

class BasicView(FormView):
	form_class = BasicForm
	template_name = "initial/form.html"

	def post(self, request, *args, **kwargs):
		"""
		Other data processing goes here
		"""
		pass