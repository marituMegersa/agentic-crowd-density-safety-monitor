from pydantic import BaseModel
from typing import List, Dict, Any

class AgentState(BaseModel):
    task_id: str
    status: str = "COMPLETED"
    history: List[Dict[str, Any]] = []
