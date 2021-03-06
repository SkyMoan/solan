from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('email','ntnu_username','first_name', 'last_name', 'bio', 'member', 'photo')
