from crecatpcha.crecaptcha import is_a_human
import logging
from django.conf import settings
from django.http import HttpResponseForbidden

logger = logging.getLogger(__name__)

SECRET_KEY = settings.CRECAPTCHA_SECRET_KEY
try:
    KEY_NAME = settings.CRECAPTCHA_KEY_NAME
except:
    KEY_NAME = 'recaptcha_token'


def crecaptcha(action=None,
               on_error_function=None,
               args_on_error=[],
               kwargs_on_error={},
               threshold=0.5):
    def do_challenge(func):
        def check_captcha(*args, **kwargs):
            request = args[0]
            ok, code = is_a_human(SECRET_KEY, request.POST[KEY_NAME], action=action, threshold=threshold)
            if ok:
                return func(*args, **kwargs)
            else:
                if not on_error_function:
                    raise HttpResponseForbidden
                kwargs_on_error['data'] = {'code': code, 'info': 'cRecaptcha error'}
                return on_error_function(*args, *args_on_error, **kwargs_on_error)

        return check_captcha

    return do_challenge
