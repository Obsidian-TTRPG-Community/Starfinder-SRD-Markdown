---
aliases: 
tags: 
---

# STARSHIP ATTACKING & DAMAGE

Whenever one starship fires a weapon at another starship, that action is resolved with a gunnery check. Attacks are made during the gunnery phase of combat, in the order determined during the helm phase, but the damage and critical damage effects (see page 321) are applied after all of the attacks have been made (meaning every starship gets to attack, even if it would be destroyed or crippled by an attack that happened during the same gunnery phase). With only very rare exceptions, each of a starship’s weapons can be fired only once per round. You make an attack using the following procedure.

# RANGE AND ARC

First, determine the range between the two starships (counted in hexes) and the arc of attack. For every range increment beyond the first, the gunnery check takes a cumulative –2 penalty. The attacking starship can fire a weapon against only ships in the same arc as that weapon; see the diagram on page 318. If the targeted starship is in a hex that lies in two arcs (the shaded hexes in the diagram), the gunner decides which arc’s weapons target it; it can’t be targeted by weapons in two arcs.

# GUNNERY CHECK

Attempt a gunnery check for each weapon fired against a target (except for linked weapons, which are resolved using one action and a single gunnery check; see the sidebar on page 301).

**Gunnery Check** = 1d20 + the gunner’s base attack bonus or the gunner’s ranks in the Piloting skill + the gunner’s Dexterity modifier + bonuses from computer systems + bonuses from the captain and science officers + range penalty

## DETERMINING THE OUTCOME

Compare the result of the gunnery check to the target’s Armor Class (AC) or Target Lock (TL), depending on the weapon used. If you attack with a direct-fire weapon (see page 303) and the result of the gunnery check equals or exceeds the target’s AC, you hit the target and damage is determined as normal (see Damage below). A target’s AC is determined using the following formula.

**AC** \= 10 + the pilot’s ranks in the Piloting skill + the ship’s armor bonus + modifier based on the ship’s size + bonuses and penalties from successful or failed stunts and actions

If the attack is made with a tracking weapon such as a missile launcher (see page 303) and the result of the gunnery check equals or exceeds the target’s TL, the tracking weapon’s projectile moves its speed toward the target, making turns during this movement as needed (a projectile from a tracking weapon has perfect maneuverability). If it intercepts the target before it reaches the end of its movement, it explodes and deals damage as normal (see Damage below). If not, attempt a new gunnery check at the start of the next gunnery phase to determine whether the projectile continues to move toward the target; you don’t receive any bonuses from computer systems or actions by your fellow crew members from previous rounds or the current round, but you can take penalties, such as from an enemy science officer’s improve countermeasures action (see page 325). If the result of a gunnery check for a tracking weapon is ever less than the target’s TL, the weapon’s projectile is destroyed and removed from play. A target’s TL is determined using the following formula.

**TL** \= 10 + the pilot’s ranks in the Piloting skill + the ship’s bonus from defensive countermeasures + modifier based on the ship’s size + penalty from the ship’s armor + bonuses and penalties from successful or failed stunts and actions

# DAMAGE

**Source** _Starfinder Core Rulebook pg. 320_  
Combat in space can be highly dangerous to the vessel and its crew. Once a starship has been damaged, critical systems might malfunction or shut down altogether, leaving its passengers without electricity, gravity, or even air. Such damage might also cause a starship to lose its sensors, propulsion, or weapons systems, which could spell defeat during an active engagement.

When a gunner hits with an attack, she rolls the damage dealt by the weapon she is using and determines which quadrant of the targeted starship she hits. A starship’s shield quadrants are the same as its firing arcs (see the diagram on page 318). Damage is first applied to any shields the target starship has in the quadrant hit by the attack, depleting a number of Shield Points equal to the amount of damage dealt. If that quadrant’s Shield Points reach 0, that shield is entirely depleted and any excess damage is applied to the target starship’s Hull Points. If the ship doesn’t have shields or if its shields in that quadrant have already been depleted, apply all damage directly to the target’s Hull Points.

