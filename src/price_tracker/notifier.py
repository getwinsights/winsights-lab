import asyncio
import os

from azure.identity import ClientSecretCredential
from dotenv import load_dotenv
from msgraph import GraphServiceClient
from msgraph.generated.models.body_type import BodyType
from msgraph.generated.models.email_address import EmailAddress
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.message import Message
from msgraph.generated.models.recipient import Recipient
from msgraph.generated.users.item.send_mail.send_mail_post_request_body import (
    SendMailPostRequestBody,
)


def send_email(subject: str, body: str):
    load_dotenv()

    tenant_id = os.getenv("MICROSOFT_TENANT_ID")
    client_id = os.getenv("MICROSOFT_CLIENT_ID")
    client_secret = os.getenv("MICROSOFT_CLIENT_SECRET")
    sender_email = os.getenv("EMAIL_ADDRESS")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    credential = ClientSecretCredential(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret=client_secret,
    )

    graph_client = GraphServiceClient(
        credential,
        ["https://graph.microsoft.com/.default"],
    )

    message = Message(
        subject=subject,
        body=ItemBody(
            content_type=BodyType.Text,
            content=body,
        ),
        to_recipients=[
            Recipient(
                email_address=EmailAddress(
                    address=receiver_email,
                )
            )
        ],
    )

    request_body = SendMailPostRequestBody(
        message=message,
        save_to_sent_items=True,
    )

    asyncio.run(
        graph_client.users.by_user_id(sender_email).send_mail.post(
            body=request_body
        )
    )