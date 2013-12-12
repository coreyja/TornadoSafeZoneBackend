from google.appengine.ext import endpoints
from protorpc import remote
from models import Hours, SafeZone

@endpoints.api(name="safezones", version="v1", description="SafeZones API", hostname="TornadoSafeZone.appspot.com")
class SafeZoneAPI(remote.Service):

    @Hours.method(path="hours/insert", name="hours.insert", http_method="POST", user_required=False)
    def hours_insert(self, hours):
        hours.put()
        return hours

    @SafeZone.method(path="safezone/insert", name="safezone.insert", http_method="POST", user_required=False)
    def safezone_insert(self, sz):
        sz.put()
        return sz;

    @SafeZone.query_method(query_fields=('limit', 'order', 'pageToken'), path="safezone/list", name="safezone.list", http_method="GET", user_required=False)
    def safezone_list(self, query):
        return query


    @SafeZone.method(request_fields=('id', ), path="safezone/delete/{id}", name="safezone.delete", http_method="DELETE", user_required=False)
    def safezone_delete(self, sz):

        if not sz.from_datastore:
            raise endpoints.NotFoundException("The SafeZone specified was not found")

        sz.key.delete()
        return SafeZone(name="deleted") # New SafeZone with deleted as name to show success

    @Hours.method(request_fields=('id', ), path="hours/delete/{id}", name="hours.delete", http_method="DELETE", user_required=False)
    def hours_delete(self, hours):

        if not hours.from_datastore:
            raise endpoints.NotFoundException("The Hours specified was not found")

        hours.key.delete()
        return Hours() # New Hours for success



app = endpoints.api_server([SafeZoneAPI], restricted=False)
