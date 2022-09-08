import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


class AuthGoogleVendor:

    def __init__(self, credential_file: str, scopes: list) -> None:
        """
        Враппер для работы с Google SendSay
        :param credential_file: Название файла с кредами
        :param scopes:
        """
        self.credential_file = credential_file
        self.scopes = scopes

    def _service(self):
        creds_service = ServiceAccountCredentials.from_json_keyfile_name(self.credential_file, self.scopes)
        http_auth = creds_service.authorize(httplib2.Http())
        return apiclient.discovery.build('sheets', 'v4', http=http_auth)
