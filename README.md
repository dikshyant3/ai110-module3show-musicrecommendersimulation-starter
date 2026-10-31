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

The recommender reads `data/songs.csv`. Each row represents a song, with identifying fields (`id`, `title`, and `artist`) and descriptive features: `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`. The current scoring design uses genre, mood, and energy; the other features are available for future experiments.

### User Preferences

The user's preferences are represented as a dictionary. For example:

```python
user_profile = {
    "favorite_genre": "rock",
    "favorite_mood": "intense",
    "target_energy": 0.8
}
```

The dataset includes `intense` but not `energetic`, so `intense` is a suitable example mood. The target energy is a user preference on the dataset's 0-to-1 scale, not a value inferred from the songs.

### Scoring Algorithm

```text
genre_score = 2.0 if song.genre equals favorite_genre, otherwise 0.0
mood_score = 1.0 if song.mood equals favorite_mood, otherwise 0.0
energy_similarity = 1 - abs(song.energy - target_energy)

score = genre_score + mood_score + energy_similarity
```

Genre and mood matches receive fixed points; energy contributes a similarity value. The score is not normalized, and genre and mood together can outweigh energy.

For example, `Storm Runner` is rock, intense, and has energy 0.91. For a profile that prefers rock, intense, and target energy 0.90, its score is `2.0 + 1.0 + (1 - abs(0.91 - 0.90)) = 3.99`.

### Ranking and Top K

Calculate a score for every song, sort songs from highest score to lowest, and return the first `K` songs. Equal scores retain the songs' original dataset order.

```text
User Preferences → Read songs.csv → Evaluate Each Song
                 → Calculate Similarity Score → Rank Songs
                 → Return Top K Recommendations
```

For each song, the system reads its genre, mood, and energy; compares those values with the user's preferences; and calculates one score. A close energy value increases the energy component, while matching genre and mood add their fixed point contributions. The resulting score determines how high that song appears when all songs are ranked.

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

The command-line runner evaluates three profiles with genres, moods, and energy values represented in the dataset. Scores and reasons below are the actual output of `python3 src/main.py`.

```text
Top recommendations for High-Energy Pop (pop / happy, target energy: 0.90):

1. Sunrise City (score: 3.92)
   Reasons:
   - genre match (+2.0)
   - mood match (+1.0)
   - energy similarity (+0.9)

2. Gym Hero (score: 2.97)
   Reasons:
   - genre match (+2.0)
   - mood mismatch (+0.0)
   - energy similarity (+1.0)

3. Rooftop Lights (score: 1.86)
   Reasons:
   - genre mismatch (+0.0)
   - mood match (+1.0)
   - energy similarity (+0.9)

4. Storm Runner (score: 0.99)
   Reasons:
   - genre mismatch (+0.0)
   - mood mismatch (+0.0)
   - energy similarity (+1.0)

5. Neon Mirage (score: 0.98)
   Reasons:
   - genre mismatch (+0.0)
   - mood mismatch (+0.0)
   - energy similarity (+1.0)

Top recommendations for Chill Lofi (lofi / chill, target energy: 0.40):

1. Midnight Coding (score: 3.98)
   Reasons:
   - genre match (+2.0)
   - mood match (+1.0)
   - energy similarity (+1.0)

2. Library Rain (score: 3.95)
   Reasons:
   - genre match (+2.0)
   - mood match (+1.0)
   - energy similarity (+0.9)

3. Focus Flow (score: 3.00)
   Reasons:
   - genre match (+2.0)
   - mood mismatch (+0.0)
   - energy similarity (+1.0)

4. Spacewalk Thoughts (score: 1.88)
   Reasons:
   - genre mismatch (+0.0)
   - mood match (+1.0)
   - energy similarity (+0.9)

5. Lunar Postcard (score: 0.98)
   Reasons:
   - genre mismatch (+0.0)
   - mood mismatch (+0.0)
   - energy similarity (+1.0)

Top recommendations for Deep Intense Rock (rock / intense, target energy: 0.90):

1. Storm Runner (score: 3.99)
   Reasons:
   - genre match (+2.0)
   - mood match (+1.0)
   - energy similarity (+1.0)

2. Gym Hero (score: 1.97)
   Reasons:
   - genre mismatch (+0.0)
   - mood match (+1.0)
   - energy similarity (+1.0)

3. Neon Mirage (score: 0.98)
   Reasons:
   - genre mismatch (+0.0)
   - mood mismatch (+0.0)
   - energy similarity (+1.0)

4. Glass Cathedral (score: 0.94)
   Reasons:
   - genre mismatch (+0.0)
   - mood mismatch (+0.0)
   - energy similarity (+0.9)

5. Sunrise City (score: 0.92)
   Reasons:
   - genre mismatch (+0.0)
   - mood mismatch (+0.0)
   - energy similarity (+0.9)
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
