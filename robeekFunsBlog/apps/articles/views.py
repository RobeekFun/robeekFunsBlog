from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Article

def index(request):
	latest_articles_list = Article.objects.order_by('-pub_date')[:100]
	return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404("Статья не найдена!")

	latest_comments_list = a.comment_set.order_by('-id')[:100]
	another_articles = Article.objects.order_by('-pub_date')[:5]

	return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list, 'another_articles': another_articles})

def leave_comment(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404("Статья не найдена!")

	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'], pub_date = timezone.now())

	return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )
