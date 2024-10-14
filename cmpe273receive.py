#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:08:49 2023

@author: user
"""

import pika

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Initialize message counter
received_message_count = 0

# Callback function to handle received messages and count them
def callback(ch, method, properties, body):
    global received_message_count
    received_message_count += 1
    print(f" [x] Received {body.decode()}")

# Set up the consumer
channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

# Start consuming messages
try:
    channel.start_consuming()
except KeyboardInterrupt:
    # Print the total received message count when the consumer is interrupted
    print(f"\nTotal Received Messages: {received_message_count}")
    connection.close()
