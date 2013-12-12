__author__ = 'coreyja'

from endpoints_proto_datastore.ndb.model import EndpointsModel
from google.appengine.ext import ndb


class Hours(EndpointsModel):
    _message_fields_schema = ('id', )

    monOpen = ndb.TimeProperty(auto_now_add=True)
    tueOpen = ndb.TimeProperty()
    wedOpen = ndb.TimeProperty()
    thursOpen = ndb.TimeProperty()
    friOpen = ndb.TimeProperty()
    satOpen = ndb.TimeProperty()
    sunOpen = ndb.TimeProperty()

    monClose = ndb.TimeProperty(auto_now_add=True)
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

    hours = ndb.IntegerProperty()

    phone = ndb.StringProperty()

    occupancy = ndb.IntegerProperty()
    max_occupancy = ndb.IntegerProperty()

    extra_info = ndb.StringProperty()