import pika

params = pika.URLParameters('amqps://zobyksdf:tEXN4vKXrQskmY9Lmi39zqk5IcdHzkSE@kangaroo.rmq.cloudamqp.com/zobyksdf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, propreties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()