from pathlib import Path
from typing import Union

def get_files(path: Union[str, Path], extension='.wav'):
    if isinstance(path, str): 
        # path.resolve()是获得绝对路径
        path = Path(path).expanduser().resolve()
    """
    path.rglob()    
        Recursively yield all existing files (of any kind, including
        directories) matching the given pattern, anywhere in this subtree.
    """
    return list(path.rglob(f'*{extension}'))
