from fastapi import HTTPException, status

class BaseException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self): 
        super().__init__(
            status_code=self.status_code, 
            detail=self.detail
        )

class FilmsNotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Фильм не найден"