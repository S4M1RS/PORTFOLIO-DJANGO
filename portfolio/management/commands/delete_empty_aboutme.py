from django.core.management.base import BaseCommand
from portfolio.models import Aboutme

class Command(BaseCommand):
    help = 'Deletes empty Aboutme instances'

    def handle(self, *args, **options):
        empty_aboutme_instances = Aboutme.objects.filter(hero=None)
        count = empty_aboutme_instances.count()

        empty_aboutme_instances.delete()

        self.stdout.write(self.style.SUCCESS(f'Deleted {count} empty Aboutme instances'))