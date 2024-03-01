from rest_framework import serializers
from .models import Client
from rest_framework.validators import ValidationError


class ClientSerializers(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"

    def validate(self, attrs):
        name = attrs["name"]

        client = Client.objects.filter(name=name).exists()
        if client:
            raise ValidationError("The Client Name Already Exists")

        return super().validate(attrs)
