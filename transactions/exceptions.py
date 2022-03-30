from rest_framework.exceptions import APIException


class TransactionError(APIException):
    status_code = 400

    def __init__(self, detail=None, code=None):
        if code:
            self.status_code = code
        if not detail:
            detail = {"error": "Transaction fail"}
        super().__init__(detail, code)
