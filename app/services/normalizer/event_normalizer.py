from dateutil import parser

def normalize_date(raw_date):

    if not raw_date:
        return None

    try:

        parsed_date = parser.parse(raw_date)

        return parsed_date.isoformat()

    except Exception:

        return None
    





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

def normalize_title(title):

    if not title:
        return None

    return title.strip()


def normalize_category(raw_category):

    if not raw_category:
        return "other"

    raw_category = raw_category.lower()

    for internal_cat, aliases in (
        INTERNAL_CATEGORIES.items()
    ):

        if raw_category in aliases:
            return internal_cat

    return "other"


def normalize_event(raw_event):

    normalized_event = {

        "external_id": raw_event.get(
            "event_id"
        ),

        "title": normalize_title(
            raw_event.get("title")
        ),

        "url": raw_event.get("url"),

        "date": normalize_date(
            raw_event.get("date")
        ),

        "category": normalize_category(
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