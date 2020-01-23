# gsuite-oauth-query
Quickly get a list of your users oauth grants and their scopes.

This proof of concept was made from the example code from Google, [here](https://developers.google.com/admin-sdk/directory/v1/quickstart/python).

You'll need to follow the setup process in the Google Quickstart Guide link above in order to run this code. 

This code will connect to the GSuite Admin API, fetch the first 10 users, and then list out the each app name and related scopes.

This is useful if you're trying to get an understanding of what GSuite Apps your users have installed. 

## Example output

```
$ python gsuite-oauth-query.py 
Getting the first 10 users in the domain
user1@domain.com
Google APIs Explorer
openid
https://www.googleapis.com/auth/admin.directory.user.security

Lucidchart
https://www.googleapis.com/auth/script.external_request
https://www.googleapis.com/auth/userinfo.profile
https://www.googleapis.com/auth/userinfo.email
https://www.googleapis.com/auth/presentations.currentonly
https://www.googleapis.com/auth/script.container.ui
openid
https://www.googleapis.com/auth/drive.file
https://www.googleapis.com/auth/script.storage
https://www.googleapis.com/auth/documents.currentonly
https://www.googleapis.com/auth/admin.directory.user.readonly
https://www.googleapis.com/auth/spreadsheets.currentonly

Mixmax
https://www.googleapis.com/auth/userinfo.profile
https://www.googleapis.com/auth/userinfo.email
https://www.googleapis.com/auth/contacts.readonly
openid
https://www.googleapis.com/auth/calendar
https://mail.google.com/

Debian Chromium
https://www.google.com/accounts/OAuthLogin

Quickstart
https://www.googleapis.com/auth/admin.directory.user.security
https://www.googleapis.com/auth/admin.directory.user

Boomerang for Gmail
https://www.googleapis.com/auth/contacts
https://www.googleapis.com/auth/userinfo.profile
https://www.googleapis.com/auth/userinfo.email
openid
https://mail.google.com/

user2@domain.com
SurveyMonkey
https://www.googleapis.com/auth/userinfo.profile
https://www.googleapis.com/auth/userinfo.email
https://www.googleapis.com/auth/plus.me
openid

LanguageTool
https://www.googleapis.com/auth/documents
https://www.googleapis.com/auth/script.external_request
https://www.googleapis.com/auth/userinfo.profile
https://www.googleapis.com/auth/userinfo.email
https://www.googleapis.com/auth/script.container.ui
openid

PDF Mergy
https://www.googleapis.com/auth/userinfo.profile
https://www.googleapis.com/auth/userinfo.email
openid

Infogram
https://www.googleapis.com/auth/userinfo.profile
https://www.googleapis.com/auth/userinfo.email
openid

Lucidpress
https://www.googleapis.com/auth/userinfo.profile
https://www.googleapis.com/auth/userinfo.email
openid
https://www.googleapis.com/auth/drive.file
https://www.googleapis.com/auth/drive.readonly
https://www.googleapis.com/auth/admin.directory.user.readonly

Awesome Table
https://www.googleapis.com/auth/userinfo.profile
https://www.googleapis.com/auth/userinfo.email
openid
https://spreadsheets.google.com/feeds
```
