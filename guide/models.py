from django.db import models
from filer.fields.file import FilerFileField


# Tag models, many to many relationship with guide
class Tag(models.Model):

    tag = models.CharField(
        'Tag',
        max_length=200,
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

    def __str__(self):
        return self.category


# Main Guide model
class Guide(models.Model):

    guide_name = models.CharField(
        'Nom du guide',
        max_length=300,
    )

    description = models.TextField(
        'Description du guide',
    )

    document = FilerFileField(related_name="guide_documents")

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    tag = models.ManyToManyField(Tag, blank=True)

    author = models.TextField(
        'Auteur du guide',
        blank=True,
    )

    def __str__(self):
        return self.category
