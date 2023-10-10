from google.cloud.vision_v1 import ImageAnnotatorClient

from security.google_cloud_credentials import IGoogleCloudCredentials


class GoogleImageAnnotator:
    def __init__(
        self,
        google_credentials: IGoogleCloudCredentials,
    ):
        self._image_annotator_client: ImageAnnotatorClient = (
            ImageAnnotatorClient.from_service_account_info(
                info=google_credentials.get_credentials()
            )
        )

    def get_client(self) -> ImageAnnotatorClient:
        return self._image_annotator_client
