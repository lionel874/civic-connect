from fastapi import FastAPI

from ROUTES.user_route import router as user_router
from ROUTES.location_route import router as location_router
from ROUTES.product_route import router as product_router
from ROUTES.service_route import router as service_router
from ROUTES.order_route import router as order_router
from ROUTES.report_route import router as report_router
from ROUTES.point_connectivite_route import router as point_connectivite_router
from database import Base,engine
from CLASS.report import Report
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from ROUTES.admin_route import router as admin_router




app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.exception_handler(ValueError)
def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )


Base.metadata.create_all(bind=engine)



app.include_router(user_router)
app.include_router(location_router)
app.include_router(product_router)
app.include_router(service_router)
app.include_router(order_router)
app.include_router(report_router)
app.include_router(point_connectivite_router)
app.include_router(admin_router)