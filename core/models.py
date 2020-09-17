from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.shortcuts import reverse
from django_countries.fields import CountryField


CATEGORY_CHOICES = (
    ('Diary', 'Diary'),
    ('Career', 'Career'),
    ('Relationship', 'Relationship'),
    ('Travel', 'Travel'),
)

LABEL_CHOICES = (
    ('Notice', 'Notice'),
    ('English', 'English'),
    ('French', 'French'),
    ('Korean', 'Korean')
)


@python_2_unicode_compatible
class Item(models.Model):
    title = models.CharField(max_length=100)
    slug_title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    label = models.CharField(choices=LABEL_CHOICES,
                             max_length=30, null=True, blank=True)
    slug = models.SlugField(unique=True)
    contents_short = models.TextField(blank=True, null=True)
    contents_long = models.TextField(blank=True, null=True)
    imgsrc = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(null=True, blank=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_create_date_str(self): 
        return self.create_date.strftime("%Y. %m. %d.")    
