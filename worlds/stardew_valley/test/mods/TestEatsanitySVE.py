import unittest

from ...mods.mod_data import ModNames
from ...options import Eatsanity, ExcludeGingerIsland, Mods
from ...strings.ap_names.ap_option_names import EatsanityOptionName
from ..options.utils import skip_if_mod_disabled
from ..TestEatsanity import SVEatsanityTestBase

# SVE fish the content pack removes when Ginger Island is excluded - either they
# live on the island or their region is gated behind Lance's hearts.
# Source: content/mods/sve.py -> SVEContentPack.fish_hook
SVE_ISLAND_FISH = (
    "Arrowhead Shark",
    "Barred Knifejaw",
    "Blue Tang",
    "Clownfish",
    "Fiber Goby",
    "Highlands Bass",
    "Ocean Sunfish",
    "Shark",
    "Seahorse",
)
SVE_ISLAND_POISONOUS_FISH = (
    "Baby Lunaloo",
    "Daggerfish",
    "Diamond Carp",
    "Gemfish",
    "Lunaloo",
    "Sea Sponge",
    "Torpedo Trout",
    "Turretfish",
    "Viper Eel",
    "Bonefish",
    "Undeadfish",
    "Shiny Lunaloo",
)
SVE_MAINLAND_FISH = (
    "Alligator",
    "Bull Trout",
    "Butterfish",
    "Dulse Seaweed",
    "Gar",
    "Goldfish",
    "Glowfish",
    "Grass Carp",
    "King Salmon",
    "Kittyfish",
    "Minnow",
    "Puppyfish",
    "Snatcher Worm",
    "Swamp Crab",
    "Tadpole",
    "Water Grub",
    "Wolf Snapper",
)
SVE_MAINLAND_POISONOUS_FISH = (
    "Meteor Carp",
    "Radioactive Bass",
    "Starfish",
    "Void Eel",
    "Frog",
)

ALL_SVE_FISH = (
    *SVE_ISLAND_FISH,
    *SVE_ISLAND_POISONOUS_FISH,
    *SVE_MAINLAND_FISH,
    *SVE_MAINLAND_POISONOUS_FISH,
)


@skip_if_mod_disabled(ModNames.sve)
class TestModdedEatsanityNone(SVEatsanityTestBase):
    options = {
        ExcludeGingerIsland: ExcludeGingerIsland.option_false,
        Eatsanity: Eatsanity.preset_none,
        Mods.internal_name: frozenset({ModNames.sve}),
    }
    unexpected_eating_locations = {f"Eat {fish}" for fish in ALL_SVE_FISH}


@skip_if_mod_disabled(ModNames.sve)
class TestModdedEatsanityFish(SVEatsanityTestBase):
    options = {
        ExcludeGingerIsland: ExcludeGingerIsland.option_false,
        Eatsanity: frozenset({EatsanityOptionName.fish}),
        Mods.internal_name: frozenset({ModNames.sve}),
    }
    expected_eating_locations = {
        *(f"Eat {fish}" for fish in SVE_MAINLAND_FISH),
        *(f"Eat {fish}" for fish in SVE_ISLAND_FISH),
    }
    unexpected_eating_locations = {
        # poisonous is off
        *(f"Eat {fish}" for fish in SVE_MAINLAND_POISONOUS_FISH),
        *(f"Eat {fish}" for fish in SVE_ISLAND_POISONOUS_FISH),
        # SVE fish are eaten, never drunk
        *(f"Drink {fish}" for fish in SVE_MAINLAND_FISH),
        # other eatsanity categories are off
        "Eat Ancient Fiber",
        "Drink Blue Moon Wine",
    }

    def test_sve_fish_live_in_the_eating_region(self):
        for fish in SVE_MAINLAND_FISH:
            with self.subTest(fish):
                location = self.world.get_location(f"Eat {fish}")
                self.assertEqual("Eating", location.parent_region.name)

    def test_sve_fish_need_progression(self):
        for fish in SVE_MAINLAND_FISH:
            with self.subTest(fish):
                self.assert_cannot_reach_location(f"Eat {fish}")

    def test_sve_fish_reachable_with_everything(self):
        self.collect_everything()
        for fish in SVE_MAINLAND_FISH:
            with self.subTest(fish):
                self.assert_can_reach_location(f"Eat {fish}")


@skip_if_mod_disabled(ModNames.sve)
class TestModdedEatsanityFishNoGingerIsland(SVEatsanityTestBase):
    options = {
        ExcludeGingerIsland: ExcludeGingerIsland.option_true,
        Eatsanity: frozenset({EatsanityOptionName.fish}),
        Mods.internal_name: frozenset({ModNames.sve}),
    }
    expected_eating_locations = {f"Eat {fish}" for fish in SVE_MAINLAND_FISH}
    unexpected_eating_locations = {
        *(f"Eat {fish}" for fish in SVE_ISLAND_FISH),
        *(f"Eat {fish}" for fish in SVE_ISLAND_POISONOUS_FISH),
    }


@skip_if_mod_disabled(ModNames.sve)
class TestModdedEatsanityPoisonousFish(SVEatsanityTestBase):
    options = {
        ExcludeGingerIsland: ExcludeGingerIsland.option_false,
        Eatsanity: frozenset({EatsanityOptionName.fish, EatsanityOptionName.poisonous}),
        Mods.internal_name: frozenset({ModNames.sve}),
    }
    expected_eating_locations = {f"Eat {fish}" for fish in ALL_SVE_FISH}
    unexpected_eating_locations = {"Eat Ancient Fiber", "Drink Blue Moon Wine"}
