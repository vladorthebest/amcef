from rest_framework import serializers
from main.models import UserPost

class PostSerializer(serializers.ModelSerializer):


    id = serializers.IntegerField()

    def create(self, validated_data):
        instance = UserPost.objects.create(**validated_data)
        instance.id = validated_data.get('id')
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.body = validated_data.get("body", instance.body)
        instance.save()
        return instance

    class Meta:
        model = UserPost
        fields = '__all__'

