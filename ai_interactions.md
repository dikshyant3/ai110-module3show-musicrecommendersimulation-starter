# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Implement Challenge 1: add five simulated song attributes, use them in recommendation scoring with explanations, update the sample user profiles, run the app and tests, and record the AI interaction and manual verification.

**Prompts used:**

> Review `data/songs.csv`, `src/recommender.py`, `src/main.py`, and `ai_interactions.md`. Add at least five new song attributes while preserving existing songs and columns; update CSV loading and scoring to use the attributes with explanations; preserve genre, mood, and energy scoring; test with `python src/main.py`; and document the prompt, generated changes, and manual verification.

**What did the agent generate or change?**

Added `popularity`, `release_decade`, `detailed_mood`, `instrumentalness`, and `speechiness` to the existing 18-song dataset. Updated `load_songs()` to convert numeric values, `score_song()` to include all five features, and the three demo profiles to provide corresponding preferences. Added regression tests for conversion, per-feature score effects, and descending recommendation order. Updated the README and model card to describe the new scoring behavior.

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

<!-- Point to the relevant class or method -->
