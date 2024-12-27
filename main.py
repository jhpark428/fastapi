import argparse
import uvicorn

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
favicon_path = "./favicon.ico"

@app.get("/")
async def index():
  return {"message": "Hello, FastAPI!!"}

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--host", default="0.0.0.0")
  parser.add_argument("--port", default="8080")

  args = parser.parse_args()
  uvicorn.run(app, host=args.host, port=int(args.port))