from django.db import models

from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField


# Tag models, many to many relationship with guide
class Tag(models.Model):

    tag = models.CharField(
        'Tag',
        max_length=200,
    )
    
    color_class = models.CharField(
        'Bootstrap color class',
        max_length=200,
        choices=(
            ('label-default', 'label-default'),
            ('label-primary', 'label-primary'),
            ('label-success', 'label-success'),
            ('label-info', 'label-info'),
            ('label-warning', 'label-warning'),
            ('label-danger', 'label-danger'),           
        ),
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.tag

    class Meta:
        ordering = ('tag',)


# Category models, one to many relationship with guide
class Category(models.Model):

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    # Title of specialty
    category_name = models.CharField(
        'Nom de catégorie',
        max_length=300,
    )

    category_img = FilerFileField(blank=True, null=True, related_name='img')

    def __str__(self):
        return self.category_name


# Main Guide model
class Guide(models.Model):

    guide_name = models.CharField(
        'Nom du guide',
        max_length=300,
    )

    description = models.TextField(
        'Description du guide',
    )

    document = FilerFileField(blank=True, null=True, related_name="guides")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="guides")

    tag = models.ManyToManyField(Tag, blank=True, related_name="guides")

    author = models.TextField(
        'Auteur du guide',
        blank=True,
    )

    def __str__(self):
        return self.guide_name
