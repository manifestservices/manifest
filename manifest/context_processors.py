import os
from config_master import OFFICIAL_MAIL,OFFICIAL_PHONE,OFFICIAL_ADDRESS,DOMAIN,TESTIMONIALS

def common_contexts(request):
    PRODUCTION_MODE=False
    if os.environ.get('MODE')=='production':
        PRODUCTION_MODE=True
    return {
            'OFFICIAL_MAIL':OFFICIAL_MAIL,
            'OFFICIAL_PHONE':OFFICIAL_PHONE,
            'OFFICIAL_ADDRESS':OFFICIAL_ADDRESS,
            'DOMAIN':DOMAIN,
            'PRODUCTION_MODE':PRODUCTION_MODE,
            'testimonials':TESTIMONIALS
            }