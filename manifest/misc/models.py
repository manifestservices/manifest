# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import logging
log=logging.getLogger(__name__)

class Contact(models.Model):
    name=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=15,default='')
    message = models.TextField(default='')
    created_datetime = models.DateTimeField(auto_now_add=True,null=True)
    created_by=models.CharField(max_length=30, default='',null=True)
    modified_datetime = models.DateTimeField(auto_now=True,null=True)
    modified_by=models.CharField(max_length=30, default='',null=True)
    
class ContactManager(object):
    
    def save_contact_message(self,name,email,phone,message):
        
        Contact.objects.create(name=name,
                               email=email,
                               phone=phone,
                               message=message)
