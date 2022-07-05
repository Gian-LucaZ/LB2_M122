import base64
import requests
import six
from src.utilities import Logger
from src.utilities.SettingsManager import SettingsManager

sm = SettingsManager("config.json")


def get(iid: str, ext: str, token, req: int = 0):
    Logger.Information("Getting data for Item: %s" % iid)

    try:
        response = requests.session().get(
            sm.proxy_get_appsettings("apis")["api"] % ext % iid,
            headers={"Authorization": token["token_type"] + " " + token["access_token"]},
        )
        response.raise_for_status()
        playlist_info = response.json()
        return playlist_info
    except requests.exceptions.HTTPError as http_error:
        Logger.Warning("Failed to get data: %s" % http_error)

        if req >= 10:
            Logger.Error("Failed to get data 10 times shutting down now")
            exit(-1)

        return get(iid, ext, token, req + 1)


def request_access_token(req: int = 0):
    payload = {"grant_type": "client_credentials"}

    credentials = sm.proxy_get_appsettings("credentials")
    headers = _get_authorization_headers(credentials["id"], credentials["secret"])

    Logger.Information("Trying to get AccessToken")

    try:
        response = requests.session().post(
            sm.proxy_get_appsettings("apis")["tokenApi"],
            data=payload,
            headers=headers,
            verify=True
        )
        response.raise_for_status()
        token_info = response.json()
        return token_info
    except requests.exceptions.HTTPError as http_error:
        Logger.Warning("Failed to get AccessToken")

        if req >= 10:
            Logger.Error("Failed to get AccessToken 10 times shutting down now")
            exit(-1)

        return request_access_token(req + 1)


def _get_authorization_headers(client_id, client_secret):
    auth_header = base64.b64encode(
        six.text_type(client_id + ":" + client_secret).encode("ascii")
    )
    return {"Authorization": "Basic %s" % auth_header.decode("ascii")}
