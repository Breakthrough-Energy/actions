import json


def parse_version(section):
    return {
        name: info["version"][2:] for name, info in section.items() if "version" in info
    }


def to_dict(lockfile):
    with open(lockfile) as f:
        obj = json.load(f)

    default = parse_version(obj["default"])
    develop = parse_version(obj["develop"])
    return {k: v for d in (default, develop) for k, v in d.items()}


def compare(original, updated):
    old = to_dict(original)
    new = to_dict(updated)
    result = {}
    result["Additions"] = {
        name: version for name, version in new.items() if name not in old
    }
    result["Deletions"] = {
        name: version for name, version in old.items() if name not in new
    }
    result["Updates"] = {
        name: f"{version} -> {new[name]}"
        for name, version in old.items()
        if name in new and new[name] != version
    }
    return result


if __name__ == "__main__":
    import sys

    try:
        result = compare(sys.argv[1], sys.argv[2])
        print(json.dumps(result))
    except Exception as e:
        print(f"Error trying to generate comparsion: {e}")
