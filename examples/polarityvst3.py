from _example_imports import *

cds = CooldownUsages()
#cds = CooldownUsages(arcane_power=5, mqg=5)
mages = []
num_mages = 4
for i in range(num_mages):
    fm = None
    if i == 0:
        fm = Mage(name=f'polarity', sp=670+300, crit=19.32, hit=16, haste=14,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(t3_8_set=False, extra_second_arcane_missile=True, interrupt_arcane_missiles=True),
                  equipped_items=EquippedItems(
                      ornate_bloodstone_dagger=False,
                      wrath_of_cenarius=False,
                      endless_gulch=False,
                  ))
        fm.arcane_surge_rupture_missiles(cds=cds)
    elif i == 1:
        fm = Mage(name=f't3legs', sp=662+300, crit=18.45, hit=16, haste=15,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(t3_8_set=False, extra_second_arcane_missile=True, interrupt_arcane_missiles=True),
                  equipped_items=EquippedItems(
                      ornate_bloodstone_dagger=False,
                      wrath_of_cenarius=False,
                      endless_gulch=False,
                      true_band_of_sulfuras=False
                  ))
        fm.arcane_surge_rupture_missiles(cds=cds)
    elif i == 2:
        fm = Mage(name=f't3legs+t3gloves', sp=673+300, crit=19.49, hit=16, haste=13,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(t3_8_set=False, extra_second_arcane_missile=True, interrupt_arcane_missiles=True),
                  equipped_items=EquippedItems(
                      ornate_bloodstone_dagger=False,
                      wrath_of_cenarius=False,
                      endless_gulch=False,
                      true_band_of_sulfuras=False
                  ))
        fm.arcane_surge_rupture_missiles(cds=cds)
    if i == 3:
        fm = Mage(name=f'polarity+t3gloves', sp=681+300, crit=20.36, hit=16, haste=12,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(t3_8_set=False, extra_second_arcane_missile=True, interrupt_arcane_missiles=True),
                  equipped_items=EquippedItems(
                      ornate_bloodstone_dagger=False,
                      wrath_of_cenarius=False,
                      endless_gulch=False,
                  ))
        fm.arcane_surge_rupture_missiles(cds=cds)
    if fm:
        mages.append(fm)

sim = Simulation(characters=mages, num_mobs=1)
sim.run(iterations=5000, duration=120, print_casts=False)
sim.detailed_report()
