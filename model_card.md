# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch: Music Recommender Simulation**

---

## 2. Goal, Intended Use, and Non-Intended Use

VibeMatch ranks songs for a listener using their favorite genre, favorite mood, and target energy. It is designed for classroom experiments that show how preferences and scoring rules affect recommendations. It assumes the listener can be described by those three preferences. It is not intended for real-world music discovery or decisions about people; the catalog is small, and the scoring rules have not been tested with listeners.

---

## 3. Algorithm Summary

The system gives a song 2 points when its genre matches the listener's favorite genre, and 1 point when its mood matches. It adds energy similarity: one minus the absolute difference between the song's energy and the listener's target energy. The total is the song's score; the system returns the highest-scoring songs and reports the matching reasons. The scorer uses only genre, mood, and energy.

---

## 4. Data Used

The CSV catalog contains 18 songs. Each row has a title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness, as well as an ID. The catalog has 15 genres and 14 moods. Lofi appears 3 times, pop appears 2 times, and the other 13 genres appear once each. Chill appears 3 times, happy and intense appear twice each, and the other 11 moods appear once each. Song energy ranges from 0.24 to 0.96. The scorer does not use tempo, valence, danceability, or acousticness, and the small catalog has few alternatives for most genres and moods.

---

## 5. Strengths

The system clearly rewards exact genre and mood matches. In the tested Chill Lofi profile, Midnight Coding and Library Rain, both lofi and chill, ranked first and second. For Deep Intense Rock, Storm Runner, the only rock song and an intense song with energy 0.91, ranked first for the target energy of 0.90.

---

## 6. Observed Behavior and Bias

The catalog is sparse: 13 of its 15 genres and 11 of its 14 moods appear only once, so many preferences have few matching choices. The 2-point genre bonus can outweigh energy similarity, which contributes at most 1 point for the tested energy range. Songs without the preferred genre or mood still entered the high-energy profiles' top five; for example, Neon Mirage ranked fifth for Pop and third for Rock because its energy is close to 0.90. This may limit variety and make recommendations depend heavily on the categories represented in this small dataset.

---

## 7. Evaluation Process

I ran three profiles against the same song catalog:

- **High-Energy Pop:** pop, happy, target energy 0.90. Top five: Sunrise City (3.92), Gym Hero (2.97), Rooftop Lights (1.86), Storm Runner (0.99), Neon Mirage (0.98).
- **Chill Lofi:** lofi, chill, target energy 0.40. Top five: Midnight Coding (3.98), Library Rain (3.95), Focus Flow (3.00), Spacewalk Thoughts (1.88), Lunar Postcard (0.98).
- **Deep Intense Rock:** rock, intense, target energy 0.90. Top five: Storm Runner (3.99), Gym Hero (1.97), Neon Mirage (0.98), Glass Cathedral (0.94), Sunrise City (0.92).

Pop and Chill Lofi share no songs in their top five. Pop and Deep Intense Rock share four: Storm Runner, Gym Hero, Neon Mirage, and Sunrise City. Chill Lofi and Deep Intense Rock share none. The Pop and Rock overlap fits their shared 0.90 energy target. Their category preferences still affect the top spot: Sunrise City matches Pop and happy for Pop, while Storm Runner matches rock and intense for Rock. A surprising result is that songs matching neither category can still rank highly when their energy is close to the target.

In the Weight Shift experiment, the original weights were genre +2, mood +1, and energy similarity multiplied by 1. The experimental weights were genre +1, mood +1, and energy similarity multiplied by 2. No song changed position in any profile's top five, but scores changed: Pop's Rooftop Lights went from 1.86 to 2.72, and Sunrise City went from 3.92 to 3.84. The experiment was different, but the results do not show that it was better. After restoring the original weights, I ran the recommender again and confirmed that the original top-five lists and scores returned.

---

## 8. Ideas for Improvement

- Add more songs for each genre and mood so profiles have more meaningful alternatives.
- Test other scoring weights with more profiles and listener feedback before choosing a preferred balance.
- Try using existing dataset features such as tempo, valence, danceability, or acousticness, and check whether they improve recommendations.

---

## 9. Personal Reflection

One of my biggest learning moments was seeing how the weights shape recommendations: a genre match adds two points, mood adds one, and energy similarity adds at most one. In Phase 4, doubling the energy weight and lowering the genre weight changed some scores, but did not change the top-five order for any of the three profiles. That showed me how a system can seem personalized while still following a small set of simple rules.

I used an AI coding assistant to help me understand the scoring behavior and organize the model-card documentation. I still needed to check suggestions against the scorer, song data, and actual terminal output, especially when verifying scores and whether the ranking changed. I was surprised that songs with no genre or mood match could still reach a top five because their energy was close to the target.

If I continued this project, I would add more songs so each genre and mood had alternatives, test more user profiles and weights, and experiment with features such as tempo or acousticness. I would compare the results carefully to see whether these changes improve recommendations, not just change the scores.
