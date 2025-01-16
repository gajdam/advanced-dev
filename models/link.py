class Link:
    def __init__(self, movieId: str, imdbId: str, tmdbId: str):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


def load_links(file_path: str):
    links = []
    with open(file_path, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            line = line.strip()

            if not line:
                continue

            parts = line.split(",", 2)
            if len(parts) < 3:
                raise ValueError(f"Incorrect line format: {line}")

            link = Link(parts[0], parts[1], parts[2])
            links.append(link.__dict__)

    return links
