from django.forms import ModelForm, CheckboxSelectMultiple
from datetimewidget.widgets import DateTimeWidget

from .models import Notifications

class NotificationsForm(ModelForm):
    class Meta:
        model = Notifications
        fields = ['header', 'content', 'image_url', "send_at",'user']

        widgets = {'user': CheckboxSelectMultiple,
                   "send_at": DateTimeWidget(attrs={'id':"send_at"}, usel10n = True, bootstrap_version=3)}
