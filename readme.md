# Welcome to the Anythink Market repo

To start the app use Docker. It will start both frontend and backend, including all the relevant dependencies, and the db.

Please find more info about each part in the relevant Readme file ([frontend](frontend/readme.md) and [backend](backend/README.md)).

## Development

When implementing a new feature or fixing a bug, please create a new pull request against `main` from a feature/bug branch and add `@vanessa-cooper` as reviewer.

## First setup
Follow these steps:
- 1. Install docker by following the description at [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- 2. run the command `docker compose up` (if you installed the docker-compose script, you need to run `docker-compose up`)
- 3. Wait (coffee time)
- 4. Validate by going to [http://localhost:3000/api/ping](http://localhost:3000/api/ping). This should return you a nice and shiny 200 and the body og `{"msg":"Pong! Seems like Everythink is working, great job!"}`
- 5. Last step to validate is to go to [http://localhost:3001/register](http://localhost:3001/register) and sign up a new user.
- 6. Profit!