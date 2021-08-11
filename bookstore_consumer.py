from kafka import KafkaConsumer
from textbooks import textbook_list
from time import sleep


def consumer1():
# This consumer tells the user which texbook they need
    consumer = KafkaConsumer('Textbook_Needed', bootstrap_servers='localhost:9092')
    for msg in consumer:
        id_num = int(msg.value)
        print("Textbook Needed: ", textbook_list(id_num))
        sleep(1)


if __name__ == '__main__':
    consumer1()
