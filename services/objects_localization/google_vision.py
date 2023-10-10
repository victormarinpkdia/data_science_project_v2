from typing import Any, Dict, Sequence, Union

from google.cloud.vision_v1 import (
    Image as GoogleVisionImage,
    ImageAnnotatorClient,
    ImageSource,
)

from images import GoogleImage, IPIllowableImage
from resources.google_cloud_services import GoogleImageAnnotator
from .objects_localization import IImageObjectsLocalizationService


class GoogleVisionImageObjectsLocalization(IImageObjectsLocalizationService):
    def __init__(self, image_annotator: GoogleImageAnnotator):
        self._image_annotator: ImageAnnotatorClient = (
            image_annotator.get_client()
        )

    def localize_objects(
        self,
        image: Union[IPIllowableImage, GoogleImage],
        point_format: bool = False,
        *args,
        **kwargs,
    ) -> Sequence[Dict[str, Any]]:
        google_vision_image: GoogleVisionImage
        if isinstance(image, GoogleImage):
            google_vision_image = GoogleVisionImage(
                source=ImageSource(image_uri=image.uri)
            )
        else:
            google_vision_image = GoogleVisionImage(
                content=image.represent_as_bytes()
            )
        raw_detected_objects = self._image_annotator.object_localization(
            image=google_vision_image
        ).localized_object_annotations
        detected_objects = [
            {
                "object_name": obj.name,
                "score": round(obj.score, 3),
                "bounding_poly": [
                    (round(nv.x, 3), round(nv.y, 3))
                    for nv in obj.bounding_poly.normalized_vertices
                ]
                if point_format
                else sum(
                    [
                        [round(nv.x, 3), round(nv.y, 3)]
                        for nv in obj.bounding_poly.normalized_vertices
                    ],
                    [],
                ),
            }
            for obj in raw_detected_objects
        ]
        unique_objects = [
            filter(
                lambda obj: obj["object_name"].lower() == obj_name.lower(),
                detected_objects,
            ).__next__()
            for obj_name in set(
                [obj["object_name"] for obj in detected_objects]
            )
        ]
        unique_objects.sort(key=lambda obj: obj["score"], reverse=True)
        return unique_objects
