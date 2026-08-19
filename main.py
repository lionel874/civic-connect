from fastapi import FastAPI

from ROUTES.user_route import router as user_router
from ROUTES.location_route import router as location_router
from ROUTES.proudct_route import router as product_router
from ROUTES.service_route import router as service_router
from ROUTES.order_route import router as order_router
from ROUTES.report_route import router as report_router


app = FastAPI()


app.include_router(user_router)
app.include_router(location_router)
app.include_router(product_router)
app.include_router(service_router)
app.include_router(order_router)
app.include_router(report_router)