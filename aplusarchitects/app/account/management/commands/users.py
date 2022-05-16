from django.core.management.base import BaseCommand, CommandError
import unicodedata
from faker import Factory
import random
import datetime
from ...models import User

fake = Factory.create()
NUM_USERS = 100


def get_email(first_name, last_name):
    _first = unicodedata.normalize(
        'NFD', first_name).encode('ascii', 'ignore')
    _last = unicodedata.normalize(
        'NFD', last_name).encode('ascii', 'ignore')
    return '%s.%s@example.com' % (
        _first.lower().decode('utf-8'),
        _last.lower().decode('utf-8'),
    )


class Command(BaseCommand):
    help = 'Populate data for Users'

    def handle(self, *args, **options):
        for dummy in range(NUM_USERS):
            try:
                first_name = fake.first_name()
                last_name = fake.last_name()
                user = User.objects.create_user(
                    email=get_email(first_name, last_name),
                    first_name=first_name,
                    last_name=last_name,
                    date_of_birth=datetime.date.today(),
                    is_active=True,
                    is_staff=random.choice([True, False]),
                    password='1'
                )
                user.save()
                self.stdout.write(
                    self.style.SUCCESS('Created user: %s' % user.email)
                )
            except:
                self.stdout.write(
                    self.style.ERROR('Can not create user.')
                )
            
