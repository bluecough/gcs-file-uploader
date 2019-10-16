Setup:

Run the following to create a serviceAccount that will be the background, download its key, create a bucket, allow the proper access to the service account, and set an open CORS policy.

PROJECT_NAME=$(gcloud config list --format="value(core.project)")
gcloud iam service-accounts create urlsigner --display-name="GCS URL Signer" --project=${PROJECT_NAME}
gcloud iam service-accounts keys  create service_account.json --iam-account=urlsigner@${PROJECT_NAME}.iam.gserviceaccount.com
gsutil mb gs://$PROJECT_NAME-urlsigner
gsutil iam ch  serviceAccount:urlsigner@${PROJECT_NAME}.iam.gserviceaccount.com:roles/storage.admin gs://$PROJECT_NAME-urlsigner
gsutil cors set cors.txt gs://$PROJECT_NAME-urlsigner


