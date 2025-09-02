import os
from re import U
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Start project: Migrate and Create Super User"

    def handle(self, *args, **aptions):
        self.stdout.write(self.style.WARNING("Running migrations..."))
        call_command("makemigrations", interactive=False)
        call_command("migrate", interactive=False)

        self.stdout.write(self.style.WARNING("Create superuser..."))
        User = get_user_model()

        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@exemplo.com")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin")


        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS("Superuser created!"))
        else:
            self.stdout.write(self.style.NOTICE("Superuser already exists!"))
