import time
import RPi.GPIO as GPIO

from google.cloud import pubsub_v1

# TODO project_id = "Your Google Cloud Project ID"
# TODO topic_name = "Your Pub/Sub topic name"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('ebay-instant', 'trial')

def callback(message_future):
    # When timeout is unspecified, the exception method waits indefinitely.
    if message_future.exception(timeout=30):
        print('Publishing message on {} threw an Exception {}.'.format(
            topic_name, message_future.exception()))
    else:
        print(message_future.result())

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print("Button Pressed")
        time.sleep(0.2)
        data = 'purchase'
        # Data must be a bytestring
        data = data.encode('utf-8')
        # When you publish a message, the client returns a Future.
        message_future = publisher.publish(topic_path, data=data)
        message_future.add_done_callback(callback)
        print('Published message IDs:')

