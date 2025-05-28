from _example_imports import *

#cds = CooldownUsages()
cds = CooldownUsages(arcane_power=19, mqg=1, potion_of_quickness=1)
mages = []
num_mages = 3
for i in range(num_mages):
    fm = None
    if i == 0:
        fm = Mage(name=f'termsbis', sp=1057, crit=53.8, hit=16, haste=7.1,
                    tal=ArcaneMageTalents,
                    opts=MageOptions(t35_3_set=False, extra_second_arcane_missile=False, interrupt_arcane_missiles=True),
                    equipped_items=EquippedItems(
                        ornate_bloodstone_dagger=False,
                        wrath_of_cenarius=False,
                        endless_gulch=False,
                        true_band_of_sulfuras=False,
                        binding_of_contained_magic=True
                    ))
        fm.arcane_surge_rupture_missiles(cds=cds)
    elif i == 1:
        fm = Mage(name=f'akanamubis', sp=969, crit=40.97, hit=16, haste=23.02,
                   tal=ArcaneMageTalents,
                   opts=MageOptions(t35_3_set=True, extra_second_arcane_missile=True, interrupt_arcane_missiles=True),
                   equipped_items=EquippedItems(
                       ornate_bloodstone_dagger=False,
                       wrath_of_cenarius=True,
                       endless_gulch=False,
                       true_band_of_sulfuras=True,
                       binding_of_contained_magic=True
                   ))
        fm.arcane_rupture_missiles(cds=cds)
    elif i == 2:
        fm = Mage(name=f'shegarbis', sp=908, crit=39.95, hit=16, haste=27.97,
                   tal=ArcaneMageTalents,
                   opts=MageOptions(t35_3_set=True, extra_second_arcane_missile=True, interrupt_arcane_missiles=True),
                   equipped_items=EquippedItems(
                       ornate_bloodstone_dagger=False,
                       wrath_of_cenarius=True,
                       endless_gulch=False,
                       true_band_of_sulfuras=True,
                       binding_of_contained_magic=True
                   ))
        fm.arcane_rupture_missiles(cds=cds)
    if fm:
         mages.append(fm)
sim = Simulation(characters=mages, num_mobs=1)
sim.run(iterations=5000, duration=120, print_casts=False)
sim.detailed_report()
