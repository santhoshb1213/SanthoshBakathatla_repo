from rest_framework import serializers

from my_awesome_project_copy.users.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }