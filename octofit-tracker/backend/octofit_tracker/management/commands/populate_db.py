import json
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = "Populate the database with test data using Django ORM"

    def handle(self, *args, **kwargs):
        with open('octofit_tracker/test_data.json', 'r') as file:
            data = json.load(file)

        # Populate Users
        for user_data in data['users']:
            User.objects.create(email=user_data['email'], name=user_data['name'], age=user_data['age'])

        # Populate Teams
        for team_data in data['teams']:
            team = Team.objects.create(name=team_data['name'])
            members = User.objects.filter(email__in=team_data['members'])
            for member in members:
                team.members.add(member)

        # Populate Activities
        for activity_data in data['activities']:
            user = User.objects.get(email=activity_data['user'])
            Activity.objects.create(user=user, activity_type=activity_data['type'], duration=activity_data['duration'])

        # Populate Leaderboard
        for leaderboard_data in data['leaderboard']:
            user = User.objects.get(email=leaderboard_data['user'])
            Leaderboard.objects.create(user=user, score=leaderboard_data['score'])

        # Populate Workouts
        for workout_data in data['workouts']:
            Workout.objects.create(name=workout_data['name'], description=workout_data['description'])

        self.stdout.write(self.style.SUCCESS('Database populated successfully using Django ORM!'))