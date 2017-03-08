from rest_framework import serializers
from guide.models import Guide, Category, Tag
from django.utils import six


# Overrides the default model serializer foreign key relation
# So that it will return the string representation and not the primary key value
class MyPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):

    def to_representation(self, value):
        return six.text_type(value)

    def use_pk_only_optimization(self):
        return False


class GuideSerializer(serializers.ModelSerializer):

    category = MyPrimaryKeyRelatedField(queryset=Category.objects.all())
    tag = MyPrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    document_url = serializers.SerializerMethodField()
    category_img_url = serializers.SerializerMethodField()
    tag_color= serializers.SerializerMethodField()

    def get_category_img_url(self, obj):
        return obj.category.category_img.url

    def get_document_url(self, obj):
        return obj.document.url

    def get_tag_color(self, obj):
        return obj.tag.color_class

    class Meta:
        model = Guide
        editable = False
        fields = (
            'guide_name',
            'description',
            'document_url',
            'category',
            'category_img_url',
            'tag',
            'tag_color',
            'author',
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        editable = False
        fields = (
            'category_name',
        )

