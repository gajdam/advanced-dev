class Tag:
    def __init__(self, userId: str, movieId: str, tag: str, timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


def load_tags(file_path: str):
    tags = []
    with open(file_path, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            line = line.strip()

            if not line:
                continue

            parts = line.split(",", 3)
            if len(parts) < 4:
                raise ValueError(f"Incorrect line format: {line}")

            tag = Tag(parts[0], parts[1], parts[2], parts[3])
            tags.append(tag.__dict__)

    return tags
