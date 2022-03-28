from rest_framework.exceptions import APIException

class UserNotAcess(APIException):
    status_code = 403
    default_detail = {"detail": "You do not have permission to perform this action."}