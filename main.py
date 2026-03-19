from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from routers.int_router import int_router
from routers.user_router import router
from routers.ai_router import ai_router
from routers.resume_router import res_router
from routers.voice_router import voice_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routers.learn import learn_router
from JWT import decode_access_token
# from controllers.ai_controller import router as ai_router

app = FastAPI()
app.include_router(router)
app.include_router(int_router)
app.include_router(ai_router)
app.include_router(res_router)
app.include_router(voice_router)
app.include_router(learn_router)
# @app.middleware("http")
# async def trial_middleware(request, call_next):
#     if request.url.path in ["/user/register", "/user/login"]:
#         print("in middleware")
#         response = await call_next(request)
#         return response
#     else:
#         # Use .get() instead of direct access to avoid KeyError
#         auth_header = request.headers.get("authorization")
#         print(auth_header)
#         if auth_header is None:
#             return JSONResponse(status_code=403, content={"error": "unauthorized"})
        
#         try:
#             token = auth_header.split(" ")[1]
#         except IndexError:
#             return JSONResponse(status_code=403, content={"error": "invalid authorization header format"})
#         print(token)
#         decode = decode_access_token(token, "my_secret_key")
#         if decode is None:
#             return JSONResponse(status_code=403, content={"error": "unauthorized"})
#         else:
#             response = await call_next(request)
#             return response