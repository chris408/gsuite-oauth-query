# gsuite-oauth-query
Quickly get a list of your users oauth grants and their scopes.

This proof of concept was made from the example code from Google, [here](https://developers.google.com/admin-sdk/directory/v1/quickstart/python).

You'll need to follow the setup process in the Google Quickstart Guide link above in order to run this code. 

This code will connect to the GSuite Admin API, fetch the first 10 users, and then list out the each app name and related scopes.

This is useful if you're trying to get an understanding of what GSuite Apps your users have installed. 
