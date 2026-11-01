# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world music recommenders learn from user behavior, such as listening, liking, or skipping songs, and combine it with song attributes to personalize suggestions. This simulation uses content-based filtering: it compares each song's attributes with a user's stated preferences, scores the match, then ranks songs by score.

### Song Dataset and Features

The recommender reads `data/songs.csv`. Each row represents a song, with identifying fields (`id`, `title`, and `artist`) and descriptive features including `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness`, `popularity`, `release_decade`, `detailed_mood`, `instrumentalness`, and `speechiness`. The scoring design uses genre, mood, energy, and all five advanced features.

### User Preferences

The user's preferences are represented as a dictionary. For example:

```python
user_profile = {
    "favorite_genre": "rock",
    "favorite_mood": "intense",
    "target_energy": 0.90,
    "target_popularity": 65,
    "preferred_release_decade": 2020,
    "preferred_detailed_mood": "defiant",
    "target_instrumentalness": 0.05,
    "target_speechiness": 0.06
}
```

The dataset includes `intense` but not `energetic`, so `intense` is a suitable example mood. Energy, instrumentalness, and speechiness targets use a 0-to-1 scale; popularity uses 0-to-100; and release decade is represented by its starting year (for example, `2020`).

### Scoring Algorithm

```text
genre_score = 2.0 if song.genre equals favorite_genre, otherwise 0.0
mood_score = 1.0 if song.mood equals favorite_mood, otherwise 0.0
energy_similarity = 1 - abs(song.energy - target_energy)
popularity_similarity = 0.4 * (1 - abs(song.popularity - target_popularity) / 100)
release_decade_score = 0.4 if song.release_decade equals preferred_release_decade
detailed_mood_score = 0.6 if song.detailed_mood equals preferred_detailed_mood
instrumentalness_similarity = 0.3 * (1 - abs(song.instrumentalness - target_instrumentalness))
speechiness_similarity = 0.3 * (1 - abs(song.speechiness - target_speechiness))

score = genre_score + mood_score + energy_similarity + all five advanced-feature scores
```

Genre and mood matches receive fixed points; energy and the numeric advanced features contribute similarity values, while release decade and detailed mood receive exact-match bonuses. The maximum score is 5.0, but scores are not normalized and weights are simple simulation choices. Profiles that omit advanced preferences remain supported using neutral numeric defaults; omitted categorical preferences receive no bonus.

For the example profile above, `Storm Runner` is rock, intense, and defiant, with energy 0.91. It scores approximately 5.55 from its genre, mood, energy, popularity, detailed-mood, instrumentalness, and speechiness matches; its 2010 release decade does not match the preferred 2020s.

### Ranking and Top K

Calculate a score for every song, sort songs from highest score to lowest, and return the first `K` songs. Equal scores retain the songs' original dataset order.

```text
User Preferences → Read songs.csv → Evaluate Each Song
                 → Calculate Similarity Score → Rank Songs
                 → Return Top K Recommendations
```

For each song, the system compares its original and advanced features with the user's preferences and calculates one score. Matching genre, mood, release decade, and detailed mood add their contributions; closer numeric values increase similarity scores. The resulting score determines the song's position in the ranked list.

### Potential Biases and Limitations

- Genre and mood matches add up to three points, so exact category matches can outweigh energy similarity.
- Exact category matching can exclude a song with the preferred energy if its genre or mood differs. It also cannot recognize related labels or nuanced similarities (for example, `energetic` versus `intense`) unless those relationships are explicitly modeled.
- A small catalog may not contain good matches for every user, and repeatedly ranking similar songs can limit variety.
- The weights are design choices, not facts about every listener. They should be tested and adjusted using feedback from a broader set of users and songs.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python3 src/main.py
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

The command-line runner evaluates three profiles. These top-five rankings and scores are from `python src/main.py`; the program also prints a reason for each scoring contribution.

```text
High-Energy Pop: Sunrise City (5.90), Gym Hero (4.32), Rooftop Lights (3.20),
                 Neon Mirage (2.31), Concrete Bloom (2.27)
Chill Lofi:      Midnight Coding (5.96), Library Rain (5.30), Focus Flow (4.33),
                 Spacewalk Thoughts (2.60), Coffee Shop Stories (1.93)
Deep Intense Rock: Storm Runner (5.55), Gym Hero (3.27), Glass Cathedral (2.31),
                   Neon Mirage (2.25), Sunrise City (2.23)
```

---

## Experiments You Tried
The three tested profiles each placed songs matching both genre and mood at the top. In particular, the Chill Lofi profile ranked matching lofi/chill songs ahead of Focus Flow, which matches genre but not mood. The Deep Intense Rock profile ranked Storm Runner first with both category matches and close energy.

### Suggested Adversarial and Edge-Case Profiles

- **Conflicting genre and mood:** `{"favorite_genre": "metal", "favorite_mood": "chill", "target_energy": 0.20}` tests whether the high-energy metal track can still rank highly from its genre bonus despite conflicting mood and energy.
- **Unrepresented categories:** `{"favorite_genre": "disco", "favorite_mood": "euphoric", "target_energy": 0.50}` tests how recommendations fall back to energy similarity when neither categorical preference exists in the catalog.
- **Opposing energy preference:** `{"favorite_genre": "lofi", "favorite_mood": "chill", "target_energy": 1.00}` tests whether strong genre and mood matches outweigh the low energy of the matching songs.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
