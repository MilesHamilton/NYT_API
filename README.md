# New York Times Books RESTFUL API

A list of 20 all time most popular books from New York Times

## Run the app

- Fork this repo
- Install and run pipenv shell on your local machine
- Install dependencies within the shell
- run the `app.py` file with the command: `python3 app.py`

## Run the tests

# REST API

The REST API to the example app is described below.

## Get A Specific Thing

### Request

`GET /id or string`

### Ex. Response

    author: "Diana Gabaldon",
    description: "The author of the Outlander novels gives tips on writing sex scenes, drawing on examples from the books.",
    id: 1,
    title: ""I GIVE YOU MY BODY ...""

## Create a new Thing

### Request

`POST /thing`

### Ex. Response

      author: "George RR Martin
      description: "winter is coming.."
      title: "A Song of Ice and Fire"

      "
    {"id":1,"title":"Foo","status":"new"}
