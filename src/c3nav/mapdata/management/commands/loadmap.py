from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from c3nav.mapdata.lastupdate import set_last_mapdata_update
from c3nav.mapdata.packageio import MapdataReader


class Command(BaseCommand):
    help = 'Load the map package files into the database'

    def add_arguments(self, parser):
        parser.add_argument('--yes', '-y', action='store_const', const=True, default=False,
                            help='don\'t ask for confirmation')

    def handle(self, *args, **options):
        reader = MapdataReader()
        reader.read_packages()

        with set_last_mapdata_update():
            with transaction.atomic():
                reader.apply_to_db()
                print()
                if not options['yes'] and input('Confirm (y/N): ') != 'y':
                    raise CommandError('Aborted.')
