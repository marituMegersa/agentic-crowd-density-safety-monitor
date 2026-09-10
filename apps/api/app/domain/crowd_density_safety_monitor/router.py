from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.crowd_density_safety_monitor.schemas import AgenticCrowdDensitySafetyMonitorSessionCreate, AgenticCrowdDensitySafetyMonitorSessionResponse
from app.domain.crowd_density_safety_monitor.service import AgenticCrowdDensitySafetyMonitorService

router = APIRouter(prefix="/api/v1/crowd_density_safety_monitor", tags=["Agentic Crowd Density Safety Monitor Domain"])

@router.post("/sessions", response_model=AgenticCrowdDensitySafetyMonitorSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticCrowdDensitySafetyMonitorSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Crowd Density Safety Monitor.
    """
    return AgenticCrowdDensitySafetyMonitorService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticCrowdDensitySafetyMonitorSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticCrowdDensitySafetyMonitorService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
