from material.serializers import ListMaterialSerializer
from rest_framework import serializers
from rest_framework.exceptions import APIException
from company.serializers import CompanySerializer
from info_collect.models import InfoCollect
from users.serializers import UserSerializer


class UniqueValidationError(APIException):
    status_code = 422


class InfoCollectSerializer(serializers.ModelSerializer):
    materials = ListMaterialSerializer(read_only=True)
    user_id = UserSerializer(read_only=True)
    company_id = CompanySerializer(read_only=True)
    class Meta:
        model = InfoCollect
        fields = ["id", "user_id", "localization", "material", "company_id"]
        read_only_fields = ["id","user_id","material","company_id"]


    def create(self, validated_data):
        info_collect = InfoCollect.objects.create(**validated_data)

        return info_collect