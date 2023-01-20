import time
import asyncio
from random import randint
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routers.graph_router import graphql_app as graph_router
from routers.rpc_router import router as rpc_router
from routers.rest_router import router as rest_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

# @app.middleware("http")
# async def faulty_server(request: Request, call_next):

#     if randint(1,10) == 10:
#         return JSONResponse(
#             status_code=503,
#             content={"message":"The Server has encountered an unexpected failure"}
#         )

#     delay = randint(1, 11)

#     if delay == 11:
#         await asyncio.sleep(20)
#     elif delay > 9:
#         await asyncio.sleep(delay)
#     else:
#         await asyncio.sleep(1)



#     response = await call_next(request)
#     return response


app.include_router(rest_router)
app.include_router(rpc_router)
app.include_router(graph_router, prefix="/graphql") # type: ignore