import pymongo
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate the MongoDB database with test data using pymongo'

    def handle(self, *args, **kwargs):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        # Populate users collection
        users = db["users"]
        users.insert_many([
            {"email": "john.doe@example.com", "name": "John Doe", "age": 25},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 30}
        ])

        # Populate teams collection
        teams = db["teams"]
        teams.insert_one({"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]})

        # Populate activities collection
        activities = db["activity"]
        activities.insert_many([
            {"user_email": "john.doe@example.com", "activity_type": "Running", "duration": 30},
            {"user_email": "jane.smith@example.com", "activity_type": "Cycling", "duration": 45}
        ])

        # Populate leaderboard collection
        leaderboard = db["leaderboard"]
        leaderboard.insert_many([
            {"user_email": "john.doe@example.com", "score": 100},
            {"user_email": "jane.smith@example.com", "score": 150}
        ])

        # Populate workouts collection
        workouts = db["workouts"]
        workouts.insert_many([
            {"name": "Push-ups", "description": "Do 20 push-ups"},
            {"name": "Sit-ups", "description": "Do 30 sit-ups"}
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data using pymongo'))
