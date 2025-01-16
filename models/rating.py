class Rating:
    def __init__(self, userId: str, movieId: str, rating: str, timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


def load_ratings(file_path: str):
    ratings = []
    with open(file_path, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            line = line.strip()

            if not line:
                continue

            parts = line.split(",", 3)
            if len(parts) < 4:
                raise ValueError(f"Incorrect line format: {line}")

            rate = Rating(parts[0], parts[1], parts[2], parts[3])
            ratings.append(rate.__dict__)

    return ratings
