output "api_gateway_url" {
  description = "API Gateway URL"
  value       = aws_api_gateway_deployment.deployment.invoke_url
}

output "lambda_function_name" {
  description = "Lambda function name"
  value       = aws_lambda_function.app.function_name
}

output "lambda_function_arn" {
  description = "Lambda function ARN"
  value       = aws_lambda_function.app.arn
}

output "kms_key_arn" {
  description = "KMS key ARN for encryption"
  value       = aws_kms_key.lambda_key.arn
}