from abc import ABC, abstractmethod
from io import BytesIO

from PIL.Image import Image as PillowImage


class IPIllowableImage(ABC):
    @abstractmethod
    def _create_pillow_image(self) -> PillowImage:
        ...

    def represent_as_bytes(self) -> bytes:
        raw_image = self._create_pillow_image()
        buffer = BytesIO()
        raw_image.save(buffer, format="jpeg")
        return buffer.getvalue()
