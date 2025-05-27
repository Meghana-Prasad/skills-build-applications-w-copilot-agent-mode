import json
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = "Populate the database with test data"

    def handle(self, *args, **kwargs):
        with open('octofit_tracker/test_data.json', 'r') as file:
            data = json.load(file)

        # Populate Users
        for user_data in data['users']:
            User.objects.get_or_create(email=user_data['email'], defaults={'name': user_data['name']})

        # Populate Teams
        for team_data in data['teams']:
            members = User.objects.filter(email__in=team_data['members'])
            team, created = Team.objects.get_or_create(name=team_data['name'])
            team.members.set(members)
            team.save()

        # Populate Activities
        for activity_data in data['activities']:
            user = User.objects.get(email=activity_data['user'])
            Activity.objects.get_or_create(user=user, type=activity_data['type'], duration=activity_data['duration'])

        # Populate Leaderboard
        for leaderboard_data in data['leaderboard']:
            user = User.objects.get(email=leaderboard_data['user'])
            Leaderboard.objects.get_or_create(user=user, score=leaderboard_data['score'])

        # Populate Workouts
        for workout_data in data['workouts']:
            Workout.objects.get_or_create(name=workout_data['name'], description=workout_data['description'])

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))