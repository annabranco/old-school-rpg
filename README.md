# _Old-school_ Role Playing Game

v0.0.19
_Under construction_

This is a text-based Fantasy Role Playing Game.

The aim to create a flexible backend system designed to acomodate different stories and games.

## Current development: interactions

- (0.0.21) basic rest action
- (0.0.21) basic time events
- (0.0.21) getting (very) tired acording to rounds of combat
- (0.0.21) getting (very) tired according to time
- (0.0.21) getting hungry according ot time
- (0.0.22) move/go
- (0.0.23) Threat level
- (0.0.24) carrying bodies
- (0.0.25) connecting scenarios
- (0.0.26) hide

## Next dev

- (0.1.0) First testing game

## Changelog

### Basic interacting with elements development

0.0.20

- implemented basic eating action
- implemented food consumption

0.0.19

- implemented weight limit when getting elements
- fixed counting weight for countless items
- fixed core_elements module name

0.0.18

- fixed getting countless items
- added number of each item on inventory
- added quantity when getting food

0.0.17

- improved get/take action by cloning objects
- added system_name as global config to standardize names when comparing them

0.0.16

- improved draw weapon
- added gender and corresponding pronoms
- added look at self appearance action
- improved looking action

0.0.15

- added equip weapon/shield/armor action
- added droping equiped weapon/shield/armor action
- improved interaction with dead enemies weapons/shields/armors

0.0.14

- added information about how many days the food owned can sustain Hero
- added articles and pronoms to elements
- added looking/searching by partial names

0.0.13

- implemented secondary effects of on searching
- added check own status action

0.0.12

- Improved get/take action
- added drop action
- implemented add to floor mechanics
- added interacting with enemies bodies
- added looting enemies bodies
- created basic databases for armors, enemies, food, shields, status, valuables and weapons

0.0.11

- added get/take action
- added checking own inventory

0.0.10

- improved searching action
- added type definitions

### Basic interacting with scenario development

0.0.9

- developed basic concept of using 5 senses to interact with elements and scenario
- improved looking action
- implemented finding things mechanics
- added comments on code
- implemented Element generic Class
- implemented Item, Container as instances of Element
- implemented Food, Weapon, Shield, Armor as instances of Item

0.0.8

- implemented global prompt
- added actions looking and searching
- added cinematics module
- implemented Scenario Class
- added basic scenario structure
- created testing forest basic scenario

### Combat development

0.0.7

- Implemented full alfa version of combat system

0.0.6

- implementeg generic Character Class
- implemented Player and NPC as Character instances
- Implemented Hero as Player instance
- added draw weapon action

0.0.5

- added databases (death, kill, damage)
- added basic status changes management
- added cinematics texts
- implemented printing cinematics
- added simultaneous attacks

0.0.4

- added status system (basic concept)
- improved defense mechanics
- implemented basic missed attack cinematics
- implemented combat prompt
- finished basic combat system (with rounds)

0.0.3

- added specific print effects
- created config file
- implemented Wait action
- added initiative system
- added surprise attack
- improved combat mechanics

0.0.2

- developed basic defense structure
- implemented defend action
- implemented roll modifiers
- implemented death by combat mechanics
- implemented kill mechanics
- implemented failed attack mechanics

0.0.1

- implemented basic dice roll system
- implemented Attack action
- implemented damage mechanics
- developed basic attack structure

## Implemented

### System

- Printing cinematics
- Printing mechanics
- Characters constructor
- Hero constructor
- Scenario constructor
- Items constructor
- Food constructor
- Weapons constructor
- Armors constructor
- Shields constructor
- Articles and pronoms
- Valuables and pronoms

### Global mechanics

- Dice rolls
- Modifiers
- Status changes
- Add to scenario mechanics
- Finding things mechanics
- Add to floor mechanics
- Droping things
- On searching effects
- On looking effects.

### Combat mechanics

- Combat rounds
- Initiative
- Attacking
- Defending
- Damage
- Simultaneous attack
- Missing attack

### Actions

- Global prompt
- Look
- Search
- Get/Take (incl. looting from bodies)
- Drop
- Check inventory/items--
- Check own status
- Equip weapon/shield/armor
- Check own appearance
- Draw weapon

### Combat actions

- Attack
- Defend
- Wait

### Database

- Enemies basic
- Status
- Weapons basic
- Armors basic
- Food basic
- Valuables basic

### Cinematics

- Start encounter
- Damages
- Deathes
- Kills
- Fails

### Scenarios

- Base
- Testing Forest