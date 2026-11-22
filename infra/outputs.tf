output "site_bucket_name" {
  description = "Name of the S3 bucket holding the website files."
  value       = aws_s3_bucket.site.id
}

output "cloudfront_distribution_id" {
  description = "Needed later to invalidate the cache on deploy."
  value       = aws_cloudfront_distribution.site.id
}

output "site_url" {
  description = "Public URL of the website."
  value       = "https://${aws_cloudfront_distribution.site.domain_name}"
}

output "deploy_role_arn" {
  description = "Role the GitHub Actions workflow assumes."
  value       = aws_iam_role.deploy.arn
}
