from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self,*args,**options):
        
        for  i  in range(100):
            first_name = self.faker.unique.first_name()
            last_name = self.faker.unique.last_name()
            User.objects.create_user(
                f'@{first_name}{last_name}',
                first_name = first_name,
                last_name = last_name,
                email = f'{first_name}{last_name}@example.org',
                password = self.faker.password(),
                bio = self.faker.sentences()
            )
        

