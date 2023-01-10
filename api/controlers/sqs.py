import boto3
import logging
import configparser
import os

from botocore.exceptions import ClientError
from botocore.config import Config

class SQSService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        aws_config = Config(region_name=os.getenv("CLOUD_REGION"))
        self.sqs = boto3.client("sqs", endpoint_url=os.getenv("CLOUD_ENDPOINT"), config=aws_config)

    def send_one_message(self, queue_url, message_body, message_attributes=None):
        if not message_attributes:
            message_attributes = {}
        
        try:
            self.logger.debug("Sending message to queue %s", queue_url)
            response = self.sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=message_body,
                MessageAttributes=message_attributes
            )
        except ClientError as error:
            self.logger.exception("Send message to %s failed: %s", queue_url, message_body)
            raise error
        else:
            return response