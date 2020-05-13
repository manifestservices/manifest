'''
Created on Jun 24, 2018

@author: thilak.desingh
'''
from django.core.mail import EmailMessage
from config_master import *    
from django.shortcuts import reverse
from django.views.generic import View
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User, Group
import logging,datetime
log=logging.getLogger(__name__)

text_content='test'


class SendMail(View):
    def __init__(self):
        log.info('SendMail class initialized')
    def send(self,name,email,phone,message):
        """
            Default method to send SMTP mails
        """
        body="SENT BY: %s "%email+ "Phone: "+phone +"CONTENT: "+message
        email = EmailMessage('CONTACT US MESSAGE',body,to=['info@manifestservices.in','servicesmanifest@gmail.com'])
        email.send()
    