from datetime import datetime


def create_custom_file_name(file_name: str) -> str:
    split_file_name = file_name.split('.')
    add_timestamp_to_file_name = f"{split_file_name[0]}_{int(datetime.now().timestamp())}."
    return add_timestamp_to_file_name + split_file_name[1]
