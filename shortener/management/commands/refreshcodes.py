from django.core.management.base import BaseCommand, CommandError

from shortener.models import kirrURL

class Command(BaseCommand):
    help = 'Refrehes all kirrURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return kirrURL.objects.refresh_shortcodes(items=options['items'])