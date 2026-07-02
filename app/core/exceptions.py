class AppException(Exception):
    def __init__(self, message: str, status_code: int, detail: str | None = None):
        self.message = message
        self.status_code = status_code
        self.detail = detail
        super().__init__(message)
        

class AgentExecutionError(AppException):
    def __init__(self, detail: str | None=None):
        super().__init__(
            message="Agent execution failed",
            status_code=500,
            detail=detail)
        
class TextExtractionError(AppException):
    def __init__(self, detail: str | None=None):
        super().__init__(
            message="Error While Extracting Text",
            status_code=500,
            detail=detail)
        
class VectorUpsertError(AppException):
    def __init__(self, detail: str | None=None):
        super().__init__(
            message="Error While Injesting",
            status_code=500,
            detail=detail)
        
class CreateChunkError(AppException):
    def __init__(self, detail: str | None=None):
        super().__init__(
            message="Error While Chunking",
            status_code=500,
            detail=detail)
        
class CreateEmbeddingError(AppException):
    def __init__(self, detail: str | None=None):
        super().__init__(
            message="Error While Creating Embeddings",
            status_code=500,
            detail=detail)
        
class DeleteDocError(AppException):
    def __init__(self, detail: str | None=None):
        super().__init__(
            message="Error While Deleting Doc",
            status_code=500,
            detail=detail)
        
class ListDocError(AppException):
    def __init__(self, detail: str | None=None):
        super().__init__(
            message="Error While Listig Docs",
            status_code=500,
            detail=detail)


class InvalidCredentials(AppException):
    def __init__(self):
        super().__init__("Invalid credentials", 401)


class UserAlreadyExists(AppException):
    def __init__(self):
        super().__init__("User already exists", 409)