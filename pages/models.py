from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render


# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default="")
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=3)
    image_url = models.URLField(default="https://www.hitpromo.net/imageManager/show/ZBOX-MINCEREAL_blank2.jpg",
                                blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class MyForm(forms.ModelForm):
    class Meta:
        model = Snack
        fields = ('name', 'description', 'reviewer', 'rating', 'image_url',)

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['image_url'].required = False
        if not self.initial.get('image_url'):
            self.initial['image_url'] = 'https://www.hitpromo.net/imageManager/show/ZBOX-MINCEREAL_blank2.jpg'
        self.fields['image_url'].widget = forms.HiddenInput()
