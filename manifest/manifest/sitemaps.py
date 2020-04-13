from django.contrib.sitemaps import Sitemap
from blog.models import Blog
from books.models import Book
from django.shortcuts import reverse
from config_master import CATEGORY_LIST


class StaticHighSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'
    def items(self):
        return ['home','reviews','blog']

    def location(self, item):
        return reverse(item)

class CategorySitemap(Sitemap):
    
    priority = 0.9
    changefreq = 'monthly'
    def items(self):
        return CATEGORY_LIST
    
    def location(self,item):
        return reverse('category_slug',args=[item])

class BlogSitemap(Sitemap):
    
    priority = 0.8
    changefreq = 'monthly'
    def items(self):
        return Blog.objects.all()


class BookSitemap(Sitemap):
    
    priority = 0.7
    changefreq = 'daily'
    def items(self):
        return Book.objects.all()

    
class StaticLowSitemap(Sitemap):
    priority = 0.6
    changefreq = 'yearly'
    def items(self):
        return ['login', 'register','contact','legal','tac','faqs', 'about_us', 'press_release','gallery']

    def location(self, item):
        return reverse(item)
    
    