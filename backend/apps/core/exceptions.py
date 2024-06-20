from rest_framework.response import Response


class ApiError(Exception):
    status_code: int = 400
    code: int | str
    message: str

    def __init__(self, message=None):
        if message:
            self.message = message

    @property
    def error(self):
        return {"code": self.code, "message": str(self.message)}

    @property
    def errors(self):
        return {"errors": [self.error]}

    def get_response(self):
        return Response(self.errors, status=self.status_code)
