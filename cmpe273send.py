#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:42:51 2023

@author: user
"""

import pika

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (ensure it exists)
channel.queue_declare(queue='hello')

# Initialize message counter
sent_message_count = 0

# Send 10,000 messages
for i in range(10000):
    message = f'Hello World! Message number {i+1}'
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    sent_message_count += 1
    print(f" [x] Sent '{message}'")

# Print total sent message count
print(f"\nTotal Sent Messages: {sent_message_count}")

# Close the connection
connection.close()
