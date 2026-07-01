from pydantic import BaseModel, Field
from typing import Dict, List

class Scenario(BaseModel):
    name: str
    local_metadata: Dict[str, str] = Field(default_factory=dict)
    precondition: str = ""
    test_steps: str = ""
    expected_result: str = ""

class Module(BaseModel):
    name: str
    global_metadata: Dict[str, str] = Field(default_factory=dict)
    scenarios: List[Scenario] = Field(default_factory=list)
