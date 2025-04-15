variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "env" {
  description = "Environment name"
  default     = "prod"
}

variable "container_image" {
  description = "Container image URL"
  type        = string
}