# Serverless Image Processing API

## Project Overview

This project implements a serverless image processing pipeline using AWS. Whenever a JPG image is uploaded to an Amazon S3 source bucket, an S3 event automatically triggers an AWS Lambda function.

The Lambda function uses the Python Pillow (PIL) library to resize the uploaded image to **128 × 128 pixels** and stores the processed thumbnail in a separate S3 bucket.

## Architecture

User Upload  
↓  
Source S3 Bucket  
↓  
S3 ObjectCreated Event  
↓  
AWS Lambda – ImageThumbnailProcessor  
↓  
Python Pillow  
↓  
Resize to 128 × 128  
↓  
Processed S3 Bucket

## AWS Services Used

- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon CloudWatch
- AWS Lambda Layers

## Technologies Used

- Python
- Boto3
- Pillow (PIL)

## S3 Buckets

**Source Bucket**

`source-images-upload-aakansh-2026`

**Destination Bucket**

`processed-thumbnails-aakansh-2026`

## Lambda Function

**Function Name:** `ImageThumbnailProcessor`

The Lambda function:

1. Receives the S3 event.
2. Extracts the source bucket and object key.
3. Downloads the uploaded image to `/tmp`.
4. Opens the image using Pillow.
5. Converts the image to RGB.
6. Resizes the image to 128 × 128 pixels.
7. Saves the processed image as JPEG.
8. Uploads the thumbnail to the destination S3 bucket.

## Lambda Layer

Pillow is provided through an AWS Lambda Layer.

**Layer:** `PillowLayer`  
**Version:** `1`

## IAM Permissions

The Lambda execution role is granted:

- `s3:GetObject` on the source bucket.
- `s3:PutObject` on the destination bucket.
- CloudWatch logging permissions through `AWSLambdaBasicExecutionRole`.

The complete IAM policy is available in `iam_policy.json`.

## Event Trigger

**Trigger:** `ImageUploadTrigger`

**Event:** All object create events

**Suffix Filter:** `.jpg`

**Destination:** `ImageThumbnailProcessor`

This allows the image-processing pipeline to execute automatically whenever a JPG image is uploaded.

## Testing

The project was tested by uploading a JPG image to the source S3 bucket.

The S3 event successfully invoked the Lambda function, and the processed 128 × 128 thumbnail was generated in the destination bucket.

CloudWatch confirmed successful execution with:

`Thumbnail created successfully: IMG-20260902-WA0003.jpg`

## Project Workflow

`JPG Upload → Amazon S3 → S3 Event → AWS Lambda → Pillow → 128×128 Thumbnail → Processed S3`

## Source Code

- `lambda_function.py` – AWS Lambda image-processing function.
- `iam_policy.json` – IAM permissions used by the Lambda execution role.

## Conclusion

This project demonstrates an event-driven and serverless image-processing architecture using AWS. The system automatically processes uploaded JPG images without requiring a continuously running image-processing server.
