__all__ = ["user_exists", "rename_user"]


def user_exists(users, name):
    return any(u["name"].lower() == name.lower() for u in users)

def rename_user(users, old_name, new_name):
    for u in users:
        if u["name"].lower() == old_name.lower():
            u["name"] = new_name
            return True
    return False

  ##Module-level encapsulation
def _normalize_name(name):
    return name.strip().lower()

print(__name__)