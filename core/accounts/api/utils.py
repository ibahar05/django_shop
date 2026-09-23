import threading
import logging

logger = logging.getLogger(__name__)


class EmailThreading(threading.Thread):
    def __init__(self, email_obj):
        threading.Thread.__init__(self)
        self.email_obj = email_obj

    def run(self):
        try:
            self.email_obj.send()
        except Exception as e:
            logger.error(f"Failed to send email: {e}", exc_info=True)
