from .models import NotificationsUsers

def send_notifications(user_id, payload, **kwargs):
    """
    :param user_id: user to  whom notifications needs to trigger
    :param payload: {
    "header" : "",
    "content": "",
    "image_url": ""
    }
    :param kwargs: any extra data which may require to trigger notification
    :return:
    """
    return True

def mark_notification_as_sent(notification_id, user_id, result):
    NotificationsUsers.objects.filter(user__username=user_id,
                                      notification__pk=notification_id
                                      ).update(is_sent=result)