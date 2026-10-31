# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Implement Challenge 1: add five simulated song attributes, use them in recommendation scoring with explanations, update the sample user profiles, run the app and tests, and record the AI interaction and manual verification.

**Prompts used:**

> Review `data/songs.csv`, `src/recommender.py`, `src/main.py`, and `ai_interactions.md`. Add at least five new song attributes while preserving existing songs and columns; update CSV loading and scoring to use the attributes with explanations; preserve genre, mood, and energy scoring; test with `python src/main.py`; and document the prompt, generated changes, and manual verification.

> For Challenge 2, add Genre-First and Mood-First scoring modes using a simple Strategy pattern, let users select the mode in `src/main.py`, preserve existing features and explanations, run the module with both modes, and document actual verification.

**What did the agent generate or change?**

Added `popularity`, `release_decade`, `detailed_mood`, `instrumentalness`, and `speechiness` to the existing 18-song dataset. Updated `load_songs()` to convert numeric values, `score_song()` to include all five features, and the three demo profiles to provide corresponding preferences. Added regression tests for conversion, per-feature score effects, and descending recommendation order. Updated the README and model card to describe the new scoring behavior.

For Challenge 2, added two interchangeable category-weight strategies, made the scoring API and CLI accept a mode, and updated imports so the documented `python -m src.main` form works from the repository root. Added tests proving the modes apply opposite category weights and return descending rankings.

**What did you verify or fix manually?**

Confirmed that the pre-existing song rows and columns, including `danceability` and `acousticness`, were retained; the five added fields are new to this working copy. Changed values for each new feature individually in a test and confirmed every change lowered the matching song's score. Confirmed explanations include each feature and that the top-five scores are descending. Pylance caught a syntax error during the scoring-reason edit; it was corrected before final validation. `./.venv/bin/python -m pytest -q` passed all 6 tests. `python src/main.py`, run with the project's virtual environment activated, evaluated all three profiles and kept their expected genre/mood matches at the top. Pylance reported no syntax errors and `git diff --check` passed. The shell did not have `python` on `PATH` unless the virtual environment was activated.

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

Challenge 2 uses the `ScoringStrategy` dataclass as the interchangeable strategy: `Genre-First` applies genre/mood weights of 2.0/1.0, while `Mood-First` uses 1.0/2.0. The shared `_score_song()` function applies that strategy and calculates all other song-feature contributions once, preserving the existing explanations. `score_song()` and `recommend_songs()` accept a mode, and `src/main.py` exposes it as `--mode`.

**How did AI help you brainstorm or implement it?**

The AI recommended the Strategy pattern because the modes differ in just two weights while sharing every other scoring rule. Keeping category weights in a small strategy object avoids copying the scoring function and lets the CLI select a strategy. I reviewed this against the existing scorer and kept Genre-First's weights at the prior 2.0/1.0 values so it remains the default.

**What changed and what did you verify?**

Added Genre-First and Mood-First scoring strategies, CLI mode selection, and module-compatible imports so both `python -m src.main --mode genre-first` and `python -m src.main --mode mood-first` work from the project root. Added tests that check category-specific weights, recommendation ordering in both modes, and explanations.

Ran both module commands with the project virtual environment. Genre-First ranked Gym Hero above Rooftop Lights for High-Energy Pop (4.32 vs. 3.20); Mood-First reversed them (3.32 vs. 4.20). For Chill Lofi, Genre-First put Focus Flow above Spacewalk Thoughts (4.33 vs. 2.60), while Mood-First put Spacewalk Thoughts above Focus Flow (3.60 vs. 3.33). Matching both genre and mood kept Sunrise City, Midnight Coding, and Storm Runner at the top of their respective profiles in both modes. All 7 tests passed; Pylance reported no syntax errors and `git diff --check` passed. The changes are on `experiment/mood-first`; they were not committed or pushed.
