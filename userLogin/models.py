# Implemented AbstractBaseUser to make more open so that 
# there woudl be scope to do any change.
# TestCases: Inporogress

from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager

country_list =[('SA', _('South Africa')), ]
type_list = [('U', _('User')), ('D', _('Driver')), ('R', _('Retailer')), ('C', _('Consumer')), ('W', _('Warehouse'))]
class User(AbstractBaseUser, PermissionsMixin):
    uid = models.CharField(_('user id'), max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('sure name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    type = models.CharField(_('type'), max_length=1, choices=type_list)
    phone_number = models.CharField(_('cell number'), max_length=30, blank=True)
    address_line1 = models.CharField(_('address line 1'), max_length=100, blank=False)
    address_line2 = models.CharField(_('address line 2'), max_length=100, blank=True)
    address_line3 = models.CharField(_('address line 3'), max_length=100, blank=True)
    address_line4 = models.CharField(_('address line 4'), max_length=100, blank=True)
    address_line5 = models.CharField(_('address line 5'), max_length=100, blank=True)
    address_line6 = models.CharField(_('address line 6'), max_length=100, blank=True)
    country = models.CharField(_('country'), max_length=100, choices=country_list)
    gps_y_coordinates = models.CharField(_('gps Y coordiats'), max_length=100, blank=True)
    gps_x_coordinates = models.CharField(_('gps X coordiats'), max_length=100, blank=True)
    

    objects = UserManager()

    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
