from rest_framework import serializers

class studentserializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=70)
    last_name = serializers.CharField(max_length=70)
    roll_no = serializers.IntegerField
    ph_no = serializers.IntegerField