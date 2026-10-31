import csv
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load song records from a CSV file."""
    path = Path(csv_path)
    if not path.is_absolute() and not path.is_file():
        path = Path(__file__).resolve().parent.parent / path

    with path.open(newline="", encoding="utf-8") as csv_file:
        songs = []
        for row in csv.DictReader(csv_file):
            row["id"] = int(row["id"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            for field in ("energy", "valence", "danceability", "acousticness"):
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and explain the score."""
    genre_match = song["genre"] == user_prefs["favorite_genre"]
    mood_match = song["mood"] == user_prefs["favorite_mood"]
    energy_similarity = 1 - abs(song["energy"] - user_prefs["target_energy"])

    genre_score = 2.0 if genre_match else 0.0
    mood_score = 1.0 if mood_match else 0.0
    energy_score = energy_similarity
    score = genre_score + mood_score + energy_score

    reasons = [
        f"genre {'match' if genre_match else 'mismatch'} (+{genre_score:.1f})",
        f"mood {'match' if mood_match else 'mismatch'} (+{mood_score:.1f})",
        f"energy similarity (+{energy_score:.1f})",
    ]
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top recommendations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, "; ".join(reasons)))

    return sorted(scored_songs, key=lambda recommendation: recommendation[1], reverse=True)[:k]
