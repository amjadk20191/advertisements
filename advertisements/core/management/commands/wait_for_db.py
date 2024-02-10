import time

from psycopg2 import OperationalError as Psycopg2OpError
import os
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
import psycopg2


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                # self.check(databases=['default'])
                psycopg2.connect(
                    dbname=os.environ.get('DB_NAME'),
                    user=os.environ.get('DB_USER'),
                    password=os.environ.get('DB_PASS'),
                    host=os.environ.get('DB_HOST'),
                    port=os.environ.get('DB_PORT'),
                )
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
