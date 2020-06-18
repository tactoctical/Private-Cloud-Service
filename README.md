# Private-Cloud-Service
A project i made since i wanted my own personal cloud server. You can run it on a VPS or your own Raspberry pi.
Dependencies: flask, flask_sqlalchemy, flask_login

You can register and login and see your authenticated files and folders. All of the data from the users is stored in a 
root folder at /media/pcs/ where there is two folders. There is a cloud folder and uploads folder. 
The cloud folder is where all the files from the users is located in subfolders, 
and the uploads folder is where the administrator can upload public files that all download.

The config file in instance/config.py contains the folder locations and other settings.

The user has the functionality to upload, edit and download files from the cloud.

The server uses a sqlite3 database with a users table with the columns:
- id
- email
- username
- password
- storagelimit
- date_of_creation
- permission_level
All users start with 5 gb of available storage on signup (You can ofc change this)
The permission level has to be changed manually in the database to give the user permission to upload to the public folder.
you can do it with this command SQL"UPDATE users SET permission_level=1 where id={USER ID};" 


Be aware it lacks comments in some places, but hope it is somewhat understandable.
