import os
import pwd

from django.core.management.base import BaseCommand
from router.transports import Transport

class Command(BaseCommand):
    args = 'text'
    help = 'Parses the provided text message and handles it'

    def handle(self, text, **options):
        try:
            user = os.getlogin()
        except OSError:
            user = pwd.getpwuid(os.geteuid())[0]

        transport = Transport("script")
        messages = transport.incoming(user, text)

        for i, message in enumerate(messages):
            print "%d/%d %s" % (i+1, len(messages), message.time.isoformat())
            print "--> %s" % message.text
            print "----" + "-"*len(message.text)

            replies = message.replies.all()
            for j, reply in enumerate(replies):
                print "    %d/%d %s" % (j+1, len(replies), reply.uri)
                print "    <-- %s" % reply.text


