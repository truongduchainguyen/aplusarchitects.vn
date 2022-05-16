from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _


class SiteSettings(models.Model):
    site = models.OneToOneField(
        Site, related_name='settings', on_delete=models.CASCADE)
    description = models.CharField(
        _('Description'), max_length=500, blank=True)
    keywords = models.CharField(_('Keywords'), max_length=255, blank=True)
    phone = models.CharField(_('Phone'), max_length=15, blank=True)
    email = models.EmailField(_('Email'), max_length=100, blank=True)
    address = models.CharField(_('Address'), max_length=255, blank=True)

    class Meta:
        permissions = (
            ('manage_sitesettings', _('Manage site settings.')),
        )

    def __str__(self):
        return self.site.domain


class SocialNetwork(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    icon = models.CharField(_('Icon'), max_length=100, blank=True)
    link = models.CharField(_('Link'), max_length=255)

    def __str__(self):
        return self.name

