from fastapi import BackgroundTasks, FastAPI
from ..components.data_parse.csvtojson import make_json
from datetime import datetime
import subprocess
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
cred = credentials.Certificate("./env/butcher-5081c-firebase-adminsdk-eisiy-9e096d4d0d.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
app = FastAPI()


def scan_domian(domain: str, parent =""):
    now = datetime.now()
    dt_string = now.strftime("_%d_%m_%Y_%H_%M_%S")
    parent_dir = os.getcwd()+"\\"+domain+dt_string+".txt"
    parent_dir.strip
    p = subprocess.Popen(['python',"./tools/third_party/subscraper/subscraper.py" ,domain,"-r"+parent_dir])
    # # Using readlines()
    p.wait()
    file1 = open(parent_dir, 'r')
    Lines = file1.readlines()
    doc_ref = db.collection(u'Targets').document(domain)
    doc_ref.set({
    u'name': domain,
    
    u'subdomains': Lines})
    # p.wait()
    # subprocess.Popen(['python',"./application/components/data_parse/csvtojson.py" ,domain+dt_string+".csv",domain+dt_string+".json"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/scan-domain/{domain}")
async def scan(domain: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(scan_domian,domain, )
    return {"message": "Notification sent in the background"}
