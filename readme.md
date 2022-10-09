# Kafka hands on
# Introduction
In this tutorial, you will learn how to build a local Apache Kafka cluster. You will also learn how to create producers and consumers in Kafka using Python.
## How to run
make sure you have ```python3```, ```docker``` and ```docker-compose``` installed on your machine.
```
docker-compose up
pip install requirements.txt
```
after that tou need to produce some messages to the broker by run this file in background.

```python3 producer.py &```

after producing some messages you can consume them by running this command

```python3 consumer.py```

and expect to have some logs in your terminal.

## How to stop
- Running this command ``` pkill -f producer.py``` to stop producer from sending new messages.
- Stopping docker containers ``` docker-compose stop ```

## Future work
- Replace fake generated data with public api for realtime data like (stocks, weather, crypto prices).
- Scale the kafka server by adding more brokers (containers) in ```docker-compose.yaml``` file to simulate different machines hosting kafka on them, and split produced data to different brokers based on any factor like country in weather and stocks data or currency in crypto-currency data.
- Also apply partitioning in produced messages and parallelize the consumers to make consuming data faster.
- if you have other public data can aggregate them like traffic data aggregated with weather data, and write them to postgresDB aka(postgres container in docker compose file) beside logging them in the terminal.