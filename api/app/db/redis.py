import os
from redis import Redis


class RedisConn(Redis):
    def check_status(self):
        try:
            self.get(None)  # getting None returns None or throws an exception
        except Exception:
            return False
        return True


redis_conn = RedisConn(
    host=os.environ["REDIS_HOST"],
    port=os.environ["REDIS_PORT"],
    db=0, decode_responses=True
)
