import os


def check_file_content_type(image_data):
    """
    This function will take image details and check if its content type is whitelisted or not.
    Based on that it will raise exception

    :param image_data:
    :return:True or None
    """
    if image_data.content_type in os.getenv('ALLOWED_CONTENT_TYPES'):
        return True
