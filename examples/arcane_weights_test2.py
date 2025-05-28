from _example_imports import *

mages = []
num_mages = 30  # Increased to accommodate multiple haste tests
control_sp = 1000
control_crit = 40
control_hit = 15
control_haste = 0
equipped_items = EquippedItems(
    ornate_bloodstone_dagger=False,
    wrath_of_cenarius=False,
)
cds = CooldownUsages(arcane_power=5, mqg=5)

# Add control mage and basic stat tests
for i in range(5):
    fm = None
    if i == 0:
        fm = Mage(name=f'control', sp=control_sp, crit=control_crit, hit=control_hit, haste=control_haste,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(),
                  equipped_items=equipped_items)
    elif i == 1:
        fm = Mage(name=f'1 hit',  sp=control_sp, crit=control_crit, hit=control_hit+1, haste=control_haste,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(),
                  equipped_items=equipped_items)
    elif i == 2:
        fm = Mage(name=f'1 crit',  sp=control_sp, crit=control_crit+1, hit=control_hit, haste=control_haste,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(),
                  equipped_items=equipped_items)
    elif i == 3:
        fm = Mage(name=f'1 haste',  sp=control_sp, crit=control_crit, hit=control_hit, haste=control_haste+1,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(),
                  equipped_items=equipped_items)
    elif i == 4:
        fm = Mage(name=f'20sp',  sp=control_sp + 20, crit=control_crit, hit=control_hit, haste=control_haste,
                  tal=ArcaneMageTalents,
                  opts=MageOptions(),
                  equipped_items=equipped_items)
    if fm:
        fm.arcane_surge_rupture_missiles(cds=cds)
        mages.append(fm)

# Add incremental haste tests, increasing by 1 each time until 25% haste increase
max_haste_increase = 25
for haste_increment in range(2, max_haste_increase + 1):
    fm = Mage(
        name=f'{haste_increment} haste',
        sp=control_sp,
        crit=control_crit,
        hit=control_hit,
        haste=control_haste + haste_increment,
        tal=ArcaneMageTalents,
        opts=MageOptions(),
        equipped_items=equipped_items
    )
    if fm:
        fm.arcane_surge_rupture_missiles(cds=cds)
        mages.append(fm)

# Run the simulation
sim = Simulation(characters=mages, num_mobs=1, mob_level=60)
sim.run(iterations=1000, duration=30, print_casts=False)

# Print detailed report
sim.detailed_report()
