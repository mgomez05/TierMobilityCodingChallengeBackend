from .models import ShortUrl
from rest_framework.serializers import ModelSerializer

class ShortUrlSerializer(ModelSerializer):
    class Meta:

        model = ShortUrl
        fields = ['realUrl']
