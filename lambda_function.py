import boto3
from PIL import Image
import os
import urllib.parse

s3 = boto3.client("s3")

DESTINATION_BUCKET = "processed-thumbnails-aakansh-2026"

def lambda_handler(event, context):
    record = event["Records"][0]

    source_bucket = record["s3"]["bucket"]["name"]
    object_key = urllib.parse.unquote_plus(
        record["s3"]["object"]["key"]
    )

    download_path = "/tmp/original.jpg"
    upload_path = "/tmp/thumbnail.jpg"

    s3.download_file(source_bucket, object_key, download_path)

    with Image.open(download_path) as image:
        image = image.convert("RGB")
        image = image.resize((128, 128))
        image.save(upload_path, "JPEG")

    s3.upload_file(
        upload_path,
        DESTINATION_BUCKET,
        object_key,
        ExtraArgs={"ContentType": "image/jpeg"}
    )

    print(f"Thumbnail created successfully: {object_key}")

    return {
        "statusCode": 200,
        "body": "Thumbnail created successfully"
    }
