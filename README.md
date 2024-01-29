# meme-random

TODO

## Setup Dev Environment

(Optional) Create and activate `venv`

```sh
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install necessary dependencies:

```sh
pip install -r src/requirements.txt
```

Note: Cloud Run expects a single `source` directory for deployment from source. This directory should contain both a `requirements.txt` and the entry point to the app `main.py`.

## Setup Cloud Environment (Deployment)

TODO

## Deployment

To deploy from source (which automatically builds a container image from source code and deploys it) change to the directory `src` and use the following command:

```sh
gcloud run deploy --update-env-vars CLOUD_STORAGE_BUCKET=replace-with-storage-bucket-here
```

If prompted to enable the API, reply `y` to enable.

1. When you are prompted for the *source code location*, press Enter to deploy the current folder (dir `src`).

2. When you are prompted for the *service name*, use e.g. `meme-random`

3. If you are prompted to enable the Artifact Registry API or to allow creation of Artifact Registry repository, respond by pressing `y`.

4. When you are prompted for region: select the region of your choice, e.g. `europe-west3`

5. When you are prompted to *allow unauthenticated invocations*, respond by pressing `y`.
