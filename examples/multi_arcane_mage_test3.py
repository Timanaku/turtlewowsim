from _example_imports import *

cds = CooldownUsages(arcane_power=5, mqg=5)
mages = []
num_mages = 4
for i in range(num_mages):
    fm = None
    if i == 0:
        fm = Mage(name=f'mephiring', sp=1000+29, crit=24+2, hit=16, haste=16,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(t3_8_set=False, extra_second_arcane_missile=False, interrupt_arcane_missiles=True),
                  equipped_items=EquippedItems(
                      ornate_bloodstone_dagger=False,
                      wrath_of_cenarius=True,
                      endless_gulch=False,
                  ))
        fm.arcane_surge_rupture_missiles(cds=cds)
    elif i == 1:
        fm = Mage(name=f'sulfuras', sp=1000+20, crit=24, hit=16, haste=16+1,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(t3_8_set=False, extra_second_arcane_missile=False, interrupt_arcane_missiles=True),
                  equipped_items=EquippedItems(
                      ornate_bloodstone_dagger=False,
                      wrath_of_cenarius=True,
                      endless_gulch=False,
                      true_band_of_sulfuras=True
                  ))
        fm.arcane_surge_fireball_rupture_missiles_improved(cds=cds)
        #fm.arcane_surge_rupture_missiles(cds=cds)
    elif i == 2:
        fm = Mage(name=f'medivhring', sp=1000+56, crit=24+2, hit=16, haste=16+1,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(t3_8_set=False, extra_second_arcane_missile=False, interrupt_arcane_missiles=True),
                  equipped_items=EquippedItems(
                      ornate_bloodstone_dagger=False,
                      wrath_of_cenarius=False,
                      endless_gulch=False,
                      true_band_of_sulfuras=False
                  ))
        fm.arcane_surge_rupture_missiles(cds=cds)
    elif i == 3:
        fm = Mage(name=f'80spring', sp=1000+80, crit=24, hit=16, haste=0,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(t3_8_set=False, extra_second_arcane_missile=False, interrupt_arcane_missiles=True),
                  equipped_items=EquippedItems(
                      ornate_bloodstone_dagger=False,
                      wrath_of_cenarius=True,
                      endless_gulch=False,
                      true_band_of_sulfuras=False
                  ))
        fm.arcane_surge_rupture_missiles(cds=cds)
    if fm:
        mages.append(fm)

sim = Simulation(characters=mages, num_mobs=1)
sim.run(iterations=5000, duration=120, print_casts=False)
sim.detailed_report()
