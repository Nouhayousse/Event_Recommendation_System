import requests
from bs4 import BeautifulSoup

from app.connectors.base_connector import BaseConnector
from app.services.cache_service import (
    is_event_cached,
    cache_event
)


class EventbriteConnector(BaseConnector):

    BASE_URL = "https://www.eventbrite.fr/d/online/seminars/"

    def fetch_events(self):

        print("Fetching Eventbrite events")

        response = requests.get(self.BASE_URL)

        print(response.status_code)

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        event_cards = soup.select(
            'div[data-testid="search-event"]'
        )

        print(f"Found {len(event_cards)} events")

        events = []

        for card in event_cards:

            # -------------------------
            # Extract basic data first
            # -------------------------

            link_element = card.find(
                "a",
                href=True
            )

            if not link_element:
                continue

            url = link_element["href"]

            # -------------------------
            # Cache check
            # -------------------------

            if is_event_cached(
                "eventbrite",
                url
            ):
                print(f"Skipping cached event: {url}")
                continue

            # -------------------------
            # Continue extraction
            # -------------------------

            title_element = card.find("h3")

            if not title_element:
                continue

            title = title_element.get_text(
                strip=True
            )

            image_element = card.find("img")

            image_url = (
                image_element.get("src")
                if image_element
                else None
            )

            event_id = link_element.get(
                "data-event-id"
            )

            location_type = link_element.get(
                "data-event-location"
            )

            category = link_element.get(
                "data-event-category"
            )

            date_element = title_element.find_next(
                "p"
            )

            date = (
                date_element.get_text(strip=True)
                if date_element
                else None
            )

            event_data = {
                "title": title,
                "url": url,
                "date": date,
                "event_id": event_id,
                "location_type": location_type,
                "category": category,
                "image_url": image_url
            }

            

            events.append(event_data)

        return events

    def normalize_event(self, raw_event):
        pass