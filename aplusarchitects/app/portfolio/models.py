from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils.encoding import smart_str
from django.urls import reverse
from text_unidecode import unidecode
# from django.contrib.staticfiles.templatetags.staticfiles import static
from django.templatetags.static import static
from ..translations import TranslationProxy


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    translated = TranslationProxy()

    class Meta:
        permissions = (
            ('manage_category', _('Manage portfolio categories.')),
        )

    def __str__(self):
        return self.translated.name

    def get_slug(self):
        return slugify(smart_text(unidecode(self.name)))

    def get_translations(self):
        return self.translations.all()


class CategoryTranslation(models.Model):
    language_code = models.CharField(max_length=10, choices=settings.LANGUAGES)
    category = models.ForeignKey(
        Category, related_name='translations', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('language_code', 'category')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    category = models.ManyToManyField(Category)
    description = models.TextField(_('Description'))
    is_featured = models.BooleanField(_('Is Featured'), default=False)

    translated = TranslationProxy()

    class Meta:
        permissions = (
            ('manage_project', _('Manage portfolio projects.')),
        )

    def __str__(self):
        return self.translated.name

    def get_translations(self):
        return self.translations.all()

    def get_display_categories(self):
        return " / ".join([category.translated.name for category in self.category.all()])

    def get_class_filter(self):
        return " ".join([category.get_slug() for category in self.category.all()])

    def get_first_image(self):
        images = self.images.all()
        return images.first() if images else None

    def get_images(self):
        return self.images.all()

    def get_avatar(self):
        avatar = self.get_first_image()
        if avatar:
            return avatar.image.url
        return static('storefront/images/pages/portfolio/400x600.png')

    def get_slug(self):
        return slugify(smart_text(unidecode(self.name)))

    def get_absolute_url(self):
        return reverse(
            'portfolio:detail', kwargs={'slug': self.get_slug(), 'pk': self.pk}
        )


class ProjectTranslation(models.Model):
    language_code = models.CharField(max_length=10, choices=settings.LANGUAGES)
    project = models.ForeignKey(
        Project, related_name='translations', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField(_('Description'))

    class Meta:
        unique_together = ('language_code', 'project')

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/projects/')
    sort_order = models.IntegerField(default=0)
    alt = models.CharField(max_length=128, blank=True)

    class Meta:
        ordering = ('sort_order',)

    def __str__(self):
        return self.alt
