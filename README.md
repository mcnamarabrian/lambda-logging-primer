# lambda-logging-primer

[AWS Lambda](https://aws.amazon.com/lambda/) is a serverless computes service provided by [Amazon Web Services](https://aws.amazon.com). Because it is serverless, developers and operations engineers do not have access to the application environment or underlying operating system. Traditional techniques like using `ssh`, `awk`, and `grep` are not available. It is important to understand how application log data is persisted and the steps application developers can take to optimize their logging experience.

The purpose of this repository is to demonstrate these patters in code. The examples are written using [Python3](https://www.python.org/) and use the [AWS Serverless Application Model (SAM)](https://aws.amazon.com/serverless/sam/) but the principles can be applied to other supported AWS Lambda runtimes regardless of the deployment mechanism.

# Pre-requisites

* [Python3.9](https://www.python.org/downloads/)

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)

* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

* [AWS CLI](https://aws.amazon.com/cli/)

# AWS Lambda Logging Behavior

Log files are text records created by applications indicating events have transpired. Historically, these records have been easy for humans to read but difficult for machines to make sense of. Logs typically contain information useful to understand normal behavior and troubleshoot when applications or systems are behaving abnormally.

AWS Lambda has the ability to log function output to [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), a monitoring and observability service. The [AWS IAM execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) associated with your function must have the ability to create a log group and log streams. The AWS managed policy [AWSLambdaBasicExecutionRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole) has the necessary permissions.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```

# Next Steps

Once you have the pre-requisites installed, you can get started with [deploying a simple Python3 Lambda function](./deploy-simple.md).
