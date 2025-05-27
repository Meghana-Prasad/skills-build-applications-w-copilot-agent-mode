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
            user = User(email=user_data['email'], name=user_data['name'], age=user_data['age'])
            user.save()

        # Populate Teams
        for team_data in data['teams']:
            team = Team(name=team_data['name'])
            team.save()
            members = User.objects.filter(email__in=team_data['members'])
            team.members.set(members)

        # Populate Activities
        for activity_data in data['activities']:
            user = User.objects.get(email=activity_data['user'])
            activity = Activity(user=user, activity_type=activity_data['type'], duration=activity_data['duration'])
            activity.save()

        # Populate Leaderboard
        for leaderboard_data in data['leaderboard']:
            user = User.objects.get(email=leaderboard_data['user'])
            leaderboard = Leaderboard(user=user, score=leaderboard_data['score'])
            leaderboard.save()

        # Populate Workouts
        for workout_data in data['workouts']:
            workout = Workout(name=workout_data['name'], description=workout_data['description'])
            workout.save()

        self.stdout.write(self.style.SUCCESS('Database populated successfully using Django ORM!'))