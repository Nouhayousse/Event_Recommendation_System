import re
from datetime import datetime, timedelta
from dateutil import parser
from zoneinfo import ZoneInfo
import pytz


TZINFOS = {

    "EDT": -4 * 3600,
    "EST": -5 * 3600,

    "PDT": -7 * 3600,
    "PST": -8 * 3600,

    "CDT": -5 * 3600,
    "CST": -6 * 3600,

    "MDT": -6 * 3600,
    "MST": -7 * 3600,
}


INTERNAL_CATEGORIES = {

    "technology": [
        "science-and-tech",
        "tech",
        "computer-science",
        "AI",
        "machine-learning",
        "data",
        "programming",
        "software-development",
        "hardware",
        "cybersecurity",
        "blockchain",
        "cryptocurrency",
        "web-development",
        "mobile-development",
        "cloud-computing",
        "devops",
        "robotics",
        "virtual-reality",
        "augmented-reality",
        "gaming",
        "electronics"
    ],

    "career-business": [
        "business",
        "startup",
        "entrepreneurship",
        "finance",
        "marketing",
        "career-development",
        "networking",
        "professional-development",
        "leadership",
        "management",
        "sales",
        "product-management",
    ],

    "science-education": [
        "family-and-education",
        "education",
        "learning",
        "science",
        "math",
        "history",
        "language",
        "philosophy",
        "psychology",
        "health-and-wellness",
        "biology",
        "chemistry",
        "school"
    ],

    "arts-culture": [
        "arts",
        "design",
        "music",
        "photography",
        "writing",
        "film",
        "theater",
        "literature",
        "culture"
    ]
}


class EventbriteNormalizer:

 def normalize_date(self, raw_date):

    if not raw_date:
        return None

    try:

        cleaned = raw_date.strip()

        cleaned = re.sub(
            r"\+\s*\d+\s*en plus",
            "",
            cleaned
        )

        if "Today" in cleaned:
            today= datetime.now().strftime("%Y-%m-%d")
            cleaned = cleaned.replace("Today", today)
        if "Tomorrow" in cleaned:
            tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            cleaned = cleaned.replace("Tomorrow", tomorrow)    

        parsed_date = parser.parse(
            cleaned,
            fuzzy=True,
            tzinfos=TZINFOS
        )

        morocco_timezone = ZoneInfo(
            "Africa/Casablanca"
        )

        if parsed_date.tzinfo is None:

            parsed_date = parsed_date.replace(
                tzinfo=morocco_timezone
            )

        else:

            parsed_date = parsed_date.astimezone(
                morocco_timezone
            )

        return parsed_date

    except Exception as e:

        print(
            f"Date normalization error: {e}"
        )

        return None

 def normalize_title(self, title):

        if not title:
            return None

        return title.strip()

 def normalize_category(self, raw_category):

        if not raw_category:
            return "other"

        raw_category = raw_category.lower()

        for internal_cat, aliases in (
            INTERNAL_CATEGORIES.items()
        ):

            if raw_category in aliases:
                return internal_cat

        return "other"

 def normalize_event(self, raw_event):

        normalized_event = {

            "external_id": raw_event.get(
                "event_id"
            ),

            "title": self.normalize_title(
                raw_event.get("title")
            ),

            "url": raw_event.get("url"),

            "date": self.normalize_date(
                raw_event.get("date")
            ),

            "category": self.normalize_category(
                raw_event.get("category")
            ),

            "source_category": raw_event.get(
                "category"
            ),

            "location_type": raw_event.get(
                "location_type"
            ),

            "image_url": raw_event.get(
                "image_url"
            ),

            "source_platform": "eventbrite"
        }

        return normalized_event