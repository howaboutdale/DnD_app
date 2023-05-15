from flask import render_template, request, redirect, session
from models.home import all_sheets, get_sheets, create_sheets, update_sheet, delete_sheet, add_comment, all_comments, all_users
from services.session_info import current_user

def index():
    sheets = all_sheets()
    return render_template ('home/index.html', sheets=sheets, current_user=current_user)

# ----------------

def get_monster_from_api(api_monster):
    api_url = f'https://www.dnd5eapi.co/api/monsters/{api_monster}'
    response = request.get(api_url).json()
    return response

def get_from_api(api_monster):
    api_monster = request.args.get('monster') # this gets what is inputed on the srd page
    monster = get_monster_from_api(api_monster)
    return render_template('API.html', monster=monster)

# -------------

def gallery():
    comments = all_comments()
    sheets = all_sheets()
    users = all_users()
    return render_template ('home/gallery.html', comments=comments, sheets=sheets, current_user=current_user, users=users)

def SRD():
    return render_template ('home/SRD.html')

def new():
    return render_template('home/create.html')

def create():
    character_name = request.form.get('character_name')
    class_and_level = request.form.get('class_and_level')
    background = request.form.get('background')
    player_name = request.form.get('player_name')
    race = request.form.get('race')
    alignment = request.form.get('alignment')
    experience_points = request.form.get('experience_points')
    stat_str = request.form.get('stat_str')
    stat_dex = request.form.get('stat_dex')
    stat_con = request.form.get('stat_con')
    stat_int = request.form.get('stat_int')
    stat_wis = request.form.get('stat_wis')
    stat_cha = request.form.get('stat_cha')
    passive_perception = request.form.get('passive_perception')
    svgthrow_stat_str = request.form.get('svgthrow_stat_str')
    svgthrow_stat_dex = request.form.get('svgthrow_stat_dex')
    svgthrow_stat_con = request.form.get('svgthrow_stat_con')
    svgthrow_stat_int = request.form.get('svgthrow_stat_int')
    svgthrow_stat_wis = request.form.get('svgthrow_stat_wis')
    svgthrow_stat_cha = request.form.get('svgthrow_stat_cha')
    prof_bonus = request.form.get('prof_bonus')
    sk_acroba = request.form.get('sk_acroba')
    sk_animal = request.form.get('sk_animal')
    sk_arcana = request.form.get('sk_arcana')
    sk_athlet = request.form.get('sk_athlet')
    sk_decept = request.form.get('sk_decept')
    sk_histor = request.form.get('sk_histor')
    sk_insigh = request.form.get('sk_insigh')
    sk_intimi = request.form.get('sk_intimi')
    sk_invest = request.form.get('sk_invest')
    sk_medici = request.form.get('sk_medici')
    sk_nature = request.form.get('sk_nature')
    sk_percep = request.form.get('sk_percep')
    sk_perfor = request.form.get('sk_perfor')
    sk_persua = request.form.get('sk_persua')
    sk_religi = request.form.get('sk_religi')
    sk_sleigh = request.form.get('sk_sleigh')
    sk_stealt = request.form.get('sk_stealt')
    sk_suviva = request.form.get('sk_suviva')
    otr_prof_lang = request.form.get('otr_prof_lang')
    armor = request.form.get('armor')
    initiative = request.form.get('initiative')
    speed = request.form.get('speed')
    current_hp = request.form.get('current_hp')
    temp_hp = request.form.get('temp_hp')
    hit_dice = request.form.get('hit_dice')
    dthsv_pass = request.form.get('dthsv_pass')
    dthsv_fail = request.form.get('dthsv_fail')
    attacks_spells = request.form.get('attacks_spells')
    equipment = request.form.get('equipment')
    traits = request.form.get('traits')
    ideals = request.form.get('ideals')
    bonds = request.form.get('bonds')
    flaws = request.form.get('flaws')
    fluff = request.form.get('fluff')
    spellcasting_class = request.form.get('spellcasting_class')
    spellcasting_ability = request.form.get('spellcasting_ability')
    spell_save_dc = request.form.get('spell_save_dc')
    spell_atk_bonus = request.form.get('spell_atk_bonus')
    cantrips = request.form.get('cantrips')
    first_level_spells = request.form.get('first_level_spells')
    second_level_spells = request.form.get('second_level_spells')
    third_level_spells = request.form.get('third_level_spells')
    fourth_level_spells = request.form.get('fourth_level_spells')
    fifth_level_spells = request.form.get('fifth_level_spells')
    sixth_level_spells = request.form.get('sixth_level_spells')
    seventh_level_spells = request.form.get('seventh_level_spells')
    eighth_level_spells = request.form.get('eighth_level_spells')
    ninth_level_spells = request.form.get('ninth_level_spells')
    age = request.form.get('age')
    height = request.form.get('height')
    character_weight = request.form.get('character_weight')
    eyes = request.form.get('eyes')
    skin = request.form.get('skin')
    hair = request.form.get('hair')
    appearance = request.form.get('appearance')
    allies_organisations = request.form.get('allies_organisations')
    character_backstory = request.form.get('character_backstory')
    additional_features_traits = request.form.get('additional_features_traits')
    treasure = request.form.get('treasure')
    create_sheets(character_name, class_and_level, background, player_name, race, alignment, experience_points, stat_str, stat_dex, stat_con, stat_int, stat_wis, stat_cha, passive_perception, svgthrow_stat_str, svgthrow_stat_dex, svgthrow_stat_con, svgthrow_stat_int, svgthrow_stat_wis, svgthrow_stat_cha, prof_bonus, sk_acroba, sk_animal, sk_arcana, sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva, otr_prof_lang, armor, initiative, speed, current_hp, temp_hp, hit_dice, dthsv_pass, dthsv_fail, attacks_spells, equipment, traits, ideals, bonds, flaws, fluff, spellcasting_class, spellcasting_ability, spell_save_dc, spell_atk_bonus, cantrips, first_level_spells, second_level_spells, third_level_spells, fourth_level_spells, fifth_level_spells, sixth_level_spells, seventh_level_spells, eighth_level_spells, ninth_level_spells, age, height, character_weight, eyes, skin, hair, appearance, allies_organisations, character_backstory, additional_features_traits, treasure)
    return redirect('/home/gallery')

