import json
from flask.views import MethodView
from google.appengine.api import users
from gaejson import GaeJSONEncoder


class CurrentUser(MethodView):
    def get(self):
        user = users.get_current_user()
        if user:
            return json.dumps(user, cls=GaeJSONEncoder)