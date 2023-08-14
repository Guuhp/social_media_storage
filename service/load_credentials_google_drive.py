from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os


def load_credentials_google_drive():
    credentials = service_account.Credentials.from_service_account_file('credentials.json',
    scopes=['https://www.googleapis.com/auth/drive'])
    service = build('drive', 'v3', credentials=credentials)
    return service


def search_videos_in_drive(folder_id):
    service = load_credentials_google_drive()
    query = f"'{folder_id}' in parents"
    response = service.files().list(q=query).execute()
    files = response.get('files', [])
    if len(files) > 0:
        print("files found in folder:")
        return files
    else:
        print("files not found in folder.")