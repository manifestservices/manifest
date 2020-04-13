from django.shortcuts import render
from manifest.views import BaseView
# Create your views here.
import logging
log=logging.getLogger(__name__)

class BlogView(BaseView):
      
    def get(self, request, *args, **kwargs):
        """
            Rendering confirm order page    
        """
        log.info('Entering Blog GET')
        slug=kwargs.get('slug')
        if slug:
            pass
        return render(request,'blog.html',self.context_dict)