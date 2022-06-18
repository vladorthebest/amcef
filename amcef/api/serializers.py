from rest_framework import serializers
from main.models import UserPost

class PostSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.body = validated_data.get("title", instance.body)
        instance.save()
        return instance

    class Meta:
        model = UserPost
        fields = '__all__'

