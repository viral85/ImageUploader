from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse


class ApiResponse:
    @staticmethod
    def create_response(success: bool, message: str, status_code: int, data: list = None) -> JSONResponse:
        data_dict = {"message": message, "success": success}
        if data:
            if 'data' in data:
                data_dict |= data
            else:
                data_dict['data'] = data
        response_headers = {"Content-Type": "application/json"}
        return JSONResponse(content=jsonable_encoder(data_dict), status_code=status_code, headers=response_headers)
