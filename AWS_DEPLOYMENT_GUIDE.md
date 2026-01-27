# AWS Deployment Setup Guide

## Prerequisites
1. AWS Account (with billing enabled)
2. IAM permissions to create ECS, ECR, and IAM roles

## Step 1: Create IAM Role for GitHub Actions

```bash
# Create trust policy file (trust-policy.json):
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::YOUR_ACCOUNT_ID:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringLike": {
          "token.actions.githubusercontent.com:sub": "repo:Vmane778/secdevops-pipeline:*"
        }
      }
    }
  ]
}

# Create the role
aws iam create-role --role-name GitHubActionsECSRole --assume-role-policy-document file://trust-policy.json

# Attach policies
aws iam attach-role-policy --role-name GitHubActionsECSRole --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPushOnly
aws iam attach-role-policy --role-name GitHubActionsECSRole --policy-arn arn:aws:iam::aws:policy/AmazonECS_FullAccess
```

## Step 2: Add GitHub Secret

In your GitHub repository:
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Create a new secret: `AWS_ROLE_ARN`
3. Value: `arn:aws:iam::YOUR_ACCOUNT_ID:role/GitHubActionsECSRole`

Replace `YOUR_ACCOUNT_ID` with your AWS Account ID.

## Step 3: Create ECS Cluster

```bash
aws ecs create-cluster --cluster-name secdevops-cluster --region us-east-1
```

## Step 4: Create ECR Repository

```bash
aws ecr create-repository --repository-name secdevops-pipeline --region us-east-1
```

## Step 5: Create ECS Task Definition

```bash
aws ecs register-task-definition \
  --cli-input-json file://aws/ecs-task-definition.json \
  --region us-east-1
```

Update `ACCOUNT_ID` in the JSON file with your AWS Account ID.

## Step 6: Create ECS Service

```bash
aws ecs create-service \
  --cluster secdevops-cluster \
  --service-name secdevops-service \
  --task-definition secdevops-task \
  --desired-count 1 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-XXXXXXXX],assignPublicIp=ENABLED}" \
  --region us-east-1
```

Get your VPC subnet ID:
```bash
aws ec2 describe-subnets --region us-east-1 --query 'Subnets[0].SubnetId' --output text
```

## Step 7: Push Code

Once everything is configured, push to `main` and the GitHub Actions workflow will:
1. Build the Docker image
2. Push to AWS ECR
3. Update ECS task definition
4. Deploy to ECS service

## Monitor Deployment

```bash
# Check service status
aws ecs describe-services \
  --cluster secdevops-cluster \
  --services secdevops-service \
  --region us-east-1

# Check running tasks
aws ecs list-tasks \
  --cluster secdevops-cluster \
  --region us-east-1
```

## Cleanup (Optional)

```bash
# Delete service
aws ecs delete-service --cluster secdevops-cluster --service secdevops-service --force

# Delete cluster
aws ecs delete-cluster --cluster secdevops-cluster

# Delete ECR repository
aws ecr delete-repository --repository-name secdevops-pipeline --force
```
