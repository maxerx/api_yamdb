from django.core.exceptions import ValidationError

import datetime

def validator_title_year(value):
    current_year = datetime.datetime.now().year
    if value > current_year:
        raise ValidationError(
            'Сообщение не может быть из будущего'
        )
