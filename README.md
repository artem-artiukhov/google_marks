# google_marks
This is simplified project to visualize of location logged IP addresses using sample Apache log file.

The first thing you need to do is to upload sample Apache file to map.

It is not perfect and as on Dec.3, 2018 requires lot of improvements like:
- pagination - to load only those locations, where map focused on at the moment;
- applying styles;
- debugging map as for some reason https://maps.googleapis.com/maps/api/js do not respond preventing downloading map on location it has been requested;
- setting place to save temporary files to.

Prerequisits (latest versions):
- Django
- Celery
- geolite2
- PostgreSQL
