from django.core.management.base import BaseCommand
from scraping import create_drive, loginBinus
from time import sleep

class Command(BaseCommand):
    help = 'running scraping'

    def handle(self, *args, **options):
        driver = create_drive()
        loginBinus(driver)

        while True:
            sleep(10000)
