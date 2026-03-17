-- Explicit column list for backwards compatibility: current CSV has 28 columns,
-- metacritic_merged schema has 31 (country_dev, studio, editor added later).
-- country_dev / studio / editor will be NULL until build_metacritic_merged.py is re-run.
-- Once the CSV is regenerated with all 31 columns, this can be simplified to:
--   COPY public.metacritic_merged FROM '...' DELIMITER ',' CSV HEADER;
COPY public.metacritic_merged
    (id, game_name, console, game_type, finished,
     published_year, played_year, hours_played, perso_score, multiplayed,
     fuzz, game_title, game_platform, game_release_date,
     genre, publisher,
     na_sales, eu_sales, jp_sales, other_sales, global_sales,
     metascore, critic_count, user_score, user_count,
     developer, rating, game_summary)
FROM '/docker-entrypoint-initdb.d/csv_file/metacritic_merged_local.csv'
DELIMITER ','
CSV HEADER;
