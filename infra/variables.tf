variable "project" {
  description = "Short name used in resource names and tags."
  type        = string
  default     = "static-site"
}

variable "aws_region" {
  description = "Region for the S3 bucket."
  type        = string
  default     = "us-east-1"
}
