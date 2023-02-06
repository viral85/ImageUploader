from dotenv import load_dotenv
from fastapi import APIRouter, UploadFile
from starlette import status
from starlette.responses import JSONResponse
from google.cloud.exceptions import NotFound, GatewayTimeout, GoogleCloudError

from common.constants import (SOMETHING_WENT_WRONG, FETCHED_SUCCESSFULLY, IMAGE, UPLOADED_SUCCESSFULLY,
                              DELETED_SUCCESSFULLY, IMAGES, GCS_CLIENT_AUTHENTICATION_ERROR, ACCESSING_GCS_BUCKET_ERROR,
                              GCS_GATEWAY_TIMEOUT_ERROR, GCS_ERROR, GENERAL_EXCEPTION, FILE_NOT_FOUND_IN_GCS)
from common.response import ApiResponse
from file_upload.service.file_upload_services import FileUploadServices
from utils.logging import app_logger

load_dotenv()
router = APIRouter()


@router.get('/get-images')
def api_list_images() -> JSONResponse:
    """
    API will fetch all the images from Google Cloud Storage Bucket.

    :return: List of images in Json Response
    """
    success = False
    message = SOMETHING_WENT_WRONG
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    image_data = None
    try:
        file_upload_service_obj = FileUploadServices()
        image_data = file_upload_service_obj.get_image_list()
        success = True
        message = FETCHED_SUCCESSFULLY.format(image=IMAGES)
        status_code = status.HTTP_200_OK
    except TypeError as e:
        message = GCS_CLIENT_AUTHENTICATION_ERROR.format(e=e)
        app_logger.error(message)
    except NotFound as e:
        message = ACCESSING_GCS_BUCKET_ERROR.format(e=e)
        app_logger.error(message)
    except GatewayTimeout as e:
        message = GCS_GATEWAY_TIMEOUT_ERROR.format(e=e)
        app_logger.error(message)
    except GoogleCloudError as e:
        message = GCS_ERROR.format(e=e)
        app_logger.error(message)
    except Exception as e:
        app_logger.error(GENERAL_EXCEPTION.format(e=e))

    return ApiResponse.create_response(success=success, message=message, status_code=status_code, data=image_data)


@router.post('/store-image')
def api_store_images(file: UploadFile) -> JSONResponse:
    """
    This function will get Image data from the user and Upload it on Google Cloud Storage Bucket

    :param file: Get Image data
    :return: if any error occurs then exception will be raised and send appropriate error message
    and if not then send success message
    """

    success = False
    message = SOMETHING_WENT_WRONG
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    try:
        file_upload_service_obj = FileUploadServices()
        file_upload_service_obj.upload_files(file_data=file)
        success = True
        message = UPLOADED_SUCCESSFULLY.format(image=IMAGE)
        status_code = status.HTTP_200_OK
    except TypeError as e:
        message = GCS_CLIENT_AUTHENTICATION_ERROR.format(e=e)
        app_logger.error(message)
    except NotFound as e:
        message = ACCESSING_GCS_BUCKET_ERROR.format(e=e)
        app_logger.error(message)
    except GatewayTimeout as e:
        message = GCS_GATEWAY_TIMEOUT_ERROR.format(e=e)
        app_logger.error(message)
    except GoogleCloudError as e:
        message = GCS_ERROR.format(e=e)
        app_logger.error(message)
    except ValueError as e:
        status_code = status.HTTP_400_BAD_REQUEST
        app_logger.error(e)
        message = str(e)
    except Exception as e:
        app_logger.error(GENERAL_EXCEPTION.format(e=e))
    return ApiResponse.create_response(success=success, message=message, status_code=status_code)


@router.delete('/delete-image/{file_name}')
def delete_images(file_name: str) -> JSONResponse:
    success = False
    message = SOMETHING_WENT_WRONG
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    try:
        file_upload_service_obj = FileUploadServices()
        file_upload_service_obj.delete_file(file_name=file_name)
        success = True
        message = DELETED_SUCCESSFULLY.format(image=IMAGE)
        status_code = status.HTTP_200_OK
    except TypeError as e:
        message = GCS_CLIENT_AUTHENTICATION_ERROR.format(e=e)
        app_logger.error(message)
    except NotFound as e:
        message = FILE_NOT_FOUND_IN_GCS.format(e=e)
        app_logger.error(message)
    except GatewayTimeout as e:
        message = GCS_GATEWAY_TIMEOUT_ERROR.format(e=e)
        app_logger.error(message)
    except GoogleCloudError as e:
        message = GCS_ERROR.format(e=e)
        app_logger.error(message)
    except Exception as e:
        app_logger.error(GENERAL_EXCEPTION.format(e=e))
    return ApiResponse.create_response(success=success, message=message, status_code=status_code)
