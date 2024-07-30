from django.core.management import call_command
import threading


class RunningScrapingThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        call_command("running_scraping")
