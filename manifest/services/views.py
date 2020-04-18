from django.shortcuts import render
from manifest.views import BaseView
from config_master import service_map
# Create your views here.



class ServicesView(BaseView):
    
    def get(self, request,*args,**kwargs):
        """ 
         This function is to fetch home page

        """
        service=kwargs.get('slug')
        template=service_map[service]
        return render(request, template,self.context_dict)