If a starship has a Damage Threshold (see page 292), any attack that would deal damage to its Hull Points equal to or less than this Damage Threshold fails to damage the ship’s Hull Points. If the damage is greater than the Damage Threshold, the full amount of damage is dealt to the ship’s Hull Points.

If a ship is reduced to 0 or fewer Hull Points, it is disabled and it floats in its current direction of travel at a rate of half its speed until it is repaired, rescued, or destroyed. Crew members aboard such ships are not in immediate danger unless their life-support system is wrecked, but they might eventually die from starvation and thirst if they have no way to repair the ship.

If a ship ever takes damage that exceeds twice its Hull Points, it is destroyed and can’t be repaired. All systems stop functioning, and the hull is compromised. The crew might initially survive, but without protection, they won’t live very long.

## CRITICAL DAMAGE

Starship systems can take critical damage, causing them to become less functional and eventually stop working altogether.

Critical damage is scored whenever a gunnery check results in a natural 20 on the die and damage is dealt to the target ship’s hull. The critical range is expanded to a natural 19 or 20 on the die if the target starship was the subject of a successful target system science officer action (see page 325).

Critical damage is also scored whenever the target starship’s hull takes damage that causes its total amount of damage to exceed its Critical Threshold (see page 292) or a multiple of that threshold. For example, a starship with 100 Hull Points and a Critical Threshold of 20 takes critical damage each time its total amount of Hull Point damage exceeds 20, 40, 60, 80, and 100 points (and so on). An individual attack does not need to deal more than 20 damage to score critical damage against this starship; it just needs to be the attack that pushes the starship’s total damage above a multiple of its Critical Threshold.

A starship can take critical damage even when its total Hull Points are below 0.

# SHIELDS

A starship takes critical damage from an attack only if that attack deals damage to the ship’s Hull Points, even if the result of the gunnery check is a natural 20. If the attack’s damage only reduces a starship’s Shield Points, no critical damage occurs.

# CRITICAL DAMAGE EFFECT

When critical damage is scored, the attacking PC should roll on the table below to randomly determine which of the target starship’s key systems is hit; that system gains a critical damage condition (see below), with the effect listed on the table. If the system isn’t currently critically damaged, it gains the glitching condition. If it is critically damaged again, its critical condition changes by one step of severity (glitching becomes malfunctioning; malfunctioning becomes wrecked). These conditions and their effects on crew actions are explained in Critical Damage Conditions.

To determine which system is affected, roll d% and consult the table below. If a system already has the wrecked condition (or in the case of the weapons array, if all weapon arcs have the wrecked condition), apply its critical damage to the next system down on the chart. If you reach the bottom of the chart, instead deal damage to one of the crew (as described below).

| D%     | System        | Effect                                                                                                                                                                                         |
|--------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1–10   | Life support  | Condition applies to all captain actions                                                                                                                                                       |
| 11–30  | Sensors       | Condition applies to all science officer actions                                                                                                                                               |
| 31–60  | Weapons array | Randomly determine one arc containing weapons; condition applies to all gunner actions using weapons in that arc (a turret counts as being in all arcs)                                        |
| 61–80  | Engines       | Condition applies to all pilot actions                                                                                                                                                         |
| 81–100 | Power core    | Condition applies to all engineer actions except hold it together and patch; a malfunctioning or wrecked power core affects other crew members’ actions (see Critical Damage Conditions below) |


# CREW DAMAGE

If the starship’s core has the wrecked condition and further critical damage is dealt to the core, no critical damage conditions are applied to the ship. Instead, one of the crew (determined randomly) is injured, taking an amount of Hit Point damage equal to the Hull Point damage dealt by the attack (without the increase for starship weapons against humanoid targets; see Shooting Starships on page 292). That crew member can attempt a DC 20 Reflex save to take only half damage.

# CRITICAL DAMAGE CONDITIONS

