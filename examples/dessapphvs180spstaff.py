from _example_imports import *

#cds = CooldownUsages()
cds = CooldownUsages(arcane_power=5, mqg=5)
mages = []
num_mages = 2
for i in range(num_mages):
    fm = None
    if i == 0:
        fm = Mage(name=f'desecration', sp=911+128+26, crit=24+1.3, hit=16, haste=10+2,
                    tal=ArcaneMageTalents,
                    opts=MageOptions(t3_8_set=False, extra_second_arcane_missile=True, interrupt_arcane_missiles=True),
                    equipped_items=EquippedItems(
                        ornate_bloodstone_dagger=False,
                        wrath_of_cenarius=True,
                        endless_gulch=False,
                        true_band_of_sulfuras=True
                    ))
        fm.arcane_surge_fireball_rupture_missiles_improved(cds=cds)
    elif i == 1:
        fm = Mage(name=f'180spstaff', sp=911+180, crit=24+2.5, hit=16, haste=10,
                   tal=ArcaneMageTalents,
                   opts=MageOptions(t3_8_set=False, extra_second_arcane_missile=True, interrupt_arcane_missiles=True),
                   equipped_items=EquippedItems(
                       ornate_bloodstone_dagger=False,
                       wrath_of_cenarius=True,
                       endless_gulch=False,
                       true_band_of_sulfuras=True
                   ))
        fm.arcane_surge_fireball_rupture_missiles_improved(cds=cds)
    if fm:
         mages.append(fm)
sim = Simulation(characters=mages, num_mobs=1)
sim.run(iterations=5000, duration=120, print_casts=False)
sim.detailed_report()
