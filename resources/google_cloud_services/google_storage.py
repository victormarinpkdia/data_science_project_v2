from google.cloud.storage import Client

from security.google_cloud_credentials import IGoogleCloudCredentials


class GoogleStorage:
    def __init__(
        self,
        google_credentials: IGoogleCloudCredentials,
    ):
        self._storage_client: Client = Client.from_service_account_info(
            info=google_credentials.get_credentials()
        )

    def get_client(self) -> Client:
        return self._storage_client
