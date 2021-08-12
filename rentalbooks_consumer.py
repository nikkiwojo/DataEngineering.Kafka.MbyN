from kafka import KafkaConsumer
from textbooks import rentalPrice
from time import sleep


def consumer4():
# This consumer tells the user which texbook they need
    consumer = KafkaConsumer('book_price', bootstrap_servers='localhost:9092')
    for msg in consumer:
        og_price = float(msg.value)
        print("Rental Price: $", rentalPrice(og_price))
        sleep(1)

if __name__ == '__main__':
    consumer4()