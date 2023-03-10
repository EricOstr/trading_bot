# import logging
from typing import Dict, List, Optional

# import pandas as pd

from hummingbot.connector.exchange.coinbase_pro.coinbase_pro_order_book_message import CoinbaseProOrderBookMessage
from hummingbot.core.data_type.order_book import OrderBook
from hummingbot.core.data_type.order_book_message import OrderBookMessage, OrderBookMessageType
# from hummingbot.logger import HummingbotLogger

# _cbpob_logger = None


class CoinbaseProOrderBook(OrderBook):
#     @classmethod
#     def logger(cls) -> HummingbotLogger:
#         global _cbpob_logger
#         if _cbpob_logger is None:
#             _cbpob_logger = logging.getLogger(__name__)
#         return _cbpob_logger

    @classmethod
    def snapshot_message_from_exchange(cls,
                                       msg: Dict[str, any],
                                       timestamp: float,
                                       metadata: Optional[Dict] = None) -> OrderBookMessage:
        """
        *required
        Convert json snapshot data into standard OrderBookMessage format
        :param msg: json snapshot data from live web socket stream
        :param timestamp: timestamp attached to incoming data
        :return: CoinbaseProOrderBookMessage
        """
        if metadata:
            msg.update(metadata)
        return CoinbaseProOrderBookMessage(
            message_type=OrderBookMessageType.SNAPSHOT,
            content=msg,
            timestamp=timestamp
        )

#     @classmethod
#     def diff_message_from_exchange(cls,
#                                    msg: Dict[str, any],
#                                    timestamp: Optional[float] = None,
#                                    metadata: Optional[Dict] = None) -> OrderBookMessage:
#         """
#         *required
#         Convert json diff data into standard OrderBookMessage format
#         :param msg: json diff data from live web socket stream
#         :param timestamp: timestamp attached to incoming data
#         :return: CoinbaseProOrderBookMessage
#         """
#         if metadata:
#             msg.update(metadata)
#         if "time" in msg:
#             msg_time = pd.Timestamp(msg["time"]).timestamp()
#         return CoinbaseProOrderBookMessage(
#             message_type=OrderBookMessageType.DIFF,
#             content=msg,
#             timestamp=timestamp or msg_time)

#     @classmethod
#     def from_snapshot(cls, snapshot: OrderBookMessage):
#         raise NotImplementedError("Coinbase Pro order book needs to retain individual order data.")

#     @classmethod
#     def restore_from_snapshot_and_diffs(self, snapshot: OrderBookMessage, diffs: List[OrderBookMessage]):
#         raise NotImplementedError("Coinbase Pro order book needs to retain individual order data.")
