from django.db import models
from django.template.defaultfilters import slugify

class Phone(models.Model):
    name = models.CharField(max_length=40, null=False, unique=True)
    price = models.FloatField(null=False)
    image = models.URLField(null=False)
    release_date = models.DateField(null=False)
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(max_length=40, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.name)
        return super().save()