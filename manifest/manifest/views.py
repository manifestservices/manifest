from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib.sitemaps import Sitemap
import logging,datetime,random
from config_master import service_list
from utils.send_mail import SendMail
log=logging.getLogger(__name__)

# def error_404(request,exception,template_name='404.html'):
#         data = {}
#         return render(request,'404.html', data)
#
# def error_500(request,exception,template_name='500.html'):
#         data = {}
#         return render(request,'500.html', data)

class BaseView(View):
    """
    :Brief: Custom base class for django's class based views
    """

    def __init__(self, **kwargs):
        """ Initializes the base view object
        """
        self.context_dict={}
        super(BaseView, self).__init__(**kwargs)
    
    
    def __set_visit_cookie(self,cookie):
        """
        :brief: This method generates and sets the cookie if not present
        value
        Note: String None is checked to reset the existing erroneous cookies being set as string NONE
        """
        if cookie and str(cookie).lower().strip()!='none':
            log.info('Cookie already exists cookie::%s'%cookie)
            return cookie
        datetime_val = datetime.datetime.now()
        visit_cookie_id = datetime_val.strftime('%Y%m%d%H%M%S') \
                                       + str(random.randint(0,1000))
        log.info('Exiting __set_visit_cookie cookie::%s'%visit_cookie_id)
        return visit_cookie_id

    def dispatch(self, request, *args, **kwargs):
        """ Customized dispatch method
        """
        visit_cookie_id=self.__set_visit_cookie(request.COOKIES.get('visit_cookie_id'))
        response = super(BaseView, self).dispatch(request, *args, **kwargs)
        if request.method.lower()=='get':
            response.set_cookie('visit_cookie_id',visit_cookie_id,
                                        max_age=365*24*60*60)
        return response
    
class TemplateView(BaseView):

    def get(self, request,*args,**kwargs):
        """ 
         This function is to fetch html template
        :NOTE:
        """
        if not kwargs.get('template'):
            return render(request,'index.html')
        page = kwargs['template']+'.html'
        return render(request,page) 
    
    
class HomePageView(BaseView):
    
    def get(self, request,*args,**kwargs):
        """ 
         This function is to fetch home page

        """
        return render(request, 'index.html',self.context_dict)

class AboutusView(BaseView):
    
    def get(self, request,*args,**kwargs):
        """ 
         This function is to fetch home page

        """
        return render(request, 'about_us.html',self.context_dict)


class ContactView(BaseView):
    
    def get(self, request,*args,**kwargs):
        """ 
         This function is to fetch home page

        """
        
        return render(request, 'contact_us.html',self.context_dict)
    
    
    def post(self, request,*args,**kwargs):
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        SendMail().send(name,email,message)
        return HttpResponseRedirect(reverse('thankyou'))
 
class SurveyView(BaseView):
    
    def get(self, request,*args,**kwargs):
        """ 
         This function is to fetch home page

        """
        
        return HttpResponseRedirect('https://aarfireee.typeform.com/to/gpNvZc')
           
class ThankyouView(BaseView):
    def get(self, request,*args,**kwargs):
        return render(request,'thankyou.html')
    
class StaticHighSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'
    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

class CategorySitemap(Sitemap):
    
    priority = 0.9
    changefreq = 'monthly'
    def items(self):
        return service_list()
    
    def location(self,item):
        return reverse('services',args=[item])

# class BlogSitemap(Sitemap):
#     
#     priority = 0.8
#     changefreq = 'monthly'
#     def items(self):
#         return Blog.objects.all()

class StaticLowSitemap(Sitemap):
    priority = 0.6
    changefreq = 'yearly'
    def items(self):
        return ['about_us', 'contact_us','projects']

    def location(self, item):
        return reverse(item)
    
    
