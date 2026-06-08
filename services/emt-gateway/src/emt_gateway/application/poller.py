import asyncio
import logging
from emt_gateway.config import settings
from emt_gateway.application.use_cases.get_arrivals import GetArrivalsUseCase
from emt_gateway.infrastructure.emt_client.emt_client import EMTClient
from emt_gateway.infrastructure.kafka.dependencies import kafka_producer

logger = logging.getLogger(__name__)


async def poll_stops():
    logger.info(f"Iniciando polling cada {settings.polling_interval_seconds}s")
    logger.info(f"Monitorizando paradas: {settings.stops_to_monitor}")

    while True:
        for stop_id in settings.stops_to_monitor:
            try:
                use_case = GetArrivalsUseCase(emt_port=EMTClient())
                arrivals = await use_case.execute(stop_id)
                await kafka_producer.publish_arrivals(stop_id, arrivals)
                logger.info(f"Parada {stop_id}: {len(arrivals)} buses publicados")
            except Exception as e:
                logger.error(f"Error polling parada {stop_id}: {e}")

        await asyncio.sleep(settings.polling_interval_seconds)