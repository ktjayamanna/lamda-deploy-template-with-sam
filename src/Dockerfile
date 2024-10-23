# Use the official AWS Lambda Python 3.9 image
FROM public.ecr.aws/lambda/python:3.9

# Copy application code and requirements to the container
COPY app.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install dependencies
RUN pip install -r requirements.txt

# Set the CMD to your function's handler
CMD ["app.lambda_handler"]
