from PIL.Image import Image as PillowImage, open

from resources.google_cloud_services import GoogleStorageBucket
from .pillowable_image import IPIllowableImage


class GoogleImage(IPIllowableImage):
    def __init__(
        self,
        image_uri: str,
        bucket: GoogleStorageBucket,
    ):
        self.uri: str = image_uri
        self._bucket: GoogleStorageBucket = bucket
        self._image_blob_name: str = self.uri.split(
            f"gs://{self._bucket.name}/"
        )[-1]
        *gcs_folder_path, name = self._image_blob_name.split("/")
        self.name: str = name
        self.extension: str = self.name.split(".")[-1]
        self._folder: str = "/".join(gcs_folder_path)

    def _create_pillow_image(self) -> PillowImage:
        return open(self._bucket.download_blob(self._image_blob_name))

    def download(self) -> None:
        self._create_pillow_image().save(self.name)
