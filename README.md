# Image Uploading to Bucket in Google Cloud Storage

This project will take File from user end and store that file in Google Cloud Storage Bucket.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Things that you need to install for the project and how to install them.
```
Python >= 3.8
pip install fastapi
pip install uvicorn
```

### Prerequisites for Google Cloud Storage
* Create a Project in GCS
* After creating project create a bucket and use that bucket name in "BUCKET_NAME" of .env file.
* For Authentication
  * Go to Service Account from the left side menubar in IAM & Admin.
  * Create Service Account and after creating it click on Action
  * In Action go to Manage Keys and create a key.
  * From that download a json file.
  * Put that json file in "gcs_json_credentials" folder in project and use that json file name in "GCS_AUTHENTICATION_FILENAME" of .env file.

### Installing
A step by step series of examples that tell you how to get a development env running.
```
python3 -m env /path/to/new/virtual/environment
cd /path/to/environment
source env/bin/activate
pip install -r requirements.txt
```

### Running the application
How to run the application locally.
```
python main.py
```


### API Endpoints

List the API endpoints with a brief description of what they do.
```
GET /get-images - Retrieves a list of images from Google Cloud Storage Bucket
POST /store-image - Stores an image in Google Cloud Storage Bucket
DELETE /delete-image/{file_name} - Delete an image from Google Cloud Storage Bucket using its File name
```

### Postman Collection Link
```
https://api.postman.com/collections/17096834-a9368080-d3f7-4d8b-ac15-c81696e6c62f?access_key=PMAT-01GRK4DGKW301ZRWJ3BAV2YGZX
```

### Built with

* [FastAPI](https://fastapi.tiangolo.com/ "FastAPI") - The web framework used
* [Google Cloud Storage](https://console.cloud.google.com/storage "Google Cloud Storage") - Image Storage facility
