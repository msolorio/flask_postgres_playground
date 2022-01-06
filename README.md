## Steps to Run

Create a postgres database
`$ createdb flask_postgres2`

Run the Bootsrap
`$ ./bootstrap.sh`

This will
- set the necessary environment variables
- start the virtual environment
- create
- run the app

Test in browser or HTTP client


returns all cats
`GET /cats`

returns a single cat
`GET /cats/<int:cat_id>`

creates a cat
`POST /cats { "name": "cat name", "age": 1, "color": "speckled" }`

deletes a cat
`DELETE /cats/<int:cat_id>`
```