from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.EmailField())

class ActivitySerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    activity_type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
