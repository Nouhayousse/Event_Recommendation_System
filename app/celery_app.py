from celery import Celery

celery_app = Celery(
    "tamtrack",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=[
        "app.tasks.meetup_tasks",
        "app.tasks.eventbrite_tasks",
        "app.tasks.maintenance_tasks"
    ]
)

celery_app.conf.timezone = "Africa/Casablanca"

celery_app.conf.beat_schedule = {
    "scrape-meetup-every-6-hours": {
        "task": "app.tasks.meetup_tasks.scrape_meetup_task",
        "schedule": 6 * 3600.0,
    },

    "mark-expired-seminars-daily": {
        "task": "app.tasks.seminar_tasks.mark_expired_seminars_task",
        "schedule": 86400.0,
    },
    "scrape-eventbrite-every-6-hours": {
        "task": "app.tasks.eventbrite_tasks.scrape_eventbrite_task",
        "schedule": 6 * 3600.0,     
    }    
}   