from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']

def main():
    """Prints the GSuite App names and related scopes for the first 10 users.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run.
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('admin', 'directory_v1', credentials=creds)

    # Call the Admin SDK Directory API for users.
    print('Getting the first 10 users in the domain')
    results = service.users().list(customer='my_customer', maxResults=10,
                                orderBy='email').execute()
    users = results.get('users', [])

    # Iterates over each user.
    for user in users:
        email = user['primaryEmail']
        # Call the Admin API for tokens.
        r = service.tokens().list(userKey=email).execute()
        print(email)
        for item in r['items']:
            print(item['displayText'])
            for scope in item['scopes']:
                print(scope)
            print('')

if __name__ == '__main__':
    main()
