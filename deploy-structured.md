# Structured Logging in a Simple Python3 Lambda Function

## Standard Libraries

Developers can use Python3 standard library modules to log data in a structured format. [AWS Lambda Monitoring part I: Improved logging (Python)](https://zoolite.eu/posts/lambda-python-logging/) provides an example of using the `logging`, `json`, `time`, and `os` modules to customize and structure function output so it can be queried effectively.

However, developers can take advantage of an existing Python module from AWS - [AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/latest/) to capture structured application data along with metadata about the function execution. We will dive a bit deeper into how developers can log their data using the `aws-lambda-powertools` module.

## AWS Lambda Powertools for Python

Per the [AWS Lambda Powertools for Python Github project page](https://github.com/awslabs/aws-lambda-powertools-python), it is a suite of Python utilities for AWS Lambda functions to ease adopting best practices such as tracing, structured logging, custom metrics, and more.

**NOTE:** AWS Lambda Powertools is also generally available for [Java](https://github.com/awslabs/aws-lambda-powertools-java) and [Typescript](https://github.com/awslabs/aws-lambda-powertools-typescript).

### Including AWS Lambda Powertools in Functions

For the purposes of this example, AWS Lambda Powertools will be installed via PyPi in our serverless application. This is the mecanism SAM uses to install third-party packages. However, it can be included as a [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-layer) as well. The `aws-lambda-powertools` package is defined in the [structured_logging_function/simple_powertools_logging/requirements.txt](./structured_logging_function/simple_powertools_logging/requirements.txt) file.


## Logging Application Data

You can build and run the function locally using the following commands.

```bash
cd structured_logging_function
sam build --use-container
sam local invoke PowertoolsFunction
```

The function emits the following log entries.

**NOTE:** The output below is representative - your output will differ.

```bash
Invoking index.handler (python3.9)
Skip pulling image and use local one: public.ecr.aws/sam/emulation-python3.9:rapid-1.53.0-x86_64.

Mounting /path/to/lambda-logging-primer/structured_logging_function/.aws-sam/build/PowertoolsFunction as /var/task:ro,delegated inside runtime container
START RequestId: 4d7cf74b-9f99-4c6b-9d6a-b6531a1a9b5c Version: $LATEST
{"level":"INFO","location":"handler:11","message":{"Random number":97},"timestamp":"2022-08-08 13:59:31,070+0000","service":"simple-powertools-logging","cold_start":true,"function_name":"PowertoolsFunction","function_memory_size":"128","function_arn":"arn:aws:lambda:us-east-1:012345678912:function:PowertoolsFunction","function_request_id":"4d7cf74b-9f99-4c6b-9d6a-b6531a1a9b5c"}
nullEND RequestId: 4d7cf74b-9f99-4c6b-9d6a-b6531a1a9b5c
REPORT RequestId: 4d7cf74b-9f99-4c6b-9d6a-b6531a1a9b5c  Init Duration: 0.34 ms  Duration: 344.89 ms     Billed Duration: 345 ms Memory Size: 128 MB     Max Memory Used: 128 MB
```

The output of the function still includes the **START**, **END**, and **REPORT** entries but make note of the log entry. It includes an abundance of information about the execution in addition to the payload emitted by the function. This is done by importing the `aws_lambda_powertools` **Logger** and **LambdaContext** methods in [structured_logging_function/simple_powertools_logging/index.py](./structured_logging_function/simple_powertools_logging/index.py). The actual log data is captured using the simple line:


* **level** - Logging level

* **location** - Source code ocation where the logging statement was executed

* **message** - Log data emitted from the function

* **timestamp** - Timestamp with milliseconds

* **service** - Service name (default: `service_undefined` but can be most easily set in SAM function envrionment variable `POWERTOOLS_SERVICE_NAME`)

* **cold_start** - Whether the function was cold (needing to run init phase)

* **function_name** - Function name

* **function_memory_size** - Function memory allocaion

* **function_arn** - Full ARN of the function

* **function_request_id** - Unique request ID

### Improving Structured Output

There is one subtle but important difference between the logged output in [structured_logging_function/simple_powertools_logging/index.py](./structured_logging_function/simple_powertools_logging/index.py) and [simple_function/user_defined_logging/index.py](./simple_function/user_defined_logging/index.py).

simple_function/user_defined_logging Handler
```bash
logger.info(f'Generated random number {random.randrange(100) + 1}')
```

structured_logging_function/simple_powertools_logging Handler
```bash
logger.info({'Random number':random.randrange(100) + 1})
```
