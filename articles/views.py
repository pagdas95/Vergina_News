from django.shortcuts import render, redirect
from .models import Article
from categories.models import SubCategory
from subscribers.models import Subscriber
from tags.models import Tags
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import ads.models
import json
import requests

# Google captcha
from decouple import config

# Create your views here.
def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

class ArticleView(DetailView):
        context_object_name = 'articles'
        template_name = 'article.html'
        model = Article

        def get(self, request, *args, **kwargs):
            post_slug = kwargs.get('title')
            detail = Article.objects.get(slug=post_slug)
            detail.total_views = detail.total_views + 1
            detail.save(update_fields=['total_views'])
            related_articles = Article.objects.filter(category=detail.category, sub_category=detail.sub_category).filter(publish=True).exclude(id=detail.id) if detail.sub_category else Article.objects.filter(category=detail.category).filter(publish=True).exclude(id=detail.id)
            context = {
                "id": detail.id,
                "title": detail.title,
                "authors": detail.get_authors(),
                "updated_at":detail.updated_at,
                "comments": detail.get_comments(),
                "category": detail.category.name,
                "sub_category": detail.sub_category if detail.sub_category else detail.category,
                "related_articles":  related_articles,
                "total_views": detail.total_views,
                "tags": detail.get_tags(),
                "article_pic": detail.article_pic,
                "article_video": detail.article_video,
                "text": detail.text,
                "site_key": config('RECAPTCHA_PUBLIC_KEY'),
                "ad_banner": ads.models.get_priority(7),
                "ad_sidebar": ads.models.get_priority(8),
             }
            return render(request, "article.html", context=context)

        def post(self, request, *args, **kwargs):
            if request.POST.get('ad_id'):
                id = request.POST.get('ad_id')
                ad = ads.models.Ad.objects.get(id=id)
                ad.total_views = ad.total_views + 1
                ad.save(update_fields=['total_views'])
                return HttpResponseRedirect(ad.url)

            keyword = request.POST.get('search')
            if keyword:
                if keyword == "":
                    result = 'all'
                else:
                    result = keyword
                return redirect('articles_view', search=result)
            else:
                request.session['email'] = request.POST.get('email_sub')

            # Check for Captcha POST then validate
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            data = {
                'secret':  config('RECAPTCHA_PRIVATE_KEY'),
                'response': recaptcha_response,
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()

            if result['success']:
                # Check for comment POST  then validate
                id = request.POST.get('Article ID')
                if id and request.POST.get('author') and request.POST.get('email') and request.POST.get('comment'):
                    comment = {
                        "author": request.POST.get('author'),
                        "email": request.POST.get('email'),
                        "text": request.POST.get('comment')
                    }
                    article = Article.objects.get(id=id)
                    article.add_comment(comment)
                    context = {
                        'post_id': article.id,
                        'category': article.category,
                        'sub_category': article.sub_category
                    }
                    messages.success(request, 'New comment added with success!')
            else:
                messages.info(request, 'Invalid reCAPTCHA. Please try again.')
            return HttpResponseRedirect(self.request.path_info)

class AllArticlesView(DetailView):
        context_object_name = 'All'
        template_name = 'allarticles.html'
        model = Article

        def get(self, request, *args, **kwargs):
            tags = Tags.objects.all().values_list('name', flat=True).distinct()
            if kwargs['search'] == 'all':
                articles = Article.objects.filter(publish=True).order_by('-updated_at')
            elif kwargs['search'] == 'popular':
                articles = Article.objects.filter(publish=True).order_by('-total_views')
            elif kwargs['search'] in tags:
                tag = Tags.objects.get(name=kwargs['search'])
                tag.total_views = tag.total_views + 1
                tag.save(update_fields=['total_views'])
                articles = Article.objects.filter(tags__name=kwargs['search']).filter(publish=True).order_by('-updated_at')
            else:
                articles = Article.objects.filter(title__icontains=kwargs['search']).filter(publish=True).order_by('-updated_at')

            paginator = Paginator(articles, 8)
            page = request.GET.get('page')
            page_articles = paginator.get_page(page)
            article_count = articles.count()
            context = {
                "articles": page_articles ,
                'article_count' : article_count,
                'search': kwargs['search'],
            }
            return render(request, "allarticles.html", context=context)

        def post(self, request, *args, **kwargs):
            request.session['email'] = request.POST.get('email_sub')
            keyword = request.POST.get('search')
            if keyword == "":
                result = 'all'
            else:
                result = keyword
            return redirect('articles_view', search=result)



from django.views.decorators.http import require_http_methods

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_http_methods(["POST"])
def preview_article(request, pk=None):
    title = request.POST.get('title', '')
    text = request.POST.get('text', '')
    authors = request.POST.getlist('author')
    updated_at = request.POST.get('updated_at')
    tags = request.POST.getlist('tags')



    preview_html = render_to_string('article_preview.html', {
        'title': title,
        'text': text,
        'authors': authors,
        'updated_at': updated_at,
        'tags': tags,

    })

    return JsonResponse({'preview_html': preview_html})
