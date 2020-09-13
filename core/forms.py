from django import forms
from django.db import models
from core.models import Item
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title',
                'slug_title',
                'category',
                'label',
                'contents_short',
                'contents_long',
                'imgsrc',
                'image']
                
""" CATEGORY_CHOICES = (
    ('Diary', 'Diary'),
    ('Career', 'Career'),
    ('Relationship', 'Relationship'),
    ('Travel', 'Travel'),
)

LABEL_CHOICES = (
    ('None', 'None'),
    ('Notice', 'Notice'),
    ('English', 'English'),
    ('French', 'French'),
)

class ItemForm(forms.Form):
    title = forms.CharField(max_length=100)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.widgets.Select())
    label = forms.ChoiceField(choices=LABEL_CHOICES, required=False, widget=forms.widgets.Select())
    slug = forms.SlugField()
    contents_short = forms.CharField(widget=forms.Textarea, required=False)
    contents_long = forms.CharField(widget=forms.Textarea, required=False)
    imgsrc = forms.URLField(required=False, widget=forms.widgets.URLInput())
    image = forms.ImageField(required=False, widget=forms.widgets.ClearableFileInput()) """
    