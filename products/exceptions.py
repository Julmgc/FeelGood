from rest_framework.exceptions import APIException


class ProductNotFoundError(APIException):
    status_code = 404

    def __init__(self, detail=None, code=None):
        if code:
            self.status_code = code
        if not detail:
            detail = {"detail": "Product id not found."}
        super().__init__(detail, code)
