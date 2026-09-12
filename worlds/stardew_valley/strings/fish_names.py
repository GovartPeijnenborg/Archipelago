all_fish = []


def fish(fish_name: str) -> str:
    all_fish.append(fish_name)
    return fish_name


class Fish:
    albacore = fish("Albacore")
    anchovy = fish("Anchovy")
    angler = fish("Angler")
    any = fish("Any Fish")
    blobfish = fish("Blobfish")
    blue_discus = fish("Blue Discus")
    bream = fish("Bream")
    bullhead = fish("Bullhead")
    carp = fish("Carp")
    catfish = fish("Catfish")
    chub = fish("Chub")
    clam = fish("Clam")
    cockle = fish("Cockle")
    crab = fish("Crab")
    crayfish = fish("Crayfish")
    crimsonfish = fish("Crimsonfish")
    dorado = fish("Dorado")
    eel = fish("Eel")
    flounder = fish("Flounder")
    ghostfish = fish("Ghostfish")
    goby = fish("Goby")
    glacierfish = fish("Glacierfish")
    glacierfish_jr = fish("Glacierfish Jr.")
    halibut = fish("Halibut")
    herring = fish("Herring")
    ice_pip = fish("Ice Pip")
    largemouth_bass = fish("Largemouth Bass")
    lava_eel = fish("Lava Eel")
    legend = fish("Legend")
    legend_ii = fish("Legend II")
    lingcod = fish("Lingcod")
    lionfish = fish("Lionfish")
    lobster = fish("Lobster")
    midnight_carp = fish("Midnight Carp")
    midnight_squid = fish("Midnight Squid")
    ms_angler = fish("Ms. Angler")
    mussel = fish("Mussel")
    mussel_node = "Mussel Node"
    mutant_carp = fish("Mutant Carp")
    octopus = fish("Octopus")
    oyster = fish("Oyster")
    perch = fish("Perch")
    periwinkle = fish("Periwinkle")
    pike = fish("Pike")
    pufferfish = fish("Pufferfish")
    radioactive_carp = fish("Radioactive Carp")
    rainbow_trout = fish("Rainbow Trout")
    red_mullet = fish("Red Mullet")
    red_snapper = fish("Red Snapper")
    salmon = fish("Salmon")
    sandfish = fish("Sandfish")
    sardine = fish("Sardine")
    scorpion_carp = fish("Scorpion Carp")
    sea_cucumber = fish("Sea Cucumber")
    shad = fish("Shad")
    shrimp = fish("Shrimp")
    slimejack = fish("Slimejack")
    smallmouth_bass = fish("Smallmouth Bass")
    snail = fish("Snail")
    son_of_crimsonfish = fish("Son of Crimsonfish")
    spook_fish = fish("Spook Fish")
    squid = fish("Squid")
    stingray = fish("Stingray")
    stonefish = fish("Stonefish")
    sturgeon = fish("Sturgeon")
    sunfish = fish("Sunfish")
    super_cucumber = fish("Super Cucumber")
    tiger_trout = fish("Tiger Trout")
    tilapia = fish("Tilapia")
    tuna = fish("Tuna")
    void_salmon = fish("Void Salmon")
    walleye = fish("Walleye")
    woodskip = fish("Woodskip")


class WaterItem:
    sea_jelly = "Sea Jelly"
    river_jelly = "River Jelly"
    cave_jelly = "Cave Jelly"
    seaweed = "Seaweed"
    green_algae = "Green Algae"
    white_algae = "White Algae"
    coral = "Coral"
    nautilus_shell = "Nautilus Shell"
    sea_urchin = "Sea Urchin"


class Trash:
    driftwood = "Driftwood"
    trash = "Trash"
    broken_cd = "Broken CD"
    broken_glasses = "Broken Glasses"
    joja_cola = "Joja Cola"
    soggy_newspaper = "Soggy Newspaper"


class WaterChest:
    fishing_chest = "Fishing Chest"
    golden_fishing_chest = "Golden Fishing Chest"
    treasure = "Treasure Chest"


class SVEFish:
    alligator = "Alligator"
    arrowhead_shark = "Arrowhead Shark"
    baby_lunaloo = "Baby Lunaloo"
    barred_knifejaw = "Barred Knifejaw"
    blue_tang = "Blue Tang"
    bonefish = "Bonefish"
    bull_trout = "Bull Trout"
    butterfish = "Butterfish"
    clownfish = "Clownfish"
    daggerfish = "Daggerfish"
    diamond_carp = "Diamond Carp"
    fiber_goby = "Fiber Goby"
    frog = "Frog"
    gar = "Gar"
    gemfish = "Gemfish"
    glowfish = "Glowfish"
    goldfish = "Goldfish"
    grass_carp = "Grass Carp"
    highlands_bass = "Highlands Bass"
    king_salmon = "King Salmon"
    kittyfish = "Kittyfish"
    lunaloo = "Lunaloo"
    meteor_carp = "Meteor Carp"
    minnow = "Minnow"
    ocean_sunfish = "Ocean Sunfish"
    puppyfish = "Puppyfish"
    radioactive_bass = "Radioactive Bass"
    sea_sponge = "Sea Sponge"
    seahorse = "Seahorse"
    shark = "Shark"
    shiny_lunaloo = "Shiny Lunaloo"
    snatcher_worm = "Snatcher Worm"
    starfish = "Starfish"
    swamp_crab = "Swamp Crab"
    tadpole = "Tadpole"
    torpedo_trout = "Torpedo Trout"
    turretfish = "Turretfish"
    undeadfish = "Undeadfish"
    viper_eel = "Viper Eel"
    void_eel = "Void Eel"
    water_grub = "Water Grub"
    wolf_snapper = "Wolf Snapper"

class DistantLandsFish:
    void_minnow = "Void Minnow"
    swamp_leech = "Swamp Leech"
    purple_algae = "Purple Algae"
    giant_horsehoe_crab = "Giant Horsehoe Crab"


class SVEWaterItem:
    dulse_seaweed = "Dulse Seaweed"


class ModTrash:
    rusty_scrap = "Scrap Rust"


all_fish = tuple(all_fish)