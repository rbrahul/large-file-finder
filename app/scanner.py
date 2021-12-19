from pathlib import Path

from app.validator import  haveFileConditionsMet


def traverse_dir(path, scanned, permission_issue, conditions):
    try:
        result = Path(path).iterdir()
        for item in result:
            if(item.is_symlink()):
                continue
            if(item.is_dir()):
                traverse_dir(item, scanned, permission_issue, conditions)
            elif(item.is_file() and haveFileConditionsMet(item, conditions)):
                scanned.append({
                    "path": str(item),
                    "size": item.stat().st_size
                })
    except PermissionError as _:
        permission_issue.append(path)