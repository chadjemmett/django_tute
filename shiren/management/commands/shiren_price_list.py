from shiren.models import Price, Item
items = {
600: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
630: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff', 'Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
660: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
690: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
720: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
750: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
780: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
810: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
210: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
220: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
231: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
241: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
252: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
262: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
273: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
283: ['Swap Staff', 'Knockback Staff', 'Pinning Staff', 'Mage Staff', 'Slow Staff', 'Swift Staff'],
1200: ['Electric Staff', 'Shocking Staff', 'Sale Pot', 'Presto Pot', 'Floramorph Pot', 'Sticky Pot', 'Unbreakable Pot', 'Black Hole Pot', 'Fever Pot'],
1260: ['Electric Staff', 'Shocking Staff'],
1320: ['Electric Staff', 'Shocking Staff'],
1380: ['Electric Staff', 'Shocking Staff'],
1440: ['Electric Staff', 'Shocking Staff'],
1500: ['Electric Staff', 'Shocking Staff', 
       'Undo Grass',
       'Repeat Grass',
       'Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
1560: ['Electric Staff', 'Shocking Staff'],
1620: ['Electric Staff', 'Shocking Staff'],
420: ['Electric Staff', 'Shocking Staff'],
441: ['Electric Staff', 'Shocking Staff'],
462: ['Electric Staff', 'Shocking Staff'],
483: ['Electric Staff', 'Shocking Staff'],
504: ['Electric Staff', 'Shocking Staff'],
525: ['Electric Staff', 
      'Undo Grass',
      'Repeat Grass',
      'Shocking Staff', 'Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
546: ['Electric Staff', 'Shocking Staff'],
567: ['Electric Staff', 'Shocking Staff'],
1575: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
1650: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
1725: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
1800: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff', 'Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
1875: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
1950: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
2025: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
551: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
577: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
603: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
656: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
682: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
708: ['Seal Staff', 'Clone Staff', 'Sacrifice Staff'],
1890: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
1980: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
2070: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
2160: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
2250: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
2340: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
2430: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
661: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
693: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
724: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
756: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
787: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
819: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
850: ['Glorious Staff', 'Unlucky Staff', 'Boring Staff', 'Fort. Staff', 'Sharing Staff'],
1000: [
        'Sale Pot', 
        'Presto Pot', 
        'Floramorph Pot', 
        'Sticky Pot', 
        'Unbreakable Pot', 
        'Black Hole Pot', 
        'Fever Pot'
        'Confusion Scroll',
        'Slumber Scroll',
        'Vacuum Slash Scrl',
        'Dispel Aura Scroll',
        'Night-Day Scroll',
        'Swift Foe Scroll',
        'Mnster House Scrl',
        'Immunity Scroll',
        'Replenish Scroll',
        'Fixer Scroll',
        'Gamblers Scroll',
        'Arbor Scroll',
        'Nixer Scroll',
        'Revival Grass',
        'Gut Grass',
        ],
1050: ['Zen Pot', 'Dodger Pot', 'Perceptive Pot', 'Reflection Pot', 'Sale Pot', 'Presto Pot', 'Floramorph Pot', 'Sticky Pot', 'Unbreakable Pot', 'Black Hole Pot', 'Fever Pot', 'Lost Scroll',  'Sanctuary Scroll', 'Expulsion Scroll',
       'Bankruptcy Scroll',

    'Cleansing Bracelet',
    'Anti-Cnf. Bracelet',
    'Alert Bracelet',
    'Anti-Crs. Bracelet',
    'Staunch Bracelet',
    'Critical Bracelet',
    'Mojo Bracelet',
    'Monster Summoner',
    'Dozer Bracelet',
    'Trap Bracelet',


       ],
1100: ['Sale Pot', 'Presto Pot', 'Floramorph Pot', 'Sticky Pot', 'Unbreakable Pot', 'Black Hole Pot', 'Fever Pot'],
1150: ['Sale Pot', 'Presto Pot', 'Floramorph Pot', 'Sticky Pot', 'Unbreakable Pot', 'Black Hole Pot', 'Fever Pot'],
1250: ['Sale Pot', 'Presto Pot', 'Floramorph Pot', 'Sticky Pot', 'Unbreakable Pot', 'Black Hole Pot', 'Fever Pot'],
350: [
        'Sale Pot', 
        'Presto Pot', 
        'Floramorph Pot', 
        'Sticky Pot', 
        'Unbreakable Pot', 
        'Black Hole Pot', 
        'Fever Pot',
        'Confusion Scroll',
        'Slumber Scroll',
        'Vacuum Slash Scrl',
        'Dispel Aura Scroll',
        'Night-Day Scroll',
        'Swift Foe Scroll',
        'Mnster House Scrl',
        'Immunity Scroll',
        'Replenish Scroll',
        'Fixer Scroll',
        'Gamblers Scroll',
        'Arbor Scroll',
        'Nixer Scroll',
        'Gut Grass',
        'Revival Grass',
        ],
367: ['Sale Pot', 'Presto Pot', 'Floramorph Pot', 'Sticky Pot', 'Unbreakable Pot', 'Black Hole Pot', 'Fever Pot'],
385: ['Sale Pot', 'Presto Pot', 'Floramorph Pot', 'Sticky Pot', 'Unbreakable Pot', 'Black Hole Pot', 'Fever Pot'],
402: ['Sale Pot', 'Presto Pot', 'Floramorph Pot', 'Sticky Pot', 'Unbreakable Pot', 'Black Hole Pot', 'Fever Pot'],
437: ['Sale Pot', 'Presto Pot', 'Floramorph Pot', 'Sticky Pot', 'Unbreakable Pot', 'Black Hole Pot', 'Fever Pot'],
1600: ['Exorcism Pot', 'Blessing Pot', 'Curse Pot' ],
1680: ['Exorcism Pot', 'Blessing Pot', 'Curse Pot' ],
1760: ['Exorcism Pot', 'Blessing Pot', 'Curse Pot' ],
1840: ['Exorcism Pot', 'Blessing Pot', 'Curse Pot' ],
1920: ['Exorcism Pot', 'Blessing Pot', 'Curse Pot' ],
2000: [
        'Exorcism Pot', 
        'Blessing Pot', 
       'Invincible Grass',
       'Cheery Grass',
       'Unlucky Seed',
       'Imabikiso',
       'Amnesia Grass',
       'Curse Pot', 
       'Water Pot', 
       'Heavenly Pot',
       'Strength Bracelet',
       'Can. Arm Bracelet',
       'Inacc. Bracelet',
       'Bunch Bracelet'
       ],
560: ['Exorcism Pot', 'Blessing Pot', 'Curse Pot'],
588: ['Exorcism Pot', 'Blessing Pot', 'Curse Pot'],
616: ['Exorcism Pot', 'Blessing Pot', 'Curse Pot'],
644: ['Exorcism Pot', 'Blessing Pot', 'Curse Pot'],
672: ['Exorcism Pot', 'Blessing Pot', 'Curse Pot'],
700: ['Exorcism Pot', 'Blessing Pot', 'Curse Pot', 'Water Pot', 
      'Strength Bracelet',
      'Can. Arm Bracelet',
      'Inacc, Bracelet',
      'Bunch Bracelet',
      'Invincible Grass',
      'Unlucky Seed', 
      'Imabikiso',
      'Amnesia Grass',
      'Heavenly Pot'],
2100: ['Synthesis Pot', 'Modders Pot', 'Water Pot', 'Heavenly Pot'],
2200: ['Water Pot', 'Heavenly Pot'],
2300: ['Water Pot', 'Heavenly Pot'],
2400: ['Water Pot', 'Heavenly Pot'],
2500: ['Zen Pot', 'Dodger Pot', 'Perceptive Pot', 'Reflection Pot', 'Water Pot', 'Heavenly Pot'],
735: ['Water Pot', 'Heavenly Pot'],
770: ['Water Pot', 'Heavenly Pot'],
805: ['Water Pot', 'Heavenly Pot'],
840: ['Water Pot', 'Heavenly Pot'],
875: ['Water Pot', 'Heavenly Pot', 'Zen Pot', 'Dodger Pot', 'Perceptive Pot', 'Reflection Pot'],
2625: ['Synthesis Pot', 'Modders Pot', 'Zen Pot', 'Dodger Pot', 'Perceptive Pot', 'Reflection Pot'],
2750: ['Zen Pot', 'Dodger Pot', 'Perceptive Pot', 'Reflection Pot'],
2875: ['Zen Pot', 'Dodger Pot', 'Perceptive Pot', 'Reflection Pot'],
3000: [
        'Zen Pot', 
        'Dodger Pot', 
        'Perceptive Pot', 
        'Reflection Pot', 
        'Lost Scroll', 
        'Sanctuary Scroll', 
       'Expulsion Scroll',
       'Bankruptcy Scroll',
       'Cleansing Bracelet',
       'Anti-Cnf. Bracelet',
       'Alert Bracelet',
       'Anti-Crs. Bracelet',
       'Staunch Bracelet',
       'Critical Bracelet',
       'Mojo Bracelet',
       'Monster Summoner',
       'Dozer Bracelet',
       'Trap Bracelet',
       ],
3125: ['Zen Pot', 'Dodger Pot', 'Perceptive Pot', 'Reflection Pot'],
918: ['Zen Pot', 'Dodger Pot', 'Perceptive Pot', 'Reflection Pot'],
962: ['Zen Pot', 'Dodger Pot', 'Perceptive Pot', 'Reflection Pot'],
1006: ['Zen Pot', 'Dodger Pot', 'Perceptive Pot', 'Reflection Pot'],
1093: ['Zen Pot', 'Dodger Pot', 'Perceptive Pot', 'Reflection Pot'],
3500: ['Extinction Scroll', 'Upgrade Pot', 'Degrade Pot', 
       'Lucky Pot', 'Unlucky Pot', 'Grilling Pot', 'Heal Pot', 'Zakoleft Pot', 
       'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot', 'Growth Bracelet',
        'Anti-Parry Bracelet',
        'Time Stop Bracelet',
        'Floating Bracelet',
       ],
3675: ['Heal Pot', 'Zakoleft Pot', 'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot','Upgrade Pot', 'Degrade Pot', 'Lucky Pot', 'Unlucky Pot', 'Grilling Pot'],
3850: ['Heal Pot', 'Zakoleft Pot', 'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot', 'Upgrade Pot', 'Degrade Pot', 'Lucky Pot', 'Unlucky Pot', 'Grilling Pot'],
4025: ['Upgrade Pot', 'Degrade Pot', 'Lucky Pot', 'Unlucky Pot', 'Grilling Pot', 'Heal Pot', 'Zakoleft Pot', 'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot'],
4200: ['Upgrade Pot', 'Degrade Pot', 'Lucky Pot', 'Unlucky Pot', 'Grilling Pot', 'Heal Pot', 'Zakoleft Pot', 'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot'],
4375: ['Upgrade Pot', 'Degrade Pot', 'Lucky Pot', 'Unlucky Pot', 'Grilling Pot', 'Heal Pot', 'Zakoleft Pot', 'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot'],
1225: ['Heal Pot', 'Zakoleft Pot', 'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot'],
1286: ['Heal Pot', 'Zakoleft Pot', 'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot'],
1347: ['Heal Pot', 'Zakoleft Pot', 'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot'],
1408: ['Heal Pot', 'Zakoleft Pot', 'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot'],
1470: ['Heal Pot', 'Zakoleft Pot', 'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot'],
1531: ['Heal Pot', 'Zakoleft Pot', 'Monster Pot', 'Klein Pot', 'Hilarious Pot', 'Shrine Maid Pot'],
6000: ['Synthesis Pot', 'Modders Pot'],
6300: ['Synthesis Pot', 'Modders Pot'],
6600: ['Synthesis Pot', 'Modders Pot'],
6900: ['Synthesis Pot', 'Modders Pot'],
7200: ['Synthesis Pot', 'Modders Pot'],
7500: ['Synthesis Pot', 'Modders Pot'],
2205: ['Synthesis Pot', 'Modders Pot'],
2310: ['Synthesis Pot', 'Modders Pot'],
2415: ['Synthesis Pot', 'Modders Pot'],
2520: ['Synthesis Pot', 'Modders Pot'],
10000: [
        'Upgrade Pot', 
        'Degrade Pot', 
        'Lucky Pot', 
        'Unlucky Pot', 
        'Grilling Pot',
        'Extinction Scroll',
        'Growth Bracelet',
        'Anti-Parry Bracelet',
        'Time Stop Bracelet',
        'Floating Bracelet',
        ],
10500: [
        'Upgrade Pot', 
        'Degrade Pot', 
        'Lucky Pot', 
        'Unlucky Pot', 
        'Grilling Pot',
        'Night Ward',
        'Scout Bracelet',
        'Trapper Bracelet',
        ],
11000: ['Upgrade Pot', 'Degrade Pot', 'Lucky Pot', 'Unlucky Pot', 'Grilling Pot'],
11500: ['Upgrade Pot', 'Degrade Pot', 'Lucky Pot', 'Unlucky Pot', 'Grilling Pot'],
12000: ['Upgrade Pot', 'Degrade Pot', 'Lucky Pot', 'Unlucky Pot', 'Grilling Pot'],
12500: ['Upgrade Pot', 'Degrade Pot', 'Lucky Pot', 'Unlucky Pot', 'Grilling Pot'],
10: [
     'Wet Scroll',
     'Weeds',
     'Piece of Paper'
     ],
3: [
     'Wet Scroll',
     'Weeds',
     'Piece of Paper'
     ],
100: [
    'Escape Scroll',
    'Navigation Scroll',
    'Oil Scroll',
    'Light Scroll',
    'Recommend. Letter',
    'Commend. Letter',
    'Otogiriso',
    'Antidote Grass',
    'Poison Grass',
    'Warp Grass',
    'Heal Grass',

    ],
35: [
    'Escape Scroll',
    'Navigation Scroll',
    'Oil Scroll',
    'Light Scroll',
    'Recommend. Letter',
    'Commend. Letter',
    'Otogiriso',
    'Antidote Grass',
    'Poison Grass',
    'Warp Grass',
    'Heal Grass',
    ],
200: ['Identify Scroll', 'Heal Grass'],
70: ['Identify Scroll', 'Heal Grass'],
300: [
    'Power Up Grass',
    'Upgrade Seed',
    'Perception Grass',
    'Swift Grass',
    'Stomach Expander',
    'Stomach Shrinker',
    'Confusion Grass',
    'Blinding Grass',
    'Nymph Grass',
    'Gathering Scroll',
    'Collection Scroll', 
    'Squid Sushi Scroll',

     ],
105: [
    'Power Up Grass',
    'Upgrade Seed',
    'Perception Grass',
    'Swift Grass',
    'Stomach Expander',
    'Stomach Shrinker',
    'Confusion Grass',
    'Blinding Grass',
    'Nymph Grass',
    'Gathering Scroll',
    'Collection Scroll', 
    'Squid Sushi Scroll',
     ],
500: [
    'Exorcism Scroll',
    'Fate Scroll',
    'Earth Scroll',
    'Plating Scroll',
    'Tag Scroll',
    'Sale Scroll',
    'Onigiri Scroll',
    'Pot God Scroll',
    'Extraction Scroll',
    'Blessing Scroll',
    'Curse Scroll',
    'Coupon Scroll',
    'Mate Scroll',
    'Darth Scroll',
    'Pot Dog Scroll',
    'Life Grass',
    'Strength Grass',
    'Dragon Grass',
    'Sleepy Grass',
    'Rage Grass',
    'Dracon Grass',
    ],
175: [ 'Exorcism Scroll',
    'Fate Scroll',
    'Earth Scroll',
    'Plating Scroll',
    'Tag Scroll',
    'Sale Scroll',
    'Onigiri Scroll',
    'Pot God Scroll',
    'Extraction Scroll',
    'Blessing Scroll',
    'Curse Scroll',
    'Coupon Scroll',
    'Mate Scroll',
    'Darth Scroll',
    'Pot Dog Scroll',
    'Life Grass',
    'Strength Grass',
    'Dragon Grass',
    'Sleepy Grass',
    'Rage Grass',
    'Dracon Grass',
    ],
800: [
    'Fear Scroll',
    'Trap Deletion Scrl',
    'Desert Scroll',
    'Trap Scroll',
    'Muzzled Scroll',
    'Grounded Scroll',
    'Attraction Scroll',

    ],
280: [
    'Fear Scroll',
    'Trap Deletion Scrl',
    'Desert Scroll',
    'Trap Scroll',
    'Muzzled Scroll',
    'Grounded Scroll',
    'Attraction Scroll',

    ],
5000: [
    'Blank Scroll',
    'Monster Detector',
    'Monsterphobic',
    'Item Detector',
    'Itemphobic',
    'Waterwalk Bracelet',
    'Wall Clip Bracelet',
    'Heal Bracelet',
    'Alleyway Bracelet',
    'Blink Bracelet',
    'Explosion Bracelet',
    'Nonary Bracelet',
    'Angel Seed',
    'SuperUnlucky Seed',
       ],
1750: [
     'Blank Scroll',
    'Monster Detector',
    'Monsterphobic',
    'Item Detector',
    'Itemphobic',
    'Waterwalk Bracelet',
    'Wall Clip Bracelet',
    'Heal Bracelet',
    'Alleyway Bracelet',
    'Blink Bracelet',
    'Explosion Bracelet',
    'Nonary Bracelet',
       ],
30000: [
       'Night Ward',
      'Scout Bracelet',
       'Trapper Bracelet',
       ],
50000: ['VIP Bracelet'],
17500: ['VIP Bracelet'],
}
