from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
HTML_STRING = """
<h1>Hello World</h1>
"""
def home_view(request):


	return HttpResponse(HTML_STRING)