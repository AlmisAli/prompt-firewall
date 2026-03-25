from fastapi import FastAPI
from app.scanner import scan_prompt
from app.policy import apply_policy
from app.schemas import ScanRequest, ScanResponse
from app.utils import log_scan  

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Prompt Security Firewall is running"}


@app.post("/scan", response_model=ScanResponse)
def scan(request: ScanRequest):
    scan_result = scan_prompt(request.text)
    final_result = apply_policy(scan_result)

    log_scan(final_result)   

    return final_result