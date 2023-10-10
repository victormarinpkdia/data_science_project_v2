from io import BytesIO

from google.cloud.exceptions import NotFound
from google.cloud.storage import Blob, Bucket

from .google_storage import GoogleStorage


class GoogleStorageBucket:
    def __init__(
        self,
        bucket_name: str,
        storage_client: GoogleStorage,
    ):
        self.name: str = bucket_name
        try:
            self._bucket: Bucket = storage_client.get_client().bucket(
                bucket_name
            )
        except NotFound as error:
            raise NotFound(f"The bucket {self.name} doesn't exist.") from error

    def _get_blob(
        self,
        blob_name: str,
    ) -> Blob:
        blob = self._bucket.get_blob(blob_name)
        if blob is None:
            raise NotFound(f"The blob {blob_name} doesn't exist.")
        return blob

    def download_blob(
        self,
        blob_name: str,
    ) -> BytesIO:
        return BytesIO(self._get_blob(blob_name).download_as_bytes())
