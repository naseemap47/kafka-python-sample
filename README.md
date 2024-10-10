## Step 1: Get Kafka

[Download](https://www.apache.org/dyn/closer.cgi?path=/kafka/3.8.0/kafka_2.13-3.8.0.tgz) the latest Kafka release and extract it: 

```
$ tar -xzf kafka_2.13-3.8.0.tgz
$ cd kafka_2.13-3.8.0
```
```
pip install kafka-python
```
## Step 2: Start the Kafka environment

NOTE: Your local environment must have Java 8+ installed.

Apache Kafka can be started using KRaft or ZooKeeper. To get started with either configuration follow one of the sections below but not both.
Kafka with KRaft

Kafka can be run using KRaft mode using local scripts and downloaded files or the docker image. Follow one of the sections below but not both to start the kafka server.
Using downloaded files

### Generate a Cluster UUID
```
$ KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
```
Format Log Directories
```
$ bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties
```
Start the Kafka Server
```
$ bin/kafka-server-start.sh config/kraft/server.properties
```

### Kafka with ZooKeeper

Run the following commands in order to start all services in the correct order:
```
# Start the ZooKeeper service
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```
Open another terminal session and run:
```
# Start the Kafka broker service
$ bin/kafka-server-start.sh config/server.properties
```
Once all services have successfully launched, you will have a basic Kafka environment running and ready to use.

## Step 3: Create a topic to store your events

Kafka is a distributed event streaming platform that lets you read, write, store, and process events (also called records or messages in the documentation) across many machines.

Example events are payment transactions, geolocation updates from mobile phones, shipping orders, sensor measurements from IoT devices or medical equipment, and much more. These events are organized and stored in topics. Very simplified, a topic is similar to a folder in a filesystem, and the events are the files in that folder.

So before you can write your first events, you must create a topic. Open another terminal session and run:
```
$ bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
```
All of Kafka's command line tools have additional options: run the kafka-topics.sh command without any arguments to display usage information. For example, it can also show you details such as the partition count of the new topic:
```
$ bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
```
```
Topic: quickstart-events        TopicId: NPmZHyhbR9y00wMglMH2sg PartitionCount: 1       ReplicationFactor: 1	Configs:
Topic: quickstart-events Partition: 0    Leader: 0   Replicas: 0 Isr: 0
```
## Step 4: Write some events into the topic

A Kafka client communicates with the Kafka brokers via the network for writing (or reading) events. Once received, the brokers will store the events in a durable and fault-tolerant manner for as long as you need—even forever.

Run the console producer client to write a few events into your topic. By default, each line you enter will result in a separate event being written to the topic.
```
$ bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
>This is my first event
>This is my second event
```
You can stop the producer client with Ctrl-C at any time.


## Step 5: Read the events

Open another terminal session and run the console consumer client to read the events you just created:
```
$ bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
This is my first event
This is my second event
```
You can stop the consumer client with Ctrl-C at any time.

Feel free to experiment: for example, switch back to your producer terminal (previous step) to write additional events, and see how the events immediately show up in your consumer terminal.

Because events are durably stored in Kafka, they can be read as many times and by as many consumers as you want. You can easily verify this by opening yet another terminal session and re-running the previous command again.


## Step 8: Terminate the Kafka environment

Now that you reached the end of the quickstart, feel free to tear down the Kafka environment—or continue playing around.

Stop the producer and consumer clients with Ctrl-C, if you haven't done so already.
Stop the Kafka broker with Ctrl-C.
Lastly, if the Kafka with ZooKeeper section was followed, stop the ZooKeeper server with Ctrl-C.

If you also want to delete any data of your local Kafka environment including any events you have created along the way, run the command:
```
$ rm -rf /tmp/kafka-logs /tmp/zookeeper /tmp/kraft-combined-logs
```