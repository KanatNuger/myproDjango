from django.shortcuts import render
from django.http import HttpResponse
from profiles.models import Article
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
# Create your views here.
HTML_STRING = """
<h1>Hello World</h1>
"""

def home_view2(request):
	article_obj = Article.objects.get(id=1)
	article_queryset = Article.objects.all()
	
	context = {
	    "object_list":article_queryset,
	    "title":article_obj.title,
	    "content":article_obj.content
	}

	HTML_STRING=render_to_string("home-view.html",
    context=context)

	return HttpResponse(HTML_STRING)

def article_search_view(request):
	query_dict = request.GET
	query= query_dict.get("q")
	article_obj = None
	if query is not None:
		article_obj = Article.objects.get(id=query)
	context={
	    "object":article_obj
	}
	return render(request,"articles/search.html", context=context)

def article_detail_view(request,id):
	article_obj = None
	if id is not None:
		article_obj = Article.objects.get(id=id)
	context ={
	"object": article_obj,
	}
	return render(request,"articles/detail.html",context=context)

@login_required
def article_create_view(request):
	form = ArticleForm()
	context ={
		"form" : form
	}
	if request.method == "POST":
		form = ArticleForm(request.POST)
		context['form'] = form
		if form.is_valid():
			title = form.cleaned_data.get("title")
			content = form.cleaned_data.get("content")
			article_object=Article.objects.create(title=title,content=content)
			context['object']=article_object
			context['created']=True
	
	return render(request,"articles/create.html",context=context)