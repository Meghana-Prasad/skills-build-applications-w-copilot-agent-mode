import json
import pymongo
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = "Populate the database with test data using pymongo"

    def handle(self, *args, **kwargs):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        with open('octofit_tracker/test_data.json', 'r') as file:
            data = json.load(file)

        # Populate Users
        db.users.insert_many(data['users'])

        # Populate Teams
        for team_data in data['teams']:
            team_data['members'] = list(db.users.find({"email": {"$in": team_data['members']}}, {"_id": 1}))
            db.teams.insert_one(team_data)

        # Populate Activities
        for activity_data in data['activities']:
            activity_data['user'] = db.users.find_one({"email": activity_data['user']}, {"_id": 1})
            db.activities.insert_one(activity_data)

        # Populate Leaderboard
        for leaderboard_data in data['leaderboard']:
            leaderboard_data['user'] = db.users.find_one({"email": leaderboard_data['user']}, {"_id": 1})
            db.leaderboard.insert_one(leaderboard_data)

        # Populate Workouts
        db.workouts.insert_many(data['workouts'])

        self.stdout.write(self.style.SUCCESS('Database populated successfully using pymongo!'))