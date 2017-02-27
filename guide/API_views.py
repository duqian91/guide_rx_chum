from rest_framework import generics
from rest_framework import filters
import django_filters

from guide.models import Guide, Category, Tag
from guide.serializers import GuideSerializer, CategorySerializer


# API views
class GuideAPIFilter(filters.FilterSet):
    class Meta:
        model = Guide
        fields = ['category',]

    # to_field_name is used to specify which field to use
    category = rest_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        to_field_name='category_name',
    )



class GuideAPIList(generics.ListAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    filter_class = GuideAPIFilter

    filter_backends = (
        filters.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )

    # add fields to search for with icontain, need to implement AJAX search in frontend
    # for foreign key values, added __namefield from .models
    search_fields = (
        'guide_name',
        'category__category_name',
        'tag__tag',
    )
