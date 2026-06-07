from emt_gateway.domain.models.bus import BusArrival
from emt_gateway.domain.ports.emt_port import EMTPort


class GetArrivalsUseCase:

    def __init__(self, emt_port: EMTPort):
        self.emt_port = emt_port

    async def execute(self, stop_id: str) -> list[BusArrival]:
        token = await self.emt_port.login()
        return await self.emt_port.get_arrivals(stop_id, token)
        