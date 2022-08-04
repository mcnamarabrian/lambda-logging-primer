# Structured Logging in a Simple python3 Lambda Function

## Standard Libraries

It is possible to take advantage of python3 modules to log data in a structured format. [AWS Lambda Monitoring part I: Improved logging (Python)](https://zoolite.eu/posts/lambda-python-logging/) provides an example of using the `logging`, `json`, `time`, and `os` modules to demonstrate how developers can roll their own logging module to structure function output.

Though helpful, developers can take advantage of an existing module  from AWS - [AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/latest/). We will dive a bit deeper into how developers can log their data using the `aws-lambda-powertools` module.

## AWS Lambda Powertools

