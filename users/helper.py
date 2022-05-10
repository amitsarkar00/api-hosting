from django.core.cache import cache
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.conf import settings

import math, random

from rest_framework.authtoken.models import Token

def generateOTP(data, field, digits, time) :
    """
    function to generate OTP
    """
    
    otp_key = data + '_' + field
    OTP = cache.get(otp_key)
    if(not OTP):
        OTP = str(math.floor(random.random() * 10 ** digits))
        cache.set(otp_key, OTP, time)
 
    return OTP

def verifyOTP(data, field, OTP):
    """
    function to verify OTP
    """

    otp_key = data + '_' + field
    return cache.get(otp_key) == OTP

def email_verification_send(email, OTP):
    # plaintext = get_template('email.txt')
    text_content  = ''
    context = { 
        'first_name': email.split('@')[0],
        'otp' :  OTP
    }

    subject = 'Shivila Mail Verification'
    from_email, to = settings.EMAIL_FROM, email
    html_content = render_to_string('email/email_verification_otp.html', context)
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def filter_dict(obj:dict, fields:list):
    """
    Filters Dict using a list of keys
    """
    new_obj = {key: obj[key] for key in obj.keys() if key in fields}
    return new_obj


def email_verification_send1(user, verification):
    # plaintext = get_template('email.txt')
    htmly = get_template('email/email_verification.html')

    context = { 
        'first_name': user.first_name,
        'url' :  'http://localhost:8000/verification/email/' + str(verification.token) + '/'
        }

    subject, from_email, to = 'Shivila Mail Verification', settings.EMAIL_FROM, user.email
    # text_content = plaintext.render(d)
    html_content = render_to_string('email/email_verification.html', context)
    msg = EmailMultiAlternatives(subject, '', from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def get_token_by_user(user=None):
    token, created = Token.objects.get_or_create(user=user)
    return {
        'token' : token.key,
        'role' : user.role
    }