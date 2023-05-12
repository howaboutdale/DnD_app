from db.db import sql

def all_sheets():
    return sql('SELECT * FROM sheets')

def get_sheets(id):
    sheets = sql('SELECT * FROM sheets WHERE id = %s', [id])
    return sheets[0]

# Need to change the parameters and the inserts into table
# gonna be a lot of arguments/parameters haha :(
# seperate into different functions?
# one for stats, include passive perception
# one for proficiencies/prof bonus and saving throws?
# one for armor class, init, speed weapons and spells?

def create_sheets(
    character_name,
    class_and_level,
    background,
    player_name,
    race,
    alignment,
    experience_points,
    stat_str,
    stat_dex,
    stat_con,
    stat_int,
    stat_wis,
    stat_cha,
    passive_perception,
    svgthrow_stat_str,
    svgthrow_stat_dex,
    svgthrow_stat_con,
    svgthrow_stat_int,
    svgthrow_stat_wis,
    svgthrow_stat_cha,
    prof_bonus,
    sk_acroba,
    sk_animal,
    sk_arcana,
    sk_athlet,
    sk_decept,
    sk_histor,
    sk_insigh,
    sk_intimi,
    sk_invest,
    sk_medici,
    sk_nature,
    sk_percep,
    sk_perfor,
    sk_persua,
    sk_religi,
    sk_sleigh,
    sk_stealt,
    sk_suviva,
    otr_prof_lang,
    armor,
    initiative,
    speed,
    current_hp,
    temp_hp,
    hit_dice,
    dthsv_pass,
    dthsv_fail,
    attacks_spells,
    equipment,
    traits,
    ideals,
    bonds,
    flaws,
    fluff,
    spellcasting_class,
    spellcasting_ability,
    spell_save_dc,
    spell_atk_bonus,
    cantrips,
    first_level_spells,
    second_level_spells,
    third_level_spells,
    fourth_level_spells,
    fifth_level_spells,
    sixth_level_spells,
    seventh_level_spells,
    eighth_level_spells,
    ninth_level_spells,
    age,
    height,
    character_weight,
    eyes,
    skin,
    hair,
    appearance,
    allies_organisations,
    character_backstory,
    additional_features_traits,
    treasure
):sql('INSERT INTO sheets(character_name, class_and_level, background, player_name, race, alignment, experience_points, stat_str, stat_dex, stat_con, stat_int, stat_wis, stat_cha, passive_perception, svgthrow_stat_str, svgthrow_stat_dex, svgthrow_stat_con, svgthrow_stat_int, svgthrow_stat_wis, svgthrow_stat_cha, prof_bonus, sk_acroba, sk_animal, sk_arcana, sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva, otr_prof_lang, armor, initiative, speed, current_hp, temp_hp, hit_dice, dthsv_pass, dthsv_fail, attacks_spells, equipment, traits, ideals, bonds, flaws, fluff, spellcasting_class, spellcasting_ability, spell_save_dc, spell_atk_bonus, cantrips, first_level_spells, second_level_spells, third_level_spells, fourth_level_spells, fifth_level_spells, sixth_level_spells, seventh_level_spells, eighth_level_spells, ninth_level_spells, age, height, character_weight, eyes, skin, hair, appearance, allies_organisations, character_backstory, additional_features_traits, treasure) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *', [character_name, class_and_level, background, player_name, race, alignment, experience_points, stat_str, stat_dex, stat_con, stat_int, stat_wis, stat_cha, passive_perception, svgthrow_stat_str, svgthrow_stat_dex, svgthrow_stat_con, svgthrow_stat_int, svgthrow_stat_wis, svgthrow_stat_cha, prof_bonus, sk_acroba, sk_animal, sk_arcana, sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva, otr_prof_lang, armor, initiative, speed, current_hp, temp_hp, hit_dice, dthsv_pass, dthsv_fail, attacks_spells, equipment, traits, ideals, bonds, flaws, fluff, spellcasting_class, spellcasting_ability, spell_save_dc, spell_atk_bonus, cantrips, first_level_spells, second_level_spells, third_level_spells, fourth_level_spells, fifth_level_spells, sixth_level_spells, seventh_level_spells, eighth_level_spells, ninth_level_spells, age, height, character_weight, eyes, skin, hair, appearance, allies_organisations, character_backstory, additional_features_traits, treasure])


