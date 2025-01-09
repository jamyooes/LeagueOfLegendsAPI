# This python file filters the data into useful attributes

class ChampData():
    def __init__(self, data):
        self.raw_data = data
    def champ_stats(self):
        """
        The function was created to help read the raw data from the API for champions
        
        Arguments:
        Data (str): raw string data of the champion's stats
        
        Data Attributes
        hp
        hpperlevel
        mp
        mpperlevel
        movespeed
        armor
        armorperlevel
        spellblock
        spellblockperlevel
        attackrange
        hpregen
        hpregenperlevel
        mpregen
        mpregenperlevel
        crit
        critperlevel
        attackdamage
        attackdamageperlevel
        attackspeedperlevel
        attackspeed
        """
        self.stats_arr = self.raw_data["stats"]
        
        # print(data["stats"])
        for stat_type in self.stats_arr:
            print(f"{stat_type}: {self.raw_data['stats'][stat_type]}")
    
    def champ_spell(self):
        """
        Readable champion spell
        
        id - Internal naming for the ability
        name - Champion ability name
        description - Simple description for the ability
        tooltip - Has additional details on ability and specifics
        leveltip - Not too sure what this is, I think it is a tool tip on hover?
        maxrank - Ability max-rank
        cooldown - CD in seconds
        cooldownBurn - string represetnation of cooldown
        cost - Mana/Energy Costs
        costBurn - Not too sure what this is (I'm guess mana costs)
        datavalues - Not too sure what this is either
        effect - No clue
        effectBurn - No clue
        vars - No clue
        costType - Resource Type
        maxammo - No clue
        range - AA range?
        rangeBurn - No clue
        image - image
        resource - Same as resource type
        """
        self.spell = self.raw_data["spells"]
        # for spell_text in self.spell:
        #     for per_spell in spell_text:
        #         print(spell_text)
        #         break
        print(self.spell[2]["resource"])
        # print(self.spell)
        