-- Explicit column list for backwards compatibility: current CSV has 16 columns,
-- how_long_to_beat schema has 19 (country_dev, studio, editor added later).
-- country_dev / studio / editor will be NULL until import_hltb.py is re-run.
-- Once the CSV is regenerated with all 19 columns, this can be simplified to:
--   COPY public.how_long_to_beat FROM '...' DELIMITER ',' CSV HEADER;
COPY public.how_long_to_beat
    (id, game_name, console, game_type, finished,
     published_year, played_year, hours_played, perso_score, multiplayed,
     comp_100, comp_all, comp_main, comp_plus,
     platform, developer)
FROM '/docker-entrypoint-initdb.d/csv_file/hltb_scrap.csv'
DELIMITER ','
CSV HEADER;
