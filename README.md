### README.md

```markdown
# Update Downloads Count - AWS Lambda Deployment with SAM

This repository contains an AWS Lambda function that updates a count in Firestore every 5 minutes. The deployment is managed using AWS SAM (Serverless Application Model).

## Prerequisites

- [AWS CLI](https://aws.amazon.com/cli/) configured with your AWS credentials
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- Python 3.10 installed locally (or any other version supported by Lambda)
- [Conda](https://docs.conda.io/en/latest/) (optional but recommended for environment management)

## Quick Start Guide

### 1. Set Up the Project

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd update_downloads_count
```

### 2. Create and Activate a Conda Environment (Optional)

It is recommended to use a Conda environment to manage dependencies:

```bash
conda create -n lambda-env python=3.10
conda activate lambda-env
```

### 3. Install Dependencies

Install the required Python libraries specified in `src/requirements.txt`:

```bash
pip install -r src/requirements.txt
```

### 4. Local Testing

You can test the Lambda function locally using AWS SAM:

```bash
sam build
sam local invoke UpdateDownloadsCountFunction --event events/event.json
```

This command will build the function and invoke it locally using the provided test event.

### 5. Deploy to AWS

To deploy the Lambda function using AWS SAM, run the following:

```bash
sam deploy --guided
```

Follow the prompts to configure the deployment, such as specifying the stack name and region.

### Optional: Using Docker for Larger Projects

If your project requires more control over dependencies or includes binaries that are easier to manage with Docker, you can use the included `Dockerfile` to build a Docker image:

1. Build the Docker image:

   ```bash
   docker build -t update-downloads-count:latest src/
   ```

2. Tag and push the image to Amazon ECR:

   ```bash
   aws ecr create-repository --repository-name update-downloads-count
   docker tag update-downloads-count:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/update-downloads-count:latest
   docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/update-downloads-count:latest
   ```

3. Update `template.yaml` to use the Docker image:

   ```yaml
   Resources:
     UpdateDownloadsCountFunction:
       Type: AWS::Serverless::Function
       Properties:
         PackageType: Image
         ImageUri: <aws_account_id>.dkr.ecr.<region>.amazonaws.com/update-downloads-count:latest
         Timeout: 30
         Events:
           UpdateCountSchedule:
             Type: Schedule
             Properties:
               Schedule: rate(5 minutes)
   ```

4. Redeploy using:

   ```bash
   sam deploy --guided
   ```

### Directory Structure

```
.
├── events
│   └── event.json                  # Sample event for local testing
├── samconfig.toml                  # Stores configuration for SAM deployments
├── src
│   ├── app.py                      # Main Lambda function code
│   ├── Dockerfile                  # Dockerfile for optional container-based deployment
│   ├── firebay-6554f-54d04c3b13d2.json  # Firestore credentials (DO NOT COMMIT)
│   ├── __init__.py                 # Python package file
│   └── requirements.txt            # Python dependencies
├── template.yaml                   # SAM template for defining the Lambda function and resources
├── tests
│   └── unit
│       └── test_handler.py         # Unit tests for the Lambda function
└── README.md                       # Documentation (you are here)
```

### Important Notes

- **Firestore Credentials**: The `firebay-6554f-54d04c3b13d2.json` file contains credentials for accessing Firestore. Make sure this file is kept secure and is not committed to version control.
- **Deployment Configuration**: The `samconfig.toml` file stores parameters for easy redeployment. Modify it if you need to change the deployment region, stack name, or other settings.
- **Testing**: Use the `sam local` commands to test the Lambda function locally before deploying it to AWS.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Summary
- This README provides a clear guide for deploying the Lambda function using AWS SAM without Docker.
- It includes an optional section for using Docker if needed, catering to both lightweight and more complex deployment scenarios.
- The guide covers the basic setup, local testing, deployment, and Docker usage, ensuring flexibility for different project needs.
# lamda-deploy-template-with-sam
