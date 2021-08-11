from kafka import KafkaConsumer
from textbooks import classList
from time import sleep


def consumer2():
# This consumer tells the user which courses use the indicated textbook
    consumer = KafkaConsumer('Textbook_Needed', bootstrap_servers='localhost:9092')
    for msg in consumer:
        id_num = int(msg.value)
        print("Courses:", classList(id_num))
        sleep(1)

if __name__ == '__main__':
    consumer2()