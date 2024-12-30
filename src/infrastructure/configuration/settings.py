import os
from dotenv import load_dotenv
import yaml
load_dotenv()


CONNECTION_NOSQL = os.getenv("CONNECTION_NOSQL")
CONNECTION_SQL = os.getenv("CONNECTION_SQL")
REPORT = yaml.safe_load(open(f"{os.getcwd()}/report.yml", encoding="utf-8"))
