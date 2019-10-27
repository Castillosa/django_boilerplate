from django.conf import settings


def settings_context(_request):
    return {"settings": settings}

import re
from django.template import base
base.tag_re = re.compile(base.tag_re.pattern, re.DOTALL)
