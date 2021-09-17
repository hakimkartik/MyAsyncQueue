class Subscriber:
    sub_id = 0
    # received_msg = list()

    def __init__(self, priority=0):
        self.subscriber_id = self.sub_id + 1
        self.sub_id = self.sub_id + 1
        self.priority = priority
        self.received_msg = list()

    def push_msg_to_subscriber(self, msg):
        msg.num_of_deliveries_required -= 1
        self.received_msg.append(msg)

    def read_all_received_msgs(self):
        tmp = [msg.data for msg in self.received_msg]
        return tmp

    def clear_subscriber_q(self):
        self.received_msg.clear()
