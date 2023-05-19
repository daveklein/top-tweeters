# top-tweeters
A Python data streaming demo

## Description
This project consists of three Python applications, one of which is a Flask app.
    - *tweet-producer.py* a Python app that pulls data from Twitter (Twitter dev account required) and produces it to Kafka
    - *tweet-processor* a Python app that processes the stream of Twitter data and counts tweets by user, sending updated count data to a Kafka topic
    - *tweet-dashboard* a Flask app that consumes from the output topic of the tweet-processor and loads a top tweeters dashboard

## Running the demo
To run this demo, you will need Docker and a Twitter developer account.

Replace the Twitter authorization values in `config.py` with your own credentials.

Replace the hashtag value in `config.py.topics`.

Run docker compose up from the directory in which you've cloned this repo.

Run the three Python applications. For best results, run `tweet-producer.py` last.

Browse to `127.0.0.1:5000/top-tweets`