import json
from config import kafka_config, tp_config, topics
from confluent_kafka import Producer, Consumer
from confluent_kafka.serialization import IntegerSerializer

def process_tweets():
    tweeters = {}
    tweet_ids = []

    # create producer and consumer
    producer = Producer(kafka_config)
    consumer = Consumer(tp_config)
    serializer = IntegerSerializer()
    
    # subscribe to input topic
    consumer.subscribe([topics['input']])

    # start consume loop
    while True:
        event = consumer.poll(1.0)
        if event is None:
            print('No new data in input topic')
        elif event.error():
            print(f'Bummer! {event.error()}')
        else:            
            tweet = json.loads(event.value())
            # prevent duplicate tweets
            if tweet['id'] not in tweet_ids:
                tweet_ids.append(tweet['id'])
                if tweet['user'] in tweeters:
                    tweeters[tweet['user']] += 1
                else:
                    tweeters[tweet['user']] = 1

                # produce current dictionary entry to output topic
                producer.produce(topics['output'], 
                                 serializer(tweeters[tweet['user']]), 
                                 tweet['user'])
                producer.flush()
                

if __name__ == "__main__":
    process_tweets()

