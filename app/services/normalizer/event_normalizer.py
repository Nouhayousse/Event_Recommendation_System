from dateutil import parser

def normalize_date(raw_date):

    if not raw_date:
        return None

    try:

        parsed_date = parser.parse(raw_date)

        return parsed_date.isoformat()

    except Exception:

        return None
    


print(
    normalize_date(
        "Fri, May 29, 12:30 PM GMT+2"
    )
)


print(
    normalize_date(
        "Monday at 6:00 PM GMT+1"
    )
)



INTERNAL_CATEGORIES = {

    "technology": [
        "science-and-tech",
        "tech",
        "computer-science",
        "ai",
        "machine-learning",
        "data"
    ],

    "business": [
        "business",
        "startup",
        "entrepreneurship",
        "finance"
    ],

    "education": [
        "family-and-education",
        "education",
        "learning"
    ],

    "arts": [
        "arts",
        "design",
        "music"
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