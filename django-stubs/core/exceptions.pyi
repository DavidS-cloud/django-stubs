import sys
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union

if sys.version_info < (3, 8):
    from typing_extensions import Literal
else:
    from typing import Literal

class FieldDoesNotExist(Exception): ...
class AppRegistryNotReady(Exception): ...

class ObjectDoesNotExist(Exception):
    silent_variable_failure: bool = ...

class MultipleObjectsReturned(Exception): ...
class SuspiciousOperation(Exception): ...
class SuspiciousMultipartForm(SuspiciousOperation): ...
class SuspiciousFileOperation(SuspiciousOperation): ...
class DisallowedHost(SuspiciousOperation): ...
class DisallowedRedirect(SuspiciousOperation): ...
class TooManyFieldsSent(SuspiciousOperation): ...
class RequestDataTooBig(SuspiciousOperation): ...
class RequestAborted(Exception): ...
class BadRequest(Exception): ...
class PermissionDenied(Exception): ...
class ViewDoesNotExist(Exception): ...
class MiddlewareNotUsed(Exception): ...
class ImproperlyConfigured(Exception): ...
class FieldError(Exception): ...

NON_FIELD_ERRORS: Literal["__all__"] = ...

class ValidationError(Exception):
    error_dict: Dict[str, List[ValidationError]] = ...
    error_list: List[ValidationError] = ...
    message: str = ...
    code: Optional[str] = ...
    params: Optional[Dict[str, Any]] = ...
    def __init__(
        self,
        # Accepts arbitrarily nested data structure, mypy doesn't allow describing it accurately.
        message: Union[str, ValidationError, Dict[str, Any], List[Any]],
        code: Optional[str] = ...,
        params: Optional[Dict[str, Any]] = ...,
    ) -> None: ...
    @property
    def message_dict(self) -> Dict[str, List[str]]: ...
    @property
    def messages(self) -> List[str]: ...
    def update_error_dict(self, error_dict: Dict[str, List[ValidationError]]) -> Dict[str, List[ValidationError]]: ...
    def __iter__(self) -> Iterator[Union[Tuple[str, List[str]], str]]: ...

class EmptyResultSet(Exception): ...
class SynchronousOnlyOperation(Exception): ...