def edit(id):
  sheet = get_sheets(id)
  return render_template('home/edit.html', sheet=sheet)

def update(id):
    character_name = request.form.get('character_name')
    class_and_level = request.form.get('class_and_level')
    background = request.form.get('background')
    player_name = request.form.get('player_name')
    race = request.form.get('race')
    alignment = request.form.get('alignment')
    experience_points = request.form.get('experience_points')
    stat_str = request.form.get('stat_str')
    stat_dex = request.form.get('stat_dex')
    stat_con = request.form.get('stat_con')
    stat_int = request.form.get('stat_int')
    stat_wis = request.form.get('stat_wis')
    stat_cha = request.form.get('stat_cha')
    passive_perception = request.form.get('passive_perception')
    svgthrow_stat_str = request.form.get('svgthrow_stat_str')
    svgthrow_stat_dex = request.form.get('svgthrow_stat_dex')
    svgthrow_stat_con = request.form.get('svgthrow_stat_con')
    svgthrow_stat_int = request.form.get('svgthrow_stat_int')
    svgthrow_stat_wis = request.form.get('svgthrow_stat_wis')
    svgthrow_stat_cha = request.form.get('svgthrow_stat_cha')
    prof_bonus = request.form.get('prof_bonus')
    sk_acroba = request.form.get('sk_acroba')
    sk_animal = request.form.get('sk_animal')
    sk_arcana = request.form.get('sk_arcana')
    sk_athlet = request.form.get('sk_athlet')
    sk_decept = request.form.get('sk_decept')
    sk_histor = request.form.get('sk_histor')
    sk_insigh = request.form.get('sk_insigh')
    sk_intimi = request.form.get('sk_intimi')
    sk_invest = request.form.get('sk_invest')
    sk_medici = request.form.get('sk_medici')
    sk_nature = request.form.get('sk_nature')
    sk_percep = request.form.get('sk_percep')
    sk_perfor = request.form.get('sk_perfor')
    sk_persua = request.form.get('sk_persua')
    sk_religi = request.form.get('sk_religi')
    sk_sleigh = request.form.get('sk_sleigh')
    sk_stealt = request.form.get('sk_stealt')
    sk_suviva = request.form.get('sk_suviva')
    otr_prof_lang = request.form.get('otr_prof_lang')
    armor = request.form.get('armor')
    initiative = request.form.get('initiative')
    speed = request.form.get('speed')
    current_hp = request.form.get('current_hp')
    temp_hp = request.form.get('temp_hp')
    hit_dice = request.form.get('hit_dice')
    dthsv_pass = request.form.get('dthsv_pass')
    dthsv_fail = request.form.get('dthsv_fail')
    attacks_spells = request.form.get('attacks_spells')
    equipment = request.form.get('equipment')
    traits = request.form.get('traits')
    ideals = request.form.get('ideals')
    bonds = request.form.get('bonds')
    flaws = request.form.get('flaws')
    fluff = request.form.get('fluff')
    spellcasting_class = request.form.get('spellcasting_class')
    spellcasting_ability = request.form.get('spellcasting_ability')
    spell_save_dc = request.form.get('spell_save_dc')
    spell_atk_bonus = request.form.get('spell_atk_bonus')
    cantrips = request.form.get('cantrips')
    first_level_spells = request.form.get('first_level_spells')
    second_level_spells = request.form.get('second_level_spells')
    third_level_spells = request.form.get('third_level_spells')
    fourth_level_spells = request.form.get('fourth_level_spells')
    fifth_level_spells = request.form.get('fifth_level_spells')
    sixth_level_spells = request.form.get('sixth_level_spells')
    seventh_level_spells = request.form.get('seventh_level_spells')
    eighth_level_spells = request.form.get('eighth_level_spells')
    ninth_level_spells = request.form.get('ninth_level_spells')
    age = request.form.get('age')
    height = request.form.get('height')
    character_weight = request.form.get('character_weight')
    eyes = request.form.get('eyes')
    skin = request.form.get('skin')
    hair = request.form.get('hair')
    appearance = request.form.get('appearance')
    allies_organisations = request.form.get('allies_organisations')
    character_backstory = request.form.get('character_backstory')
    additional_features_traits = request.form.get('additional_features_traits')
    treasure = request.form.get('treasure')
    update_sheet(id, character_name, class_and_level, background, player_name, race, alignment, experience_points, stat_str, stat_dex, stat_con, stat_int, stat_wis, stat_cha, passive_perception, svgthrow_stat_str, svgthrow_stat_dex, svgthrow_stat_con, svgthrow_stat_int, svgthrow_stat_wis, svgthrow_stat_cha, prof_bonus, sk_acroba, sk_animal, sk_arcana, sk_athlet, sk_decept, sk_histor, sk_insigh, sk_intimi, sk_invest, sk_medici, sk_nature, sk_percep, sk_perfor, sk_persua, sk_religi, sk_sleigh, sk_stealt, sk_suviva, otr_prof_lang, armor, initiative, speed, current_hp, temp_hp, hit_dice, dthsv_pass, dthsv_fail, attacks_spells, equipment, traits, ideals, bonds, flaws, fluff, spellcasting_class, spellcasting_ability, spell_save_dc, spell_atk_bonus, cantrips, first_level_spells, second_level_spells, third_level_spells, fourth_level_spells, fifth_level_spells, sixth_level_spells, seventh_level_spells, eighth_level_spells, ninth_level_spells, age, height, character_weight, eyes, skin, hair, appearance, allies_organisations, character_backstory, additional_features_traits, treasure)
    return redirect('/home/gallery')

def delete(id):
  delete_sheet(id)
  return redirect('/home/gallery')

def comment(id):
    comment_content = request.form.get('comment_content')
    commenter_name = current_user()['first_name']
    add_comment(id, session['user_id'], comment_content, commenter_name)
    return redirect('/home/gallery')