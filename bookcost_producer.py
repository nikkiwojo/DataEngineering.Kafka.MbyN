from kafka import KafkaProducer
from textbooks import newBookCost
from time import sleep


if __name__=='__main__':

    # Create and send producer / tells student total price to buy brand new book
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    while True:
        book_price = bytes(str(newBookCost()), encoding='utf-8')
        producer.send('book_price', key=book_price, value=book_price)
        print(f"Book Price: ${book_price.decode('utf-8')}")
        sleep(1)