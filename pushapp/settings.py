from django.conf import settings

PUSHAPP_SETTINGS = getattr(settings, "PUSHAPP_SETTINGS", {})


# GCM
PUSHAPP_SETTINGS.setdefault("GCM_POST_URL", "https://android.googleapis.com/gcm/send")
PUSHAPP_SETTINGS.setdefault("GCM_MAX_RECIPIENTS", 1000)


# APNS
PUSHAPP_SETTINGS.setdefault("APNS_PORT", 2195)
PUSHAPP_SETTINGS.setdefault("APNS_FEEDBACK_PORT", 2196)
PUSHAPP_SETTINGS.setdefault("APNS_ERROR_TIMEOUT", None)
PUSHAPP_SETTINGS.setdefault("APNS_MAX_NOTIFICATION_SIZE", 2048)
if settings.DEBUG:
    PUSHAPP_SETTINGS.setdefault("APNS_HOST", "gateway.sandbox.push.apple.com")
    PUSHAPP_SETTINGS.setdefault("APNS_FEEDBACK_HOST", "feedback.sandbox.push.apple.com")
else:
    PUSHAPP_SETTINGS.setdefault("APNS_HOST", "gateway.push.apple.com")
    PUSHAPP_SETTINGS.setdefault("APNS_FEEDBACK_HOST", "feedback.push.apple.com")
