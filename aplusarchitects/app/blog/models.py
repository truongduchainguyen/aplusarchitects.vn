from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.utils.encoding import smart_str
from django.utils.translation import gettext_lazy as _
# from django.contrib.staticfiles.templatetags.staticfiles import static
from django.templatetags.static import static
from text_unidecode import unidecode
from ..translations import TranslationProxy
from ..account.models import User


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    translated = TranslationProxy()

    class Meta:
        permissions = (
            ('manage_category', _('Manage blog categories.')),
        )

    def __str__(self):
        return self.translated.name

    def get_num_post(self):
        return self.post.count()

    def get_slug(self):
        return slugify(smart_text(unidecode(self.name)))

    def get_absolute_url(self):
        return reverse(
            'blog:category', kwargs={'slug': self.get_slug(), 'pk': self.pk}
        )


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


class Tag(models.Model):
    name = models.CharField(_('Name'), max_length=50)

    translated = TranslationProxy()

    class Meta:
        permissions = (
            ('manage_tag', _('Manage blog tags.')),
        )

    def __str__(self):
        return self.translated.name

    def get_slug(self):
        return slugify(smart_text(unidecode(self.name)))

    def get_absolute_url(self):
        return reverse(
            'blog:tag', kwargs={'slug': self.get_slug(), 'pk': self.pk}
        )


class TagTranslation(models.Model):
    language_code = models.CharField(max_length=10, choices=settings.LANGUAGES)
    tag = models.ForeignKey(
        Tag, related_name='translations', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('language_code', 'tag')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    description = models.CharField(_('Description'), max_length=150)
    content = models.TextField(_('Content'))
    image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)
    author = models.ForeignKey(
        User, related_name='post', on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name='post', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='post', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    translated = TranslationProxy()

    class Meta:
        permissions = (
            ('manage_post', _('Manage blog posts.')),
        )

    def __str__(self):
        return self.translated.title

    def get_slug(self):
        return slugify(smart_text(unidecode(self.title)))

    def get_absolute_url(self):
        return reverse(
            'blog:detail', kwargs={'slug': self.get_slug(), 'pk': self.pk}
        )

    def get_display_image(self):
        if self.image:
            return self.image.url
        return static('storefront/images/pages/blog/1240x800.png')


class PostTranslation(models.Model):
    language_code = models.CharField(max_length=10, choices=settings.LANGUAGES)
    post = models.ForeignKey(
        Post, related_name='translations', on_delete=models.CASCADE
    )
    title = models.CharField(_('Title'), max_length=255)
    content = models.TextField(_('Content'))

    class Meta:
        unique_together = ('language_code', 'post')

    def __str__(self):
        return self.title
