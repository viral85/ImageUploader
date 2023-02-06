import os

from dotenv import load_dotenv
from fastapi import UploadFile
from google.cloud import storage

from utils.custom_file_name import create_custom_file_name

load_dotenv()


class GoogleCloudStorageService:
    @classmethod
    def create_gcs_client(cls):
        return storage.Client.from_service_account_json(
            f"gcs_json_credentials/{os.getenv('GCS_AUTHENTICATION_FILENAME')}")

    @classmethod
    def get_gcs_bucket_detail(cls):
        storage_client = cls.create_gcs_client()
        return storage_client.get_bucket(os.getenv('BUCKET_NAME'))

    @classmethod
    def upload_file_in_gcs_bucket(cls, file_data: UploadFile):
        """
        This Function will take file_data as parameters and create a bucket object with filename
        and upload file in the bucket

        :param file_data: File to be uploaded in GCS Bucket
        :return: None
        """
        bucket = cls.get_gcs_bucket_detail()

        # Creating an object of file in Bucket
        object_name_in_gcs_bucket = bucket.blob(create_custom_file_name(file_data.filename))

        # Uploading image from File to Google Cloud Storage Bucket
        return object_name_in_gcs_bucket.upload_from_file(file_data.file)
