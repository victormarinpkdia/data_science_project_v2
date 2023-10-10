from abc import ABC, abstractmethod
from typing import Dict


class IGoogleCloudCredentials(ABC):
    @abstractmethod
    def get_credentials(self) -> Dict:
        ...
