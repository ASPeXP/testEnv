 
import os
from dotenv import load_dotenv

load_dotenv("./.env")  # บรรทัดนี้จะไปอ่านค่าตัวแปรมาจากไฟล์ .env ทั้งหมด

name = os.getenv("NAME")
domain = os.getenv("DOMAIN")

print("Name: ", name)
print("Domain: ", domain)