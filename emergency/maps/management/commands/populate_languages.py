from django.core.management.base import BaseCommand, CommandError

from ...models import Language

LANGUAGES = (
    # Name (in english for now), ISO 639-3 code
    ('English', 'ENG'),
    ('Spanish', 'SPA'),
    ('Thai', 'THA'),
)


class Command(BaseCommand):
    help = 'Populate Languages model from source data.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            dest='clear',
            default=False,
            help='Clear all existing Languages from database before population'
        )

    def handle(self, *args, **options):
        if options['clear']:
            Language.objects.all().delete()

        langs = [Language(name=name, code=code) for name, code in LANGUAGES]

        Language.objects.bulk_create(langs)

        self.stdout.write(
            self.style.SUCCESS('Successfully generated %s Languages' % len(LANGUAGES))
)
