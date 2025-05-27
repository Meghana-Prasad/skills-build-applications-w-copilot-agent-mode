from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserView(APIView):
    def get(self, request):
        return Response({"message": "List of users"}, status=status.HTTP_200_OK)

class TeamView(APIView):
    def get(self, request):
        return Response({"message": "List of teams"}, status=status.HTTP_200_OK)

class ActivityView(APIView):
    def get(self, request):
        return Response({"message": "List of activities"}, status=status.HTTP_200_OK)

class LeaderboardView(APIView):
    def get(self, request):
        return Response({"message": "Leaderboard"}, status=status.HTTP_200_OK)

class WorkoutView(APIView):
    def get(self, request):
        return Response({"message": "List of workouts"}, status=status.HTTP_200_OK)