The following are the critical damage conditions and their effects, ordered by severity. These effects apply primarily to starship combat and rarely impact noncombat play (wrecked engines can still be used to get a starship to a safe place to repair, for example— though the GM might rule that it takes longer than normal).

## GLITCHING

A glitching system isn’t operating at peak performance. Crew actions involving the system (except the hold it together and patch engineer actions; see page 323) take a –2 penalty.

## MALFUNCTIONING

A malfunctioning system is difficult to control. Crew actions involving the system (except the hold it together and patch engineer actions) take a –4 penalty. Also, crew members can’t take push actions (see page 322) using that system. If the power core is malfunctioning, all actions aboard the starship not involving the power core take a –2 penalty; this penalty stacks with penalties from critical damage conditions affecting other systems.

## WRECKED

A wrecked system is minimally functional. Crew actions involving the system (except the hold it together and patch engineer actions and minor crew actions; see page 326) automatically fail. If the power core is wrecked, all crew actions aboard the starship not involving the power core take a –4 penalty; this penalty stacks with penalties from critical damage conditions affecting other systems.

# RESTORING SHIELDS AND REPAIRING DAMAGE

When a starship combat encounter is over, the crew members can repair damage done to their starship, provided it hasn’t been destroyed and they haven’t been captured! Shields regenerate Shield Points at a set rate (depending on the type of shield; see page 302) as long as the starship’s power core isn’t wrecked. You can double this recharge rate for 10 minutes by taking 1 minute and succeeding at an Engineering check (DC = 15 + 1-1/2 × the starship’s tier). Any penalties from critical damage conditions apply to this check.

You can remove the critical damage condition from a system by taking 10 minutes and succeeding at an Engineering check. The DC depends on the severity of the condition (DC 15 for glitching, DC 20 for malfunctioning, and DC 25 for wrecked). The system is no longer critically damaged (it has no critical damage conditions) and can function as normal.

Repairing damage to the hull (restoring lost Hull Points) is more difficult. You must first stop the starship completely, usually at a safe location (for instance, a world with a nonhostile atmosphere or a dock on a space station), and the repairing character or characters must have access to the outside of the hull. On most of the Pact Worlds, the crew can pay mechanics to repair the starship; the cost and time needed are up to the GM. If the crew is on its own in uncharted territory, it can still repair the starship’s hull. Doing so costs 10 UPBs (see page 233) per point of damage to be repaired and requires 5 hours of work regardless of the number of points repaired. A character who succeeds at an Engineering check (DC = 15 + 1-1/2 × the starship’s tier) can cut either the cost or the time in half. For every 10 points by which she exceeds the DC, she can reduce one of these factors by half (or by half again), to a minimum of 1 UPB per point of damage and 1 hour. Any number of allies can use the aid another action (see page 133) to assist with this Engineering check. Failing the check to reduce the time or cost instead increases the cost by 5 UPBs per point of damage.

# OTHER ACTIONS IN STARSHIP COMBAT

**Source** _Starfinder Core Rulebook pg. 322_  
While your role determines what actions you can take during a starship combat encounter, on occasion you might want to perform some other kind of action, such as casting a spell or using a class feature. The GM has the final say on what kind of regular actions you can take, but generally, you can take only a move or standard action in a single round, and you can take only a minor crew action (see page 326) during that round. You aren’t assumed to be adjacent to any of your allies during starship combat, so the GM might also decide that you need to take an additional round to get close enough to an ally to affect him with an ability or spell. Any such action is resolved at the beginning of the round, before the engineering phase.  

## NPC SHIP GUNNERY BONUSES

**Source** _Starfinder Core Rulebook pg. 326_  
The gunnery check bonus for an NPC starship of tier 9 or lower is equal to the starship’s tier plus the highest ability score modifier for an NPC of a CR equivalent to the starship’s tier (using the array on page 129 of _Alien Archive_).

For an NPC starship of tier 10 or higher, use the same calculation but substitute the second-highest ability score modifier instead.
