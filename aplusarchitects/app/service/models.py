from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
# from django.contrib.staticfiles.templatetags.staticfiles import static
from django.templatetags.static import static
from ..translations import TranslationProxy


class Service(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'))
    percent = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    sort_order = models.IntegerField(
        default=0, validators=[MinValueValidator(0)])
    background = models.ImageField(upload_to='service/', blank=True)

    translated = TranslationProxy()

    class Meta:
        permissions = (
            ('manage_service', _('Manage services.')),
        )

    def __str__(self):
        return self.translated.name

    def get_background(self):
        if self.background:
            return self.background.url
        return static('storefront/images/pages/service/1240x800.png')

    def get_translations(self):
        return self.translations.all()


class ServiceTranslation(models.Model):
    language_code = models.CharField(max_length=10, choices=settings.LANGUAGES)
    service = models.ForeignKey(
        Service, related_name='translations', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField(_('Description'))

    class Meta:
        unique_together = ('language_code', 'service')

    def __str__(self):
        return self.name
