from rest_framework import serializers
from .models import Students
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['firstname','lastname','age','school_name','created_at']
        read_only_fields = ['id','created_at']