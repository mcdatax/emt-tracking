from fastapi import APIRouter, HTTPException
from emt_gateway.application.use_cases.get_arrivals import GetArrivalsUseCase
from emt_gateway.infrastructure.emt_client.emt_client import EMTClient
from emt_gateway.infrastructure.kafka.dependencies import kafka_producer

router = APIRouter(prefix = "/buses", tags = ["buses"])

@router.get("/{stop_id}/arrivals")
async def get_arrivals(stop_id: str):
    try:
        use_case = GetArrivalsUseCase(emt_port = EMTClient())
        arrivals = await use_case.execute(stop_id)
        await kafka_producer.publish_arrivals(stop_id, arrivals)
        return {"stop_id": stop_id,
                "arrivals": arrivals
                }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))