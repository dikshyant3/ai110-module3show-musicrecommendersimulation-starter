"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import argparse
import textwrap
from typing import Dict, List, Tuple

if __package__:
    from .recommender import load_songs, recommend_songs
else:
    from recommender import load_songs, recommend_songs


def _format_recommendation_table(
    recommendations: List[Tuple[Dict, float, str]]
) -> str:
    headers = ("Rank", "Song Title", "Artist", "Final Score", "Recommendation Reasons")
    rows = [
        (
            str(rank),
            song["title"],
            song["artist"],
            f"{score:.2f}",
            [
                line
                for reason in explanation.split("; ")
                for line in textwrap.wrap(reason, width=55) or [""]
            ],
        )
        for rank, (song, score, explanation) in enumerate(recommendations, start=1)
    ]
    widths = [
        max(len(headers[index]), *(len(row[index]) for row in rows))
        for index in range(len(headers) - 1)
    ]
    widths.append(
        max(len(headers[-1]), *(len(line) for row in rows for line in row[-1]))
    )

    def format_row(row: Tuple[str, ...]) -> str:
        return "| " + " | ".join(
            value.ljust(widths[index]) for index, value in enumerate(row)
        ) + " |"

    separator = "+-" + "-+-".join("-" * width for width in widths) + "-+"
    table_lines = [separator, format_row(headers), separator]
    for row in rows:
        reason_lines = row[4]
        table_lines.append(format_row((*row[:4], reason_lines[0])))
        table_lines.extend(
            format_row(("", "", "", "", reason_line))
            for reason_line in reason_lines[1:]
        )
    table_lines.append(separator)
    return "\n".join(table_lines)


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
        print(_format_recommendation_table(recommendations))
        print()


if __name__ == "__main__":
    main()
