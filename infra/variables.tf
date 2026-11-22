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

variable "github_org" {
  description = "GitHub user or organisation that owns the repository."
  type        = string
  default     = "Ya-dje"
}

variable "github_repo" {
  description = "GitHub repository name."
  type        = string
  default     = "Static-website-hosted-on-AWS-with-Github-actions"
}

variable "github_branch" {
  description = "Only workflows running on this branch can deploy."
  type        = string
  default     = "main"
}

variable "github_org_id" {
  description = "Numeric ID of the GitHub account (appears in the OIDC sub claim)."
  type        = string
  default     = "194743586"
}

variable "github_repo_id" {
  description = "Numeric ID of the GitHub repository (appears in the OIDC sub claim)."
  type        = string
  default     = "1456890531"
}
