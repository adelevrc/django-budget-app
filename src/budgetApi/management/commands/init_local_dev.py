from django.contrib.auth.models import User
from django.core.management import BaseCommand

from budgetApi.models import Category

ADMIN_ID = 'admin'
ADMIN_PASSWORD = '12345678!'

CATEGORIES = [
    {
        'name': 'Animaux',
        'description': "tout pour nos petites bêtes "
    },
    {
        'name': 'Banques / Assurance',
        'description': "Pour contribuer au capitalisme "
    },
    {
        'name': 'Loisirs',
        'description': "Il n'y a pas de honte à se faire du mal"
    }
]


class Command(BaseCommand):
    help = 'Initialize project for local development'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING(self.help))

        Category.objects.all().delete()

        for data_category in CATEGORIES:
            Category.objects.create(name=data_category['name'],
                                    description=data_category['description'])

        User.objects.create_superuser(ADMIN_ID, 'admin@oc.drf', ADMIN_PASSWORD)
        self.stdout.write(self.style.SUCCESS("All Done !"))
