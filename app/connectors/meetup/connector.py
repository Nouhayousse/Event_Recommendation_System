from playwright.sync_api import sync_playwright


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