from typing import Callable, List, Mapping, Tuple, Union

JSONType = Union[str, int, float, bool, None, Mapping[str, 'JSONType'], List['JSONType'], Tuple['JSONType', ...]]
APIMapping = Mapping[str, Callable[[], JSONType]]
