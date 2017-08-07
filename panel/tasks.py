from celery.task import task
from .models import NotificationsUsers
from .helpers import send_notifications, mark_notification_as_sent

import datetime
@task
def process_notification():
    notifications = NotificationsUsers.objects.filter(
        is_sent=False, notification__send_at__gte=datetime.datetime.now()
    ).values_list("notification__pk", "user__username","notification__header",
                  "notification__content", "notification__image_url")
    for notification in notifications:
        payload = {
            "header": notification[2],
            "content": notification[3],
            "image_url": notification[4]
        }
        result = send_notifications(
            user_id=notification[1],
            payload=payload
        )

        mark_notification_as_sent(notification[0], notification[2], result)