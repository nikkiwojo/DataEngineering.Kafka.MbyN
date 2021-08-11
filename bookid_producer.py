from kafka import KafkaProducer
from textbooks import textbook_id
from time import sleep


if __name__=='__main__':

    # Create and send producer / tells student which textbook is needed
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    while True:
        book_id = bytes(str(textbook_id()), encoding='utf-8')
        producer.send('Textbook_Needed', key=book_id, value=book_id)
        print(f"Textbook Id: #{book_id.decode('utf-8')}")
        sleep(1)



