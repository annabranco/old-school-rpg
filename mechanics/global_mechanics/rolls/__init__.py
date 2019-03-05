from core.config import write_to_screen
import time
from random import randint
from typing import List, Dict


def roll_dices(dices_number: int, difficult: int, reason: str):
    i: int = 1
    rolls: List[int] = []
    rolled_results: List[int] = []
    results_object: Dict[str, int] = {
        'decisive': 0,
        'critical': 0,
        'success': 0,
        'fail': 0,
        'decisiveMinusCritical': 0,
        'final_result': 0
    }

    while i <= dices_number:
        rolls.append(randint(1, 10))
        i += 1
    for roll in rolls:
        if roll == 10:
            rolled_results.append({roll: '❕ decisive success'})
            results_object['decisive'] += 1
            results_object['success'] += 1
        elif roll == 1:
            rolled_results.append({roll: '❗️ critical fail'})
            results_object['critical'] += 1
        elif roll >= difficult:
            rolled_results.append({roll: '✔️ success'})
            results_object['success'] += 1
        else:
            rolled_results.append({roll: '✖️  fail'})
            results_object['fail'] += 1

    results_object['decisiveMinusCritical']: int = results_object['decisive'] - \
        results_object['critical']
    results_object['final_result']: int = results_object['success'] + \
        results_object['decisiveMinusCritical']
    special: str = print_rolls(difficult, rolls, rolled_results,
                          results_object, reason)
    return [results_object['final_result'], special]


def print_rolls(difficult: int, rolls: int, rolled_results: List[int], results_object: Dict[str, int], reason: str) -> str:
    time.sleep(0.01)
    print(f'  *** {reason} ***')
    print(f'Dices to roll: {len(rolled_results)}, difficult: {difficult}')
    print('\n')
    index: int = 0
    while index < len(rolls):
        result_num = rolls[index]
        result_txt = rolled_results[index][result_num]
        index += 1
        time.sleep(1.2)
        write_to_screen(f'{result_num} ')
        time.sleep(0.8)
        write_to_screen(f'{result_txt}\n')
    print('\n')
    special, result, final_result = define_result(results_object)

    print(f'\t* Result: {special.upper()} {result.upper()} ({final_result})')
    print('\n')
    return special


def define_result(results_object: Dict[str, int]):
    final_result: int
    decisive, critical, success, fail, decisiveMinusCritical, final_result = results_object.values()

    special: str = ''
    result: str
    if final_result == 0:
        result = 'fail'
    elif final_result > 0:
        result = 'success'
        if decisiveMinusCritical >= 3:
            special = 'epic'
        elif decisiveMinusCritical > 0:
            special = 'decisive'
    else:
        result = 'fail'
        if decisiveMinusCritical <= -3:
            special = 'disastrous'
        elif decisiveMinusCritical < 0:
            special = 'critical'

    return [special, result, final_result]
