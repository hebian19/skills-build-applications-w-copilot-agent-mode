
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Drop collections directly using pymongo
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db['users'].drop()
        db['teams'].drop()
        db['activities'].drop()
        db['leaderboard'].drop()
        db['workouts'].drop()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=timezone.now())
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=timezone.now())
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date=timezone.now())
        Activity.objects.create(user=clark, type='Yoga', duration=20, date=timezone.now())

        # Create Workouts
        Workout.objects.create(name='HIIT', description='High Intensity Interval Training', difficulty='Hard')
        Workout.objects.create(name='5K Run', description='5 Kilometer run', difficulty='Medium')
        Workout.objects.create(name='Stretching', description='Full body stretching routine', difficulty='Easy')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
