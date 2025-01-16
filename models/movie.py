class Movie:
    def __init__(self, id: str, title: str, genres):
        self.id = id
        self.title = title
        self.genres = genres


def load_movies(file_path: str):
    movies = []
    with open(file_path, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            line = line.strip()

            if not line:
                continue

            parts = line.split(",", 2)
            if len(parts) < 3:
                raise ValueError(f"Incorrect line format: {line}")

            movie = Movie(parts[0], parts[1], parts[2])
            movies.append(movie.__dict__)

    return movies
