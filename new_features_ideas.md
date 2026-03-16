# New Feature Ideas for Gaming of a Lifetime

This document lists potential features and visualizations to be added to the Gaming of a Lifetime analytics dashboard.

---

## 1. Personal GOTY vs. Critical Consensus
*   **Goal:** Identify your personal "Game of the Year" for each release year and compare it with the highest-rated game by critics (Metacritic).
*   **Data Requirements:**
    *   `gaming_lifetime`: `published_year`, `game_name`, `perso_score`.
    *   `metacritic`: `year_of_release`, `game_name`, `metascore`.
*   **Logic:**
    1.  Group `gaming_lifetime` by `published_year` and find the entry with the maximum `perso_score`.
    2.  Group `metacritic` by `year_of_release` and find the entry with the maximum `metascore`.
    3.  Merge both results on the year to see where your taste aligns or diverges from the press.
*   **Visualization:** A comparison table or "Versus" cards showing the personal winner vs. the critical winner for each year.

---

## 2. Console Genre "Radar" (Spider Chart)
*   **Goal:** Visualize the unique "identity" of each console in your collection (e.g., is your Switch a "Platformer machine" vs. your PC as a "Strategy hub"?).
*   **Data Requirements:**
    *   `gaming_lifetime`: `console`, `game_type` (multi-genres split by `|`), `hours_played`.
*   **Logic:**
    1.  Explode the `game_type` column to handle multi-genre entries.
    2.  Sum `hours_played` per console and per genre.
    3.  Normalize data (percentage of total console time) to allow comparison between consoles with different usage levels.
*   **Visualization:** A Radar Chart (Spider Chart) with genres as axes. Overlapping shapes for different consoles or a dropdown to switch between them.

---

## 3. Gaming Efficiency (HLTB vs. Reality)
*   **Goal:** Determine your player profile: are you a "Speedrunner" (finishing faster than average) or a "Wanderer" (taking your time)?
*   **Data Requirements:**
    *   `gaming_lifetime`: `game_name`, `hours_played`.
    *   `how_long_to_beat`: `comp_main` (Main Story time) or `comp_plus`.
*   **Logic:**
    1.  Calculate the ratio: `hours_played / comp_main`.
    2.  Ratio < 1.0: Efficient/Speedrun profile.
    3.  Ratio > 1.5: Explorer/Completionist profile.
*   **Visualization:** A Scatter Plot with HLTB time on the X-axis and Personal time on the Y-axis. A diagonal line represents the average; points above/below show deviation.

---

## 4. Global Development Map (World Map)
*   **Goal:** Visualize the geographic origin of your favorite games and identify regional trends.
*   **Data Requirements:**
    *   `gaming_lifetime`: `country_dev`, `game_name`, `perso_score`.
*   **Logic:**
    1.  Count games per country.
    2.  Calculate average `perso_score` per country to see which region produces your highest-rated experiences.
*   **Visualization:** An interactive Choropleth Map (World Map) where color intensity represents game count or average score.

---

## 5. Evolution of Taste (Streamgraph)
*   **Goal:** Track how your preferred genres have shifted over decades (e.g., more Platformers in childhood, more RPGs/Strategy in adulthood).
*   **Data Requirements:**
    *   `gaming_lifetime`: `played_year`, `game_type`.
*   **Logic:**
    1.  Calculate the distribution (%) of genres for each `played_year`.
    2.  Smooth the data over time to show transitions.
*   **Visualization:** A Streamgraph (flowing stacked area chart) showing the "flow" of genres across your gaming timeline.

---

## 6. Hidden Gems Detector
*   **Goal:** Identify games you loved (`perso_score` high) but were overlooked by the public (low sales) or underrated by critics.
*   **Data Requirements:**
    *   `gaming_lifetime`: `perso_score`.
    *   `metacritic`: `metascore`, `global_sales`.
*   **Logic:**
    1.  Filter games where `perso_score` is high (e.g., > 80).
    2.  Isolate cases where `perso_score` is significantly higher than `metascore` or where `global_sales` are very low.
    3.  Calculate the "Discovery Value": `perso_score - metascore`.
*   **Visualization:** A Bubble Chart where bubble size represents `perso_score`, X-axis is `metascore`, and Y-axis is `global_sales`.

---

## 7. Studio Loyalty Index
*   **Goal:** Determine which developer or publisher is your "safe bet" based on your historical data.
*   **Data Requirements:**
    *   `gaming_lifetime`: `studio`, `editor`, `perso_score`.
*   **Logic:**
    1.  Group by `studio` and calculate average `perso_score` and count of games played.
    2.  Create a "Loyalty Score" that weights both the frequency of play and the average quality.
*   **Visualization:** A Lollipop Chart showing average score per studio, with the size of the bubble representing the number of games played.

---

## 8. Churn & Abandonment Analysis
*   **Goal:** Understand the patterns behind why you stop playing certain games (is it the genre, the platform, or the time investment?).
*   **Data Requirements:**
    *   `gaming_lifetime`: `finished`, `game_type`, `hours_played`, `console`.
*   **Logic:**
    1.  Compare abandonment rates (`finished = False`) across different genres and consoles.
    2.  Analyze the "Threshold of Boredom": the average `hours_played` before a game is abandoned.
*   **Visualization:** A Sankey Diagram showing the flow from "Game Started" through "Genre" to the final state of "Finished" or "Abandoned".

---

## 9. Nostalgia vs. Modernity Factor
*   **Goal:** See if you tend to rate "Retro" games (played years after release) higher than "Day-One" modern releases.
*   **Data Requirements:**
    *   `gaming_lifetime`: `published_year`, `played_year`, `perso_score`.
*   **Logic:**
    1.  Calculate the `delay = played_year - published_year`.
    2.  Categorize games: "Day-One" (0-1 year delay), "Backlog" (2-5 years), "Retro" (10+ years).
    3.  Compare average scores across these categories.
*   **Visualization:** A Heatmap or Box Plot showing the distribution of `perso_score` based on the gap between release and play dates.

---

## 10. Franchise Deep Dive (Saga Evolution)
*   **Goal:** Track the quality and your interest level across major video game series over time.
*   **Data Requirements:**
    *   `gaming_lifetime`: `game_name`, `perso_score`, `published_year`.
*   **Logic:**
    1.  Use keyword matching/grouping to aggregate games into franchises (e.g., "Final Fantasy", "Zelda", "Resident Evil").
    2.  Plot the trajectory of your personal scores over the chronological release of the saga.
*   **Visualization:** A Multi-series Line Chart where each line represents a franchise, showing the "peaks and valleys" of the series according to your taste.

---

## Future Considerations
*   **Studio Hall of Fame:** Ranking developers (e.g., Nintendo, Rockstar) by average personal score.
*   **Backlog Predictor:** Suggesting the next game to play from `finished = False` based on current genre preferences and available HLTB time.
*   **Franchise Deep Dive:** Aggregating scores and hours for major series (Final Fantasy, Zelda, etc.).
