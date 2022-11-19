from dataclasses import dataclass

@dataclass
class Product:
    id: int
    description: str
    org: str


@dataclass
class Timeline:
    time: str
    product_id: int
    action: str
