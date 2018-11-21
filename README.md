# KBC WebApp

It's a simple **Server + Android App** system which can be used to conduct a quiz game for a relatively
moderate amount of users. This repository contains the code for the server written in **Python3** using the
**Flask** framework. It just provides a REST API to be used by the app and some web pages that help the host
conduct the quiz game.

## Motivation 

This project is inpired by the show "Kaun Banega Crorepati" or "KBC". I built this because my housing society wanted
to conduct a small quiz event for the children on the eve of Children's Day 2018.

## How does this Work ?

Well, the basics are pretty simple. This repository has the code for the server. You start the server
and then use an android app that makes appropriate requests to the server and you get to conduct your game.

### Web Pages Available:

1. `http://localhost:8000/`. This is the main **Homepage.**
2. `http://localhost:8000/resgistered` . This page shows the **Registered users** (updates in real time).
3. `http://localhost:8000/submissions` . This page shows the **Submissions**. (updates in real time)
4. `http://localhost:8000/questions` . This page can be used to display the questions to the audience after the quiz is over

> Note: Replace `localhost` with the ip of your computer on the network

### API Details:

* **URL** : `/api/post/register`

    * Method : `POST`
    * Required Params : `name=[string]`
    * Sample Request : `{ "name" : "John Doe" }`
    * Success Response : `{ "success":True, "id":"<some unique id>", "error": "none" }`
    * Error Response : `{ "success":False, "error": <details about the error> }`

* **URL** : `/api/post/delete_registration`

    * Method : `POST`
    * Required Params : `name=[string], id=[string]`
    * Sample Request : `{ "name" : "John Doe", "id"="89jes1s" }`
    * Success Response : `{ "success":True, "error":"none" }`
    * Error Response : `{ "success":False, "error":"request to delete a non-existing user" }`


* **URL** : `/api/post/submission`

    * Method : `POST`
    * Required Params : `name=[string], id=[string], score=[int]`
    * Sample Request : `{ "name" : "John Doe", "id"="89jes1s", "score": 4 }`
    * Success Response : `{ "success":True, "error":"none" }`
    * Error Response : `{"success":False, "error": "User is not registered"}`

