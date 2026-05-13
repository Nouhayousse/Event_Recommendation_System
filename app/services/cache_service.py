import redis
import hashlib
import json



redis_client = redis.Redis(host='localhost',
                            port=6379,
                            db=1,
                            decode_responses=True)


def generate_event_key(source: str, url: str):
    return f"{source}:{hashlib.md5(url.encode()).hexdigest()}"

def is_event_cached(source: str, url: str) -> bool:
    key = generate_event_key(source, url)
    return redis_client.exists(key)


def cache_event(source: str, url: str, data: dict,  ttl=86400):
    key = generate_event_key(source, url)
    redis_client.setex(key, ttl, json.dumps(data))