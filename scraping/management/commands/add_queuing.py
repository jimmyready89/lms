from django.core.management.base import BaseCommand
from scraping.models import ScrapingQueue
from datetime import datetime
from scraping.RunningScrapingThread import RunningScrapingThread


class Command(BaseCommand):
    help = 'add queuing'

    def add_arguments(self, parser):
        parser.add_argument('comment', type=str, help='request comment')
        parser.add_argument('parameter', type=str, help='request parameter')

    def handle(self, *args, **options):
        comment = options['comment']
        parameter = options['parameter']

        scrapingQueueCount = ScrapingQueue.objects.filter(start_datetime=None).count()
        ScrapingQueue.objects.create(
            comment=comment,
            parameter=parameter,
            request_datetime=datetime.now()
        )

        if scrapingQueueCount == 0:
            RunningScrapingThread().start()

        return
