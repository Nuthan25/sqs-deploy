import json
import logging

# Configure logging to log to CloudWatch Logs
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # Log the received event
    logger.info("Received event: " + json.dumps(event))

    # Process the event (in this case, we just log it)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }