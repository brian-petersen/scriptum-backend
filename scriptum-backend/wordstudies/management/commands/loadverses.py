import json

from django.core.management.base import BaseCommand

from wordstudies.models import Verse


class Command(BaseCommand):
    help = 'Loads verses into the db'

    def add_arguments(self, parser):
        parser.add_argument('json_path', nargs='+')

    def handle(self, *args, **options):
        json_paths = options['json_path']

        for json_path in json_paths:
            self.stdout.write('Importing ' + json_path)

            with open(json_path) as json_file:
                data = json.load(json_file)
                json_verses = data['verses']

                for json_verse in json_verses:
                    verse = Verse()
                    verse.reference = json_verse['reference']
                    verse.text = json_verse['text']

                    verse.save()
