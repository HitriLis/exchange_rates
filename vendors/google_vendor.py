import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


class AuthGoogleVendor:

    def __init__(self) -> None:
        """
        Враппер для работы с Google SendSay
        """
        self.credential_file = None
        self.scopes = None
        self.api = None

    def service(self):
        try:
            creds_service = ServiceAccountCredentials.from_json_keyfile_name(self.credential_file, self.scopes)
            http_auth = creds_service.authorize(httplib2.Http())
            return apiclient.discovery.build(self.api, 'v4', http=http_auth)
        except BaseException as err:
            print(err)
