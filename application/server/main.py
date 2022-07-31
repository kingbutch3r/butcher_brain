from fastapi import BackgroundTasks, FastAPI
import subprocess
app = FastAPI()


def scan_domian(domain: str, message=""):
    p = subprocess.Popen(['python',"./subscraper/subscraper.py" ,domain,"-r domans.csv" ])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/scan-domain/{domain}")
async def scan(domain: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(scan_domian, domain, message="some notification")
    return {"message": "Notification sent in the background"}
