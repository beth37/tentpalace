import os
import json  # Add this import statement
from django.core.management import BaseCommand
from tentpalace.settings import BASE_DIR
from main_app.models import Customer


class Command(BaseCommand):
    help = "populates database with test data from a json file"

    def handle(self, *args, **options):
        path = os.path.join(BASE_DIR, 'customers.json')
        print(path)
        self.stdout.write(
            self.style.SUCCESS('Started to inject data')
        )

        with open(path) as file:
            customers = json.load(file)
            for customer in customers:
                Customer.objects.create(
                    first_name=customer['first_name'],
                    last_name=customer['last_name'],
                    email=customer['email'],
                    phone=customer['phone'],

                    profile_pic="students/profile.png"
                )

        self.stdout.write(
            self.style.SUCCESS('Completed injecting data')
        )
