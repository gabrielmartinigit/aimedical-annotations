import os
import boto3

TABLE = os.environ["TABLE_NAME"]
BUCKET = os.environ["BUCKET"]
dynamodb = boto3.resource("dynamodb")


def lambda_handler(event, context):
    text_metrics = event["TextMetrics"]["body"]["metrics"]
    key = event["TranscriptionJob"]["Media"]["MediaFileUri"].split(f"s3://{BUCKET}/")[-1]
    record_id = os.path.splitext(os.path.basename(key))[0]
    table = dynamodb.Table(TABLE)

    table.update_item(
        Key={"record_id": record_id},
        UpdateExpression="set report=:report, video=:video",
        ExpressionAttributeValues={
            ":report": text_metrics,
            ":video": key,
        },
        ReturnValues="ALL_NEW",
    )

    return {
        "statusCode": 200,
        "body": {"status": "success"},
    }
