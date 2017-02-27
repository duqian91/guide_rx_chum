from rest_framework import serializers
from guide.models import Guide, Category


class GuideSerializer(serializers.ModelSerializer):

    document_url = serializers.SerializerMethodField()

    def get_document_url(self, obj):
        return obj.document.url

    class Meta:
        model = Guide
        editable = False
        fields = (
            'guide_name',
            'description',
            'document',
            'category',
            'tag',
            'author',
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        editable = False
        fields = (
            'category_name',
        )

