from django.core.management.base import BaseCommand, CommandError
from ...models import User

class Command(BaseCommand):

    def __init__(self):
        super().__init__()
    

    def handle(self,*args,**options):
        
        for i in User.objects.all():
            if(i.username != "@admin" or i.username != "@aosman11" ):
                i.delete()