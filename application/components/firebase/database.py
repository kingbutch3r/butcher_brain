import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("../../env/butcher-5081c-firebase-adminsdk-eisiy-9e096d4d0d.json")
firebase_admin.initialize_app(cred)