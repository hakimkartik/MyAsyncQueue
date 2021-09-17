from collections import deque
from messages import Messages


class Channel:
    msg_q = deque()
    __channel_id = 100
    publisher = None

    def __init__(self, channel_name, publisher):
        self.channel_id = self.__channel_id + 1
        self.__channel_id = self.__channel_id + 1
        self.channel_name = channel_name
        self.publisher = publisher
        self.list_of_subscribers = list()
        self.num_of_publisher = 1
        self.num_of_subscriber = 0

    # def set_publisher(self, publisher):
    #     self.publisher = publisher

    def add_msg_to_channel(self, msg):
        m = Messages(msg)
        self.msg_q.append(m)
        self._update_subscribers(m)

    def remove_old_msg(self):
        print("Number of msgs : {}".format(len(self.msg_q)))
        front_msg = self.check_front_msg_in_channel()
        if front_msg.num_of_deliveries_required == 0:
            print("Removing msgs from channel {}".format(self.channel_name))
            self.read_msg_from_channel()
            print("Msgs left : {}".format(len(self.msg_q)))

    def _update_subscribers(self, msg):
        self.list_of_subscribers.sort(key=lambda x: x.priority, reverse=True)
        for sub in self.list_of_subscribers:
            sub.push_msg_to_subscriber(msg)

        self.remove_old_msg()

    def check_front_msg_in_channel(self):
        return self.msg_q[0]

    def read_msg_from_channel(self):
        return self.msg_q.popleft()

    def add_a_subscriber(self, subscriber):
        self.num_of_subscriber += 1
        self.list_of_subscribers.append(subscriber)

    def remove_a_subscriber(self, subscriber):
        self.num_of_subscriber -= 1
        self.list_of_subscribers.remove(subscriber)
