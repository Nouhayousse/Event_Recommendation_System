from abc import ABC, abstractmethod

class BaseConnector(ABC):

    @abstractmethod
    def fetch_events(self):
        pass

    @abstractmethod
    def normalize_event(self, raw_event):
        pass