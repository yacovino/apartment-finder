from scraper import do_scrape
import settings
import time
import sys

if __name__ == "__main__":
    while True:
        try:
            do_scrape()
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception:
            pass
        time.sleep(settings.SLEEP_INTERVAL)
