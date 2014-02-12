__author__ = 'coreyja'

from endpoints_proto_datastore.ndb.model import EndpointsModel
from google.appengine.ext import ndb


class Hours(EndpointsModel):
    _message_fields_schema = ('id', 'monOpen', 'tueOpen', 'wedOpen', 'thursOpen', 'friOpen', 'satOpen', 'sunOpen',
                              'monClose', 'tueClose', 'wedClose', 'thursClose', 'friClose', 'satClose', 'sunClose')

    monOpen = ndb.TimeProperty()
    tueOpen = ndb.TimeProperty()
    wedOpen = ndb.TimeProperty()
    thursOpen = ndb.TimeProperty()
    friOpen = ndb.TimeProperty()
    satOpen = ndb.TimeProperty()
    sunOpen = ndb.TimeProperty()

    monClose = ndb.TimeProperty()
    tueClose = ndb.TimeProperty()
    wedClose = ndb.TimeProperty()
    thursClose = ndb.TimeProperty()
    friClose = ndb.TimeProperty()
    satClose = ndb.TimeProperty()
    sunClose = ndb.TimeProperty()


class SafeZone(EndpointsModel):
    _message_fields_schema = ('id', 'title', 'location', 'hours', 'phone', 'occupancy', 'max_occupancy', 'extra_info')

    title = ndb.StringProperty()
    location = ndb.GeoPtProperty()

    hours = ndb.StructuredProperty(Hours)

    phone = ndb.StringProperty()

    occupancy = ndb.IntegerProperty()
    max_occupancy = ndb.IntegerProperty()

    extra_info = ndb.StringProperty()

    def formatted_phone(self):

        return  '(' + self.phone[0:3] + ') ' + self.phone[3:6] + '-' + self.phone[6:] if self.phone else ''