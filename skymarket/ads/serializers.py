from rest_framework import serializers

from skymarket.ads.models import Comment, Ad
#from ads.models import Comment, Ad

# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description", )


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
