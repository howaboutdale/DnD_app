CREATE DATABASE dnd_app_db;
\c dnd_app_db

-- Break this into different tables me thinks || At least that's everything from the first page of a character sheet!
CREATE TABLE sheets (
    id SERIAL PRIMARY KEY,
    character_name TEXT,
    class_and_level TEXT,
    background TEXT,
    player_name TEXT,
    race TEXT,
    alignment TEXT,
    experience_points TEXT,
    stat_str TEXT,
    stat_dex TEXT,
    stat_con TEXT,
    stat_int TEXT,
    stat_wis TEXT,
    stat_cha TEXT,
    passive_perception TEXT,
    svgthrow_stat_str TEXT,
    svgthrow_stat_dex TEXT,
    svgthrow_stat_con TEXT,
    svgthrow_stat_int TEXT,
    svgthrow_stat_wis TEXT,
    svgthrow_stat_cha TEXT,
    prof_bonus TEXT,
    sk_acroba TEXT,
    sk_animal TEXT,
    sk_arcana TEXT,
    sk_athlet TEXT,
    sk_decept TEXT,
    sk_histor TEXT,
    sk_insigh TEXT,
    sk_intimi TEXT,
    sk_invest TEXT,
    sk_medici TEXT,
    sk_nature TEXT,
    sk_percep TEXT,
    sk_perfor TEXT,
    sk_persua TEXT,
    sk_religi TEXT,
    sk_sleigh TEXT,
    sk_stealt TEXT,
    sk_suviva TEXT,
    otr_prof_lang TEXT,
    armor TEXT,
    initiative TEXT,
    speed TEXT,
    current_hp TEXT,
    temp_hp TEXT,
    hit_dice TEXT,
    dthsv_pass TEXT,
    dthsv_fail TEXT,
    attacks_spells TEXT,
    equipment TEXT,
    traits TEXT,
    ideals TEXT,
    bonds TEXT,
    flaws TEXT,
    fluff TEXT,
    spellcasting_class TEXT,
    spellcasting_ability TEXT,
    spell_save_dc TEXT,
    spell_atk_bonus TEXT,
    cantrips TEXT,
    first_level_spells TEXT,
    second_level_spells TEXT,
    third_level_spells TEXT,
    fourth_level_spells TEXT,
    fifth_level_spells TEXT,
    sixth_level_spells TEXT,
    seventh_level_spells TEXT,
    eighth_level_spells TEXT,
    ninth_level_spells TEXT,
    age TEXT,
    height TEXT,
    character_weight TEXT,
    eyes TEXT,
    skin TEXT,
    hair TEXT,
    appearance TEXT,
    allies_organisations TEXT,
    character_backstory TEXT,
    additional_features_traits TEXT,
    treasure TEXT
);

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password_digest TEXT
);

CREATE TABLE comments(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  sheet_id INTEGER
);