import ast
import os
from typing import Dict, Optional

from .google_cloud_credentials import IGoogleCloudCredentials


class LocalGoogleCloudCredentials(IGoogleCloudCredentials):
    def __init__(self):
        google_credentials: Optional[str] = os.getenv(
            "GOOGLE_CLOUD_CREDENTIALS"
        )
        if not google_credentials:
            raise Exception(
                "The mandatory GOOGLE_CLOUD_CREDENTIALS environment variable "
                "isn't defined in the local .env file."
            )
        try:
            self._google_credentials: Dict = ast.literal_eval(
                google_credentials.replace("\n", "").replace("    ", "")
            )
        except ValueError as error:
            raise Exception(
                "The mandatory GOOGLE_CLOUD_CREDENTIALS environment variable "
                "isn't defined in string-as-dict format in the local "
                ".env file."
            ) from error

    def get_credentials(self) -> Dict:
        return self._google_credentials
