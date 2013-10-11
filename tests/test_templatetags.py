# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.template import RequestContext, Template

from . import BaseTest

import stored_messages


class TestStoredMessagesTags(BaseTest):
    def test_stored_messages_list(self):
        # create a message
        for i in range(20):
            stored_messages.add_message_for([self.user], stored_messages.INFO, "unicode message ❤")

        t = Template("{% load stored_messages_tags %}"
                     "{% stored_messages_list 15 %}")
        render = t.render(RequestContext(self.request))

        self.assertInHTML("<li>[test_user] unicode message ❤</li>", render, 15)

    def test_stored_messages_list_empty_for_unauthenticated_user(self):
        stored_messages.add_message_for([self.user], stored_messages.INFO, "unicode message ❤")

        t = Template("{% load stored_messages_tags %}"
                     "{% stored_messages_list 15 %}")
        render = t.render(RequestContext(self.factory.get("/")))

        self.assertInHTML("<li>[test_user] unicode message ❤</li>", render, 0)