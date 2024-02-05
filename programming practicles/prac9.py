class smartmeter:
    def __init__(self):
        self.energy_balance = 1000
        self.solar_panels = False
    
    def use_energy(self, energy_needed):
        self.energy_balance -= energy_needed


def main():
    smart_meter = smartmeter()
    print(smart_meter.energy_balance)
    smart_meter.use_energy(100)
    print(smart_meter.energy_balance)
    

main()




    
