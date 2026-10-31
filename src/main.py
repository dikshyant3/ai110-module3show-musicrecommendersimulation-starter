"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import argparse

if __package__:
    from .recommender import load_songs, recommend_songs
else:
    from recommender import load_songs, recommend_songs


def main() -> None:
    parser = argparse.ArgumentParser(description="Recommend songs by scoring mode.")
    parser.add_argument(
        "--mode",
        choices=("genre-first", "mood-first"),
        default="genre-first",
        help="Ranking strategy to use (default: genre-first).",
    )
    mode = parser.parse_args().mode

    songs = load_songs("data/songs.csv") 

    profiles = [
        (
            "High-Energy Pop",
            {
                "favorite_genre": "pop",
                "favorite_mood": "happy",
                "target_energy": 0.9,
                "target_popularity": 80,
                "preferred_release_decade": 2020,
                "preferred_detailed_mood": "euphoric",
                "target_instrumentalness": 0.05,
                "target_speechiness": 0.05,
            },
        ),
        (
            "Chill Lofi",
            {
                "favorite_genre": "lofi",
                "favorite_mood": "chill",
                "target_energy": 0.4,
                "target_popularity": 55,
                "preferred_release_decade": 2020,
                "preferred_detailed_mood": "cozy",
                "target_instrumentalness": 0.2,
                "target_speechiness": 0.04,
            },
        ),
        (
            "Deep Intense Rock",
            {
                "favorite_genre": "rock",
                "favorite_mood": "intense",
                "target_energy": 0.9,
                "target_popularity": 65,
                "preferred_release_decade": 2020,
                "preferred_detailed_mood": "defiant",
                "target_instrumentalness": 0.05,
                "target_speechiness": 0.06,
            },
        ),
    ]

    print(f"Scoring mode: {mode.title()}")
    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5, mode=mode)

        print(
            f"\nTop recommendations for {profile_name} "
            f"({user_prefs['favorite_genre']} / {user_prefs['favorite_mood']}, "
            f"target energy: {user_prefs['target_energy']:.2f}):\n"
        )
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} (score: {score:.2f})")
            print("   Reasons:")
            for reason in explanation.split("; "):
                print(f"   - {reason}")
            print()


if __name__ == "__main__":
    main()
