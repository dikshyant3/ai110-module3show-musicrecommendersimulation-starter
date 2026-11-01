# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch: Music Recommender Simulation**

---

## 2. Goal, Intended Use, and Non-Intended Use

VibeMatch ranks songs for a listener using genre, mood, energy, popularity, release decade, detailed mood, instrumentalness, and speechiness preferences. It is designed for classroom experiments that show how preferences and scoring rules affect recommendations. It is not intended for real-world music discovery or decisions about people; the catalog is small, the values are simulated, and the scoring rules have not been tested with listeners.

---

## 3. Algorithm Summary

The system gives a song 2 points for a genre match and 1 point for a mood match, then adds energy similarity. It also adds popularity similarity (weighted by 0.4), an exact release-decade match (0.4), an exact detailed-mood match (0.6), instrumentalness similarity (weighted by 0.3), and speechiness similarity (weighted by 0.3). Similarity is one minus the absolute difference for 0-to-1 features, and one minus the absolute popularity difference divided by 100. The total score is not normalized; the system returns the highest-scoring songs and reports the contribution of every feature.

---

## 4. Data Used

The CSV catalog contains 18 songs. Each row has a title, artist, genre, mood, energy, tempo, valence, danceability, acousticness, popularity, release decade, detailed mood, instrumentalness, and speechiness, as well as an ID. The catalog has 15 genres and 14 moods. Lofi appears 3 times, pop appears 2 times, and the other 13 genres appear once each. Chill appears 3 times, happy and intense appear twice each, and the other 11 moods appear once each. Song energy ranges from 0.24 to 0.96; popularity ranges from 39 to 88; release decades span 2000 to 2020. All five advanced features are used by the scorer. Tempo, valence, danceability, and acousticness are available but not used in the current scoring rule.

---

## 5. Strengths

The system clearly rewards exact genre and mood matches. In the tested Chill Lofi profile, Midnight Coding and Library Rain, both lofi and chill, ranked first and second. For Deep Intense Rock, Storm Runner, the only rock song and an intense song with energy 0.91, ranked first for the target energy of 0.90.

---

## 6. Observed Behavior and Bias

The catalog is sparse: 13 of its 15 genres and 11 of its 14 moods appear only once, so many preferences have few matching choices. The 2-point genre bonus can outweigh the individual similarity terms. Songs without the preferred genre or mood still enter the high-energy profiles' top five; this reflects their strong energy and advanced-feature contributions, and may limit variety. Popularity and categorical bonuses are simple hand-set rules, not learned preferences.

---

## 7. Evaluation Process

I ran three profiles against the same song catalog:

- **High-Energy Pop:** pop, happy, target energy 0.90, popularity 80, 2020s, euphoric, instrumentalness 0.05, speechiness 0.05. Top five: Sunrise City (5.90), Gym Hero (4.32), Rooftop Lights (3.20), Neon Mirage (2.31), Concrete Bloom (2.27).
- **Chill Lofi:** lofi, chill, target energy 0.40, popularity 55, 2020s, cozy, instrumentalness 0.20, speechiness 0.04. Top five: Midnight Coding (5.96), Library Rain (5.30), Focus Flow (4.33), Spacewalk Thoughts (2.60), Coffee Shop Stories (1.93).
- **Deep Intense Rock:** rock, intense, target energy 0.90, popularity 65, 2020s, defiant, instrumentalness 0.05, speechiness 0.06. Top five: Storm Runner (5.55), Gym Hero (3.27), Glass Cathedral (2.31), Neon Mirage (2.25), Sunrise City (2.23).

Pop and Chill Lofi share no songs in their top five. Pop and Deep Intense Rock share three: Gym Hero, Neon Mirage, and Sunrise City. Chill Lofi and Deep Intense Rock share none. The Pop and Rock overlap fits their shared 0.90 energy target and shared 2020s preference. Their category preferences still affect the top spot: Sunrise City matches Pop, happy, and euphoric for Pop, while Storm Runner matches rock, intense, and defiant for Rock.

The earlier Weight Shift experiment used the genre/mood/energy-only scorer, before the five advanced features were added. It changed the genre weight from +2 to +1 and energy similarity from x1 to x2. No song changed position in any profile's top five, but scores changed: Pop's Rooftop Lights went from 1.86 to 2.72, and Sunrise City went from 3.92 to 3.84. The experiment was different, but the results do not show that it was better. After restoring the original weights, I ran the recommender again and confirmed that the original top-five lists and scores returned.

---

## 8. Ideas for Improvement

- Add more songs for each genre and mood so profiles have more meaningful alternatives.
- Test other scoring weights with more profiles and listener feedback before choosing a preferred balance.
- Try using existing dataset features such as tempo, valence, danceability, or acousticness, and check whether they improve recommendations.

---

## 9. Personal Reflection

One of my biggest learning moments was seeing how weights shape recommendations: the original genre, mood, and energy contributions remain, and five additional simulated features now add up to two points. This demonstrated how new signals can change ranks and make the reasons more detailed, while still following simple hand-set rules.

I used an AI coding assistant to help me understand the scoring behavior and organize the model-card documentation. I still needed to check suggestions against the scorer, song data, and actual terminal output, especially when verifying scores and whether the ranking changed. I was surprised that songs with no genre or mood match could still reach a top five because their energy was close to the target.

If I continued this project, I would add more songs so each genre and mood had alternatives, test more user profiles and weights, and experiment with features such as tempo or acousticness. I would compare the results carefully to see whether these changes improve recommendations, not just change the scores.
