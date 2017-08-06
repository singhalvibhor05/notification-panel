from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from .models import Notifications, User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username')

class NotificationsSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Notifications
        fields = ('header', 'content', 'image_url', 'created_at', 'modified_at',
                  'users')
        read_only_fields = ('created_at', 'modified_at',)

        def create(self, validated_data):
            return Notifications.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.header = validated_data.get('header', instance.header)
            instance.content = validated_data.get('content', instance.content)
            instance.image_url = validated_data.get('image_url', instance.image_url)
            instance.save()

            return instance
