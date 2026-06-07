import httpx
from emt_gateway.domain.models.bus import BusArrival, BusStop
from emt_gateway.domain.ports.emt_port import EMTPort
from emt_gateway.config import settings


class EMTClient(EMTPort):

    def __init__(self):
        self.base_url = settings.emt_base_url
        self.client = httpx.AsyncClient()

    async def login(self) -> str:
        response = await self.client.get(
            f"{self.base_url}/v1/mobilitylabs/user/login/",
            headers = {
                "email": settings.emt_email,
                "password": settings.emt_password
            }
        )
        response.raise_for_status()
        data = response.json()
        return data["data"][0]["accessToken"]
    
    async def get_arrivals(self, stop_id: str, token: str) -> list[BusArrival]:
        response = await self.client.post(
            f"{self.base_url}/v1/transport/busemtmad/stops/{stop_id}/arrives/",
            headers = {"accessToken": token},
            json = {
                "cultureInfo": "ES",
                "Text_StopRequired_YN": "N",
                "Text_EstimationsRequired_YN": "Y",
                "Text_IncidencesRequired_YN": "N"
            }
        )

        response.raise_for_status()
        arrivals = response.json()["data"][0]["Arrive"]
        return[
            BusArrival(
                line = a["line"],
                destination = a["destination"],
                stop_id = stop_id,
                estimated_time = a["estimateArrive"],
                distance = a["DistanceBus"]
            )
            for a in arrivals
        ]

    async def get_stop_info(self, stop_id: str, token: str) -> BusStop:
        response = await self.client.get(
            f"{self.base_url}/v1/transport/busemtmad/stops/{stop_id}/detail/",
            headers = {"accessToken": token},
        )
        response.raise_for_status()
        stop = response.json()["data"][0]
        return BusStop(
            stop_id = stop_id,
            name = stop["stopName"],
            address = stop["address"],
            latitude = stop["geometry"]["coordinates"][1],
            longitude = stop["geometry"]["coordinates"][0],
        )