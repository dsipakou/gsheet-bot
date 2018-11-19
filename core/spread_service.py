from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client import file, client, tools

from core import local_constants as constants


class SpreadService:
    def __init__(self):
        self.token_file = constants.TOKEN_FILE
        self.scopes = constants.SCOPES
        self.creds_file = constants.CREDS_FILE

    def get_creds(self):
        store = file.Storage(self.token_file)
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(self.creds_file, self.scopes)
            creds = tools.run_flow(flow, store)
        return creds

    def get_service(self, creds=None):
        crd = creds
        if not crd:
            crd = self.get_creds()
        return build('sheets', 'v4', http=crd.authorize(Http()))

    def get_sheet(self, service=None):
        if service:
            sheet = service.spreadsheets()
        else:
            sheet = self.get_service().spreadsheets()
        return sheet