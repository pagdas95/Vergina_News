from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
import ads.models
import articles
import categories.models
import tags.models
from .models import Author
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
class AuthorView(DetailView):
        #context_object_name = 'author'
        template_name = 'author.html'
        model = Author

        def get(self, request, *args, **kwargs):
            slug = self.kwargs.get('author_id')
            author = Author.objects.filter(slug=slug).first()

            related_authors = Author.objects.order_by('id').exclude(id=author.id)
            articles = author.get_articles().order_by('-updated_at')
            paginator = Paginator(articles, 12)
            page = request.GET.get('page')
            page_articles = paginator.get_page(page)
            article_count = articles.count()
            context = {
                    "author": author,
                    "articles": page_articles,
                    "article_count": article_count,
                    "related_authors": related_authors,
                    "tags": tags.models.TagCloud.get_tags,
                    "ad_sidebar": ads.models.get_priority(9),
            }
            return render(request, 'author.html', context=context)

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
                return HttpResponseRedirect(request.path_info)
