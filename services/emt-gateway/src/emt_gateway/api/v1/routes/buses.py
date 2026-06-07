from fastapi import APIRouter, HTTPException
from emt_gateway.application.use_cases.get_arrivals import GetArrivalsUseCase
from emt_gateway.infrastructure.emt_client.emt_client import EMTClient


router = APIRouter(prefix = "/buses", tags = ["buses"])

@router.get("/{stop_id}/arrivals")
async def get_arrivals(stop_id: str):
    try:
        use_case = GetArrivalsUseCase(emt_port = EMTClient())
        arrivals = await use_case.execute(stop_id)
        return {"stop_id": stop_id,
                "arrivals": arrivals
                }
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))