class Messages:
    __msg_id = 0

    def __init__(self, data, num_of_deliveries_required=1):
        self.msg_id = self.__msg_id + 1
        self.__msg_id = self.__msg_id + 1
        self.data = data
        self.num_of_deliveries_required = num_of_deliveries_required
