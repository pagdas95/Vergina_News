from django.shortcuts import render
from django.views.generic.detail import DetailView
import articles

from articles.models import Article
from .models import Category , SubCategory
from django.views.generic.list import ListView


# Create your views here.
class CategoryView(DetailView):
    context_object_name = 'category'
    template_name = 'categories.html'
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category')
        articles = Article.objects.all().filter(category__name=category)
        context = {
                "category":self.kwargs.get('category'),
                "sub_category":self.kwargs.get('sub_category'),
                "articles": articles,
        }
        return render(request, "category.html", context=context)

class SubCategoryView(DetailView):
    context_object_name = 'sub_category'
    template_name = 'categories.html'
    model = SubCategory

    def get(self, request, *args, **kwargs):
        sub_category = self.kwargs.get('sub_category')
        print(sub_category)
        detail = Article.objects.all().filter(sub_category__slug = sub_category)
        context = {
                "detail": detail,
        }
        return render(request, "category.html", context=context)
