import file_upload.api.router
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()
app.include_router(file_upload.api.router.router)

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", reload=True)
