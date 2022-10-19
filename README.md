### Server requirements
You need to get to have Docker and docker-compose installed

### Deployment process
Clone the repo
change directory to repo
Run ```docker-compose build```
Once the build is complete run ```docker-compose up```

Run migrations
```docker-compose run web python manage.py migrate```
create a superuser by running 
```docker-compose run web python manage.py createsuperuser```

generate a token
generate a token by running 
```docker-compose run web python manage.py drf_create_token <username>```

creating a trip:

You can send a curl on the terminal to:

```
curl --request POST \
  --url http://0.0.0.0:8000/api/trips/create/api_token=<your_generated_token>\
  --header 'Content-Type: application/json' \
  --data '{
		"address_type": "pick_up_point",
		"driver_id": 3,
		"vehicle_id": 4,
		"customer_id": 2,
		"address": "adress",
		"cargo_tonnage": 100.34
}'

```
