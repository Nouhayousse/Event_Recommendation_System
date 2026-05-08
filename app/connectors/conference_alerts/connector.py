from app.connectors.base_connector import BaseConnector

class ConferenceAlertsConnector(BaseConnector):

    def fetch_events(self):
        print("Fetching Conference Alerts events")

    def normalize_event(self, raw_event):
        pass