kafka_config = { 
    "bootstrap.servers": "localhost:29092",
}

credentials = {
    "consumer.key": "{YOUR_CONSUMER_KEY}",
    "consumer.secret": "{YOUR_CONSUMER_SECRET}",
    "access.token": "{YOUR_ACCESS_TOKEN}",
    "access.token_secret": "{YOUR_ACCESS_TOKEN_SECRET}"
}

tp_config = {
    "bootstrap.servers": "localhost:29092",
    "auto.offset.reset": "earliest",
    "group.id": "conf-tweets"
}

td_config = {
    "bootstrap.servers": "localhost:29092",
    "auto.offset.reset": "earliest",
    "group.id": "top-tweeters"
}

topics = {
    "input": "conf-tweets",
    "output": "top-tweeters",
    "hashtag": "conference"
}
