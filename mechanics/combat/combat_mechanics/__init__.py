from core.config import *
from core.characters.Hero import Hero
import cinematics
from mechanics.combat.combat_rounds import combat_rounds
from mechanics.combat import initiative
from mechanics.combat import attack
from mechanics.combat import defend
from db import status
from db import death
from db import kills
from db import damages
from mechanics.global_mechanics import status_changes


def damage(successes, attacker, defendant):
    defendant.take_damage(abs(successes))

    if defendant.status == 'dead':
        if defendant == Hero:
            death.death_by_combat(defendant, attacker)
        else:
            kills.killed_enemy(attacker, defendant)

    elif defendant.status == 'severily wounded':
        cinematics_block()
        if defendant == Hero:
            print_cinematics(
                f'{attacker.name} strikes you causing great pain and damage. You feel badly hurt.\n')
        else:
            print_cinematics(
                f'You slash your {Hero.weapon["name"]} causing a great damage on {defendant.name}. It is badly hurt.\n')
        cinematics_block()
    else:
        damages.cause_damage(attacker, defendant, successes)

    next_round(attacker, defendant)


def next_round(attacker, defendant):
    if defendant == Hero and combat_rounds.took_action['Hero'] and combat_rounds.took_action['enemy']:
        print('\nStart next round.\n')
        initiative.initiative(attacker, 0)
    elif combat_rounds.took_action['Hero'] and combat_rounds.took_action['enemy']:
        initiative.initiative(defendant, 0)
    elif defendant == Hero and combat_rounds.took_action['enemy']:
        cinematics.declare_enemy_status(attacker)
        cinematics.declare_hero_status()
        action_block()
        attack.attack(attacker, 0, False)
    elif attacker == Hero and combat_rounds.took_action['Hero']:
        cinematics.declare_enemy_status(defendant)
        cinematics.declare_hero_status()
        action_block()
        defend.defend(defendant, 0, False)
    else:
        print('something went wrong')


def missed(attacker, defendant):
    cinematics_block()
    if attacker == Hero:
        print_cinematics(f'You miss your blow on {defendant["name"]}.\n')
    else:
        print_cinematics(
            f'{attacker["name"]} misses the attack against you.\n')
    cinematics_block()
    next_round(attacker, defendant)


def simultaneous_damage(results_number_hero, Hero, results_number_enemy, enemy):

    total_hp_hero = Hero['total_hp']
    hp_hero = Hero['hp']
    new_hero_hp = hp_hero - abs(results_number_enemy)
    Hero['hp'] = new_hero_hp

    total_hp_enemy = enemy['total_hp']
    hp_enemy = enemy['hp']
    new_enemy_hp = hp_enemy - abs(results_number_hero)
    enemy['hp'] = new_enemy_hp

    print('Current HPs after the simultaneous attack:')
    print(f'You: {new_hero_hp}')
    print(f'{enemy["name"]}: {new_enemy_hp}')

    if new_hero_hp <= 0:
        status_changes.update_status(Hero, 'dead')
    elif new_hero_hp <= total_hp_hero / 3:
        status_changes.update_status(Hero, 'severily wounded')
    elif new_hero_hp <= total_hp_hero / 3 * 2:
        status_changes.update_status(Hero, 'wounded')
    elif new_hero_hp < total_hp_hero:
        status_changes.update_status(Hero, 'lightly wounded')

    if new_enemy_hp <= 0:
        status_changes.update_status(enemy, 'dead')
    elif new_enemy_hp <= total_hp_enemy / 3:
        status_changes.update_status(enemy, 'severily wounded')
    elif new_enemy_hp <= total_hp_enemy / 3 * 2:
        status_changes.update_status(enemy, 'wounded')
    elif new_enemy_hp < total_hp_enemy:
        status_changes.update_status(enemy, 'lightly wounded')

    if new_hero_hp <= 0 and new_enemy_hp <= 0:
        death.mutual_death_by_combat(enemy)
    elif new_hero_hp <= 0:
        death.death_by_simultaneous_attack(enemy, results_number_hero)
    elif new_enemy_hp <= 0:
        kills.killed_enemy_on_simultaneous_attack(Hero, enemy)
    else:
        cinematics_block()
        print_cinematics(
            f'You and {enemy["name"]} hit each other at the same time, causing mutual damage.')
        cinematics_block()
        print('\nStart next round.\n')
        next_round(Hero, enemy)
