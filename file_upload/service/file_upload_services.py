import os
from typing import List, Dict, Any
from fastapi import UploadFile

from common.constants import INVALID_FILE_TYPE_MESSAGE
from common.validation import check_file_content_type
from utils.google_cloud_storage_services import GoogleCloudStorageService


class FileUploadServices:
    @classmethod
    def upload_files(cls, file_data: UploadFile) -> None:
        """
        This function will get file data and Upload it in Google Cloud Storage Bucket

        :param file_data: To get the File that has to be Upload in Google Cloud Storage
        :return: None
        """
        if not check_file_content_type(image_data=file_data):
            raise ValueError(INVALID_FILE_TYPE_MESSAGE.format(msg=os.getenv('ALLOWED_CONTENT_TYPES')))
        google_cloud_storage_obj = GoogleCloudStorageService()
        google_cloud_storage_obj.upload_file_in_gcs_bucket(file_data=file_data)

    @classmethod
    def get_image_list(cls) -> list[dict[str, str | Any]]:
        """
        This function will fetch all the images from Google Cloud Storage Bucket

        :return: List of Images
        """
        google_cloud_storage_obj = GoogleCloudStorageService()
        bucket_data = google_cloud_storage_obj.get_gcs_bucket_detail()
        blobs = bucket_data.list_blobs()
        bucket_files_data = []
        for blob in blobs:
            blob_details = bucket_data.get_blob(blob.name)
            bucket_files_data.append({"name": blob_details.name,
                                      "url": f"{os.getenv('GOOGLE_CLOUD_STORAGE_URL')}/{os.getenv('BUCKET_NAME')}/{blob_details.name}"})

        return bucket_files_data

    @classmethod
    def delete_file(cls, file_name: str) -> None:
        google_cloud_storage_obj = GoogleCloudStorageService()
        bucket = google_cloud_storage_obj.get_gcs_bucket_detail()
        blob = bucket.blob(file_name)
        blob.delete()
