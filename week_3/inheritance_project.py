class City:
    def __init__(self, name, country, population):
        self.name = name
        self.country = country
        self.population = population

    def __str__(self):
        return f"{self.name}, {self.country} - Population: {self.population}"
    

class Sahiwal(City):
    def __init__(self, population):
        super().__init__("Sahiwal", "Pakistan", population)

    def __str__(self):
        return f"Sahiwal, Pakistan - Population: {self.population}"
    
    def towns(self):
        return ["Fareed Town", "Shadman Town", "Green Town", "Garden Town"]
    

class Lahore(City):
    def __init__(self, population):
        super().__init__("Lahore", "Pakistan", population)

    def __str__(self):
        return f"Lahore, Pakistan - Population: {self.population}"
    
    def towns(self):
        pass
