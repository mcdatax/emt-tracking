import json
from aiokafka import AIOKafkaProducer
from emt_gateway.config import settings



class KafkaProducer:

    def __init__(self):
        self._producer = None

    async def start(self):
        self._producer = AIOKafkaProducer(
            bootstrap_servers=settings.kafka_bootstrap_servers
        )
        await self._producer.start()

    async def stop(self):
        if self._producer:
            await self._producer.stop()

    async def publish_arrivals(self, stop_id: str, arrivals: list) -> None:
        for arrival in arrivals:
            message = {
                "stop_id": stop_id,
                "line": arrival.line,
                "destination": arrival.destination,
                "estimated_time": arrival.estimated_time,
                "distance": arrival.distance,
            }
            await self._producer.send(
                topic = "bus-arrivals",
                key = stop_id.encode(),
                value = json.dumps(message).encode()
            )