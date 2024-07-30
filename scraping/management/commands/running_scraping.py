from django.core.management.base import BaseCommand
from scraping.function import BrowserConnection
# , loginBinus
from scraping.function.utilty import next_free_port
# from scraping.function.functional import ChangeApp
# from scraping.function.content import PeriodList, CourseList, CollectStudentList, CollectLecturersList, CollectGroup
from playwright.sync_api import sync_playwright
from scraping.models import ScrapingQueue, ScrapingBrowser
from time import sleep
from datetime import datetime
import json


class Command(BaseCommand):
    help = 'running scraping'

    def handle(self, *args, **options):
        browserConfig = ScrapingBrowser.objects.first()
        if browserConfig is None:
            Port = next_free_port(9800)

            browserConfig = ScrapingBrowser.objects.create(
                port=Port
            )

        while True:
            scrapingQueue = ScrapingQueue.objects\
                .filter(start_datetime=None)\
                .first()

            if scrapingQueue is not None:
                scrapingQueue.start_datetime = datetime.now()
                scrapingQueue.save()

                response = {
                    "status": True,
                    "message": [],
                    "data": {}
                }

                try:
                    with sync_playwright() as playwright:
                        browserConnection = BrowserConnection(playwright, browserConfig.port)
                        print(browserConnection)
                        # loginStatus = loginBinus(browserConnection)
                        # if loginStatus is False:
                        #     raise Exception("Login Failed")

                        # changeAppStatus = ChangeApp(browserConnection, "LMS")
                        # if changeAppStatus is False:
                        #     raise Exception("App Status Failed")

                        # print(PeriodList(browserConnection))

                        # print(CourseList(browserConnection))

                        # print(CollectStudentList(browserConnection, "https://newbinusmaya.binus.ac.id/lms/course/74318d36-6117-4341-b01b-5432abe93028"))

                        # print(CollectLecturersList(browserConnection, "https://newbinusmaya.binus.ac.id/lms/course/74318d36-6117-4341-b01b-5432abe93028"))

                        # print(CollectGroup(browserConnection, "https://newbinusmaya.binus.ac.id/lms/course/74318d36-6117-4341-b01b-5432abe93028"))
                except Exception as e:
                    response.status = False
                    response.message = e

                scrapingQueue.response = json.dumps(response)
                scrapingQueue.end_datetime = datetime.now()
                scrapingQueue.save()
            else:
                break

            sleep(2)
