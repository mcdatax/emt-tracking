from abc import ABC, abstractmethod
from emt_gateway.domain.models.bus import BusArrival, BusStop

class EMTPort(ABC):

    @abstractmethod
    async def login(self) -> str:
        """Retorma el accessToken"""

    @abstractmethod
    async def get_arrivals(self, stop_id: str, token: str) -> list[BusArrival]:
        """Retorna los buses en tiempo real para una parada"""

    @abstractmethod
    async def get_stop_info(self, stop_id: str, token: str) -> BusStop:
        """Retorna la información de una parada"""