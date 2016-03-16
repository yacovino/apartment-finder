from scraper import do_scrape
import settings
import time

while True:
    try:
        do_scrape()
    except Exception:
        pass
    time.sleep(settings.SLEEP_INTERVAL)
