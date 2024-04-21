"""import modules"""

import uvicorn
from fastapi import FastAPI

from calculatrice_rpn.apis.rpn import router as stack_router


app = FastAPI()

app.include_router(stack_router, tags=["RPN"])


@app.get("/health")
def health_check():
    return {"status": "ok"}


def run():
    """run for api"""
    uvicorn.run(app, host="0.0.0.0", port=8000)
