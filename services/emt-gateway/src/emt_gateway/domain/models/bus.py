from dataclasses import dataclass

@dataclass
class BusArrival:
    line: str
    destination: str
    stop_id: str
    estimated_time: int # En segundos
    distance: int # En metros

    def minutes_remaining(self) -> int:
        return self.estimated_time // 60
    
    def is_arrival_soon(self) -> bool:
        return self.estimated_time < 60


@dataclass
class BusStop:
    stop_id: str
    name: str
    address: str
    latitude: float
    longitude: float