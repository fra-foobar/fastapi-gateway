import re
from fastapi import FastAPI, Request
from cache.main import get_from_cache
import time
import uvicorn

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    if request.method == 'GET':
        # call get from cache
        response = await call_next(request)
    else:
        # POST | PUT | PATCH | DELETE | COPY | HEAD | OPTIONS | LINK | UNLINK | PURGE | LOCK | UNLOCK | PROPFIND | VIEW
        # dispatch to microservice and clear cache
        response = await call_next(request)
        # PURGE THE CACHE. THE URL PATTERN TO PURGE MUST BE PASSED BY THE CALLED MICROSERVICE
        pass
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