def update_sheet(id, character_name, class_and_level, background, player_name, race, alignment, experience_points, stat_str, stat_dex, stat_con, stat_int, stat_wis, stat_cha, passive_perception, svgthrow_stat_str, svgthrow_stat_dex, svgthrow_stat_con, svgthrow_stat_int, svgthrow_stat_wis, svgthrow_stat_cha, prof_bonus, sk_acroba, sk_animal, sk_arcana, sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva, otr_prof_lang, armor, initiative, speed, current_hp, temp_hp, hit_dice, dthsv_pass, dthsv_fail, attacks_spells, equipment, traits, ideals, bonds, flaws, fluff, spellcasting_class, spellcasting_ability, spell_save_dc, spell_atk_bonus, cantrips, first_level_spells, second_level_spells, third_level_spells, fourth_level_spells, fifth_level_spells, sixth_level_spells, seventh_level_spells, eighth_level_spells, ninth_level_spells, age, height, character_weight, eyes, skin, hair, appearance, allies_organisations, character_backstory, additional_features_traits, treasure):
    sql('UPDATE sheets SET character_name=%s, class_and_level=%s, background=%s, player_name=%s, race=%s, alignment=%s, experience_points=%s, stat_str=%s, stat_dex=%s, stat_con=%s, stat_int=%s, stat_wis=%s, stat_cha=%s, passive_perception=%s, svgthrow_stat_str=%s, svgthrow_stat_dex=%s, svgthrow_stat_con=%s, svgthrow_stat_int=%s, svgthrow_stat_wis=%s, svgthrow_stat_cha=%s, prof_bonus=%s, sk_acroba=%s, sk_animal=%s, sk_arcana=%s, sk_athlet=%s, sk_decept=%s, sk_histor=%s, sk_insigh=%s, sk_intimi=%s, sk_invest=%s, sk_medici=%s, sk_nature=%s, sk_percep=%s, sk_perfor=%s, sk_persua=%s, sk_religi=%s, sk_sleigh=%s, sk_stealt=%s, sk_suviva=%s, otr_prof_lang=%s, armor=%s, initiative=%s, speed=%s, current_hp=%s, temp_hp=%s, hit_dice=%s, dthsv_pass=%s, dthsv_fail=%s, attacks_spells=%s, equipment=%s, traits=%s, ideals=%s, bonds=%s, flaws=%s, fluff=%s, spellcasting_class=%s, spellcasting_ability=%s, spell_save_dc=%s, spell_atk_bonus=%s, cantrips=%s, first_level_spells=%s, second_level_spells=%s, third_level_spells=%s, fourth_level_spells=%s, fifth_level_spells=%s, sixth_level_spells=%s, seventh_level_spells=%s, eighth_level_spells=%s, ninth_level_spells=%s, age=%s, height=%s, character_weight=%s, eyes=%s, skin=%s, hair=%s, appearance=%s, allies_organisations=%s, character_backstory=%s, additional_features_traits=%s, treasure=%s WHERE id=%s RETURNING *', [character_name, class_and_level, background, player_name, race, alignment, experience_points, stat_str, stat_dex, stat_con, stat_int, stat_wis, stat_cha, passive_perception, svgthrow_stat_str, svgthrow_stat_dex, svgthrow_stat_con, svgthrow_stat_int, svgthrow_stat_wis, svgthrow_stat_cha, prof_bonus, sk_acroba, sk_animal, sk_arcana, sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva, otr_prof_lang, armor, initiative, speed, current_hp, temp_hp, hit_dice, dthsv_pass, dthsv_fail, attacks_spells, equipment, traits, ideals, bonds, flaws, fluff, spellcasting_class, spellcasting_ability, spell_save_dc, spell_atk_bonus, cantrips, first_level_spells, second_level_spells, third_level_spells, fourth_level_spells, fifth_level_spells, sixth_level_spells, seventh_level_spells, eighth_level_spells, ninth_level_spells, age, height, character_weight, eyes, skin, hair, appearance, allies_organisations, character_backstory, additional_features_traits, treasure, id])

def delete_sheet(id):
    sql('DELETE FROM sheets WHERE id=%s RETURNING *', [id])





    #sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva
        #svgthrow_stat_str, svgthrow_stat_dex, svgthrow_stat_con, svgthrow_stat_int, svgthrow_stat_wis, svgthrow_stat_cha, sk_acroba, sk_animal, sk_arcana, sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva
    # otr_prof_lang, armor, initiative, speed, current_hp, temp_hp, hit_dice, dthsv_pass, dthsv_fail, attacks_spells, equipment, traits, ideals, bonds, flaws, fluff


    # %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,