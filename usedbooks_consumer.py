from kafka import KafkaConsumer
from textbooks import usedBookCost
from time import sleep


def consumer3():
# This consumer tells the user which texbook they need
    consumer = KafkaConsumer('book_price', bootstrap_servers='localhost:9092')
    for msg in consumer:
        og_price = float(msg.value)
        print("Used Price: $", usedBookCost(og_price))
        sleep(1)

if __name__ == '__main__':
    consumer3()