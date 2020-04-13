from django.shortcuts import render
from manifest.views import BaseView
# Create your views here.



class ServicesView(BaseView):
    
    def get(self, request,*args,**kwargs):
        """ 
         This function is to fetch home page

        """
        service=kwargs.get('slug')
        service_map={
                     'ecommerce':'ecommerce.html',
                     'web-applications':'web_applications.html',
                     'search-engine-optimization':'search_engine_optimization.html'   
                        }
        template=service_map[service]
        return render(request, template,self.context_dict)
