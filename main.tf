provider "google" {
  project     = "diplomat-394119"
  credentials = file("credentials.json")
  region      = "us-central1"
  zone        = "us-central1-c"
}
