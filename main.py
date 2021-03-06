#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

from models import SafeZone


class MainHandler(webapp2.RequestHandler):
    def get(self):

        safezone_query = SafeZone.query()
        safezones = safezone_query.fetch(100)

        template_args = {
            'safezones': safezones,
        }


        template = JINJA_ENVIRONMENT.get_template('templates/main.jinja2')
        self.response.write(template.render(template_args))


class InsertHandler(webapp2.RequestHandler):
    def get(self):

        template = JINJA_ENVIRONMENT.get_template('templates/SafeZones/insert.jinja2')
        self.response.write(template.render())


class EditHandler(webapp2.RequestHandler):
    def get(self, id):

        safezone = SafeZone.get_by_id(int(id))

        if not safezone:
            print(id)

        template_args = {
            'safezone': safezone,
        }

        template = JINJA_ENVIRONMENT.get_template('templates/SafeZones/edit.jinja2')
        self.response.write(template.render(template_args))


class SingleHandler(webapp2.RequestHandler):
    def get(self, id):

        safezone = SafeZone.get_by_id(int(id))

        template_args = {
            'safezone': safezone,
        }

        template = JINJA_ENVIRONMENT.get_template('templates/SafeZones/single.jinja2')
        self.response.write(template.render(template_args))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/insert', InsertHandler),
    (r'/safezone/(.*)/edit', EditHandler),
    (r'/safezone/(.*)', SingleHandler)
], debug=True)
