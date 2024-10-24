variable "environment" {
  description = "The environment for the deployment (e.g., dev, staging, production)"
  type        = string
}

variable "region" {
  description = "The region where the resources will be deployed (e.g., us-west1, eu-central-1)"
  type        = string
}