from ntk_pattern import MessageSUB
from ntk_pattern import MessagePUB
from msg_dict import TOPIC

## MAP 
class Map2DDataSUB(MessageSUB):
    def __init__(self, callback, topic=TOPIC['Map2DData']):
        super().__init__(callback,topic)

class Map2DDataPUB(MessagePUB):
    def __init__(self,topic=TOPIC['Map2DData']):
        super().__init__(topic)

class Map2DDataACKSUB():
    def __init__(self, callback, topic=TOPIC['Map2DDataACK']):
        super().__init__(callback,topic)


class Map2DDataACKPUB():
    def __init__(self,topic=TOPIC['Map2DDataACK']):
        super().__init__(topic)



## GOAL



