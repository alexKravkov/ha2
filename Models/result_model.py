from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(order=True)
class Res:
    code: int
    triangle_type: str
    error_message: str
