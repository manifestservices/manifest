from django.shortcuts import render
from manifest.views import BaseView
# Create your views here.


class ProjectView(BaseView):
    
    def get(self, request,*args,**kwargs):
        """ 
         This function is to fetch home page

        """
        return render(request, 'projects.html',self.context_dict)