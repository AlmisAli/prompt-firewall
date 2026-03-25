from pydantic import BaseModel


class ScanRequest(BaseModel):
    text: str


class ScanResponse(BaseModel):
    final_action: str
    output_text: str
    details: dict