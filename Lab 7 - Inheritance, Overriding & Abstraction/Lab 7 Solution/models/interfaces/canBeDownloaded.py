from abc import ABC, abstractmethod

class CanBeDownloaded(ABC):
    
    @abstractmethod
    def get_download_size(self):
        pass