from flask import Flask
from threading import Thread
from config import td_config, topics
from page import part_a, part_b
from confluent_kafka import Consumer
from confluent_kafka.serialization import IntegerDeserializer, StringDeserializer

app = Flask(__name__)

leader_board = {}

@app.route('/top-tweets')
def top_tweets():
    result = part_a
    for count, item in enumerate(sorted(leader_board.items(), key=lambda kv: kv[1], reverse=True)):
        result += f"<tr><td>{item[0]}</td><td>{item[1]}</td></tr>"
        if count > 10:
            break
    result += part_b
    return result


def load_leaders():
    consumer = Consumer(td_config)
    int_ser = IntegerDeserializer()
    str_ser = StringDeserializer()
    consumer.subscribe([topics["output"]])
    while True:
        event = consumer.poll(1.0)
        if event is None:
            print('No new data in output topic')
        elif event.error():
            print(f'Bummer! {event.error()}')
        else:            
            user = str_ser(event.key())
            count = int_ser(event.value())
            # exclude conference account and/or other popular outliers
            if user not in ['Conf_Account']:
                leader_board[user] = count

def run_app():
    app.run(host="127.0.0.1", port=5000, threaded=True)

if __name__ == '__main__':
    first_thread = Thread(target=load_leaders)
    second_thread = Thread(target=run_app)
    first_thread.start()
    second_thread.start()
    
