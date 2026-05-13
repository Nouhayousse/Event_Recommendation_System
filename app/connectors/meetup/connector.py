from playwright.sync_api import sync_playwright

from app.services.cache_service import is_event_cached
from app.utils.url_utils import clean_url

class MeetupConnector:

    CATEGORY_IDS = {
        "hobbies-passions": 571,
        "sports-fitness": 482,
        "career-business": 405,
        "technology": 546,
        "science-education": 436,
        "arts-culture": 521,
        "writing": 467
    }

    BASE_URL = (
        "https://www.meetup.com/find/"
        "?categoryId={category_id}"
        "&source=EVENTS"
    )

    def fetch_events(self):

        all_events = []

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
             )

            page = browser.new_page()

            for category_name, category_id in self.CATEGORY_IDS.items():

                print(f"\nFetching: {category_name}")

                url = self.BASE_URL.format(
                category_id=category_id
                )

                page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000
                )

                page.wait_for_timeout(5000)

                cards = page.locator(
                '[data-testid="categoryResults-eventCard"]'
                )

                count = cards.count()

                print(f"Found {count} cards")

                for i in range(count):

                    card = cards.nth(i)

                    try:

                        title = card.locator("h3").inner_text()

                        event_url = card.locator(
                        "a"
                        ).first.get_attribute("href")

                        cleaned_url = clean_url(event_url)

                        # Check cache before proceeding
                        if is_event_cached(
                            "meetup",
                            cleaned_url
                        ):
                            print(f"Skipping cached event: {event_url}")
                            continue

                        date = card.locator(
                            "time"
                        ).get_attribute("datetime")

                        image_url = card.locator(
                            "img"
                        ).first.get_attribute("src")

                        is_online = (
                        "Online" in card.inner_text()
                        )

                        event = {
                         "title": title,
                         "url": cleaned_url,
                         "date": date,
                         "image_url": image_url,
                         "is_online": is_online,
                         "category": category_name
                        }

                        print(event)

                        all_events.append(event)

                    except Exception as e:

                        print(f"Error parsing card: {e}")

            browser.close()

        return all_events