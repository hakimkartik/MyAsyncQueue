from publisher import Publisher
from subscriber import Subscriber
from channel import Channel


def process():
    pub1 = Publisher("pub1")
    channel1 = Channel("channel1", pub1)
    sub1 = Subscriber("sub1")
    channel1.add_a_subscriber(sub1)
    channel1.add_msg_to_channel("hello")
    print(sub1.read_all_received_msgs())
    channel1.add_msg_to_channel("world")
    print(sub1.read_all_received_msgs())
    channel1.add_msg_to_channel("leo")
    print(sub1.read_all_received_msgs())

    sub2 = Subscriber("sub2")
    print(sub2.read_all_received_msgs())

    channel1.add_a_subscriber(sub2)
    print(sub2.read_all_received_msgs())

    channel1.add_msg_to_channel("a")
    print(sub1.read_all_received_msgs())
    print(sub2.read_all_received_msgs())
    channel1.add_msg_to_channel("b")
    print(sub1.read_all_received_msgs())
    print(sub2.read_all_received_msgs())
    channel1.add_msg_to_channel("c")
    print(sub1.read_all_received_msgs())
    print(sub2.read_all_received_msgs())
    channel1.remove_a_subscriber(sub2)


def main():
    process()


if __name__ == "__main__":
    main()
