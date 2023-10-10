from abc import ABC, abstractmethod


class IImageObjectsLocalizationService(ABC):
    @abstractmethod
    def localize_objects(self, *args, **kwargs):
        pass
