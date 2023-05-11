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
    fluff
):sql('INSERT INTO sheets(character_name, class_and_level, background, player_name, race, alignment, experience_points, stat_str, stat_dex, stat_con, stat_int, stat_wis, stat_cha, passive_perception, svgthrow_stat_str, svgthrow_stat_dex, svgthrow_stat_con, svgthrow_stat_int, svgthrow_stat_wis, svgthrow_stat_cha, sk_acroba, sk_animal, sk_arcana, sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva, otr_prof_lang, armor, initiative, speed, current_hp, temp_hp, hit_dice, dthsv_pass, dthsv_fail, attacks_spells, equipment, traits, ideals, bonds, flaws, fluff) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *', [character_name, class_and_level, background, player_name, race, alignment, experience_points, stat_str, stat_dex, stat_con, stat_int, stat_wis, stat_cha, passive_perception, svgthrow_stat_str, svgthrow_stat_dex, svgthrow_stat_con, svgthrow_stat_int, svgthrow_stat_wis, svgthrow_stat_cha, sk_acroba, sk_animal, sk_arcana, sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva, otr_prof_lang, armor, initiative, speed, current_hp, temp_hp, hit_dice, dthsv_pass, dthsv_fail, attacks_spells, equipment, traits, ideals, bonds, flaws, fluff])


def update_sheet(id, name, image_url, diameter, distance, mass, moon_count):
    sql('UPDATE sheets SET name=%s, image_url=%s, diameter=%s, distance=%s, mass=%s, moon_count=%s WHERE id=%s RETURNING *', [name, image_url, diameter, distance, mass, moon_count, id])

def delete_sheet(id):
    sql('DELETE FROM sheets WHERE id=%s RETURNING *', [id])





    #sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva
        #svgthrow_stat_str, svgthrow_stat_dex, svgthrow_stat_con, svgthrow_stat_int, svgthrow_stat_wis, svgthrow_stat_cha, sk_acroba, sk_animal, sk_arcana, sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva
    # otr_prof_lang, armor, initiative, speed, current_hp, temp_hp, hit_dice, dthsv_pass, dthsv_fail, attacks_spells, equipment, traits, ideals, bonds, flaws, fluff
