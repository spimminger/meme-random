import os
import random

from flask import Flask
from google.cloud import storage

CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Serve random item from a Storage bucket"""

    # Create a Storage client.
    gcs = storage.Client()

    # Get the bucket and all of its items
    bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)
    blobs = list(bucket.list_blobs())

    # Select a random element from list of items
    target_blob = random.choice(blobs)

    # Read item as string
    blob_as_string = target_blob.download_as_string()

    return blob_as_string


if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)))
