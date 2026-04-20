import boto3
import os

bucket_name = "dbbsvcdsuickldsd"
file_name = "index.html"

# show current directory files (for debugging)
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())

s3 = boto3.client("s3")

try:
    s3.upload_file(file_name, bucket_name, file_name)
    print("✅ Upload successful!")
except Exception as e:
    print("❌ Upload failed:", e)
