import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='barc', exchange_type='topic')

routing_key = sys.argv[1] 
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='barc', routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()