# -*- coding: utf-8 -*-
"""
Created on Thu May 29 11:16:52 2025

@author: Orion-Trd-1
"""
import time

class Microwave:
    def __init__(self,brand:str,power_rating:str) -> None:
        self.brand = brand
        self.power_rating =power_rating
        self.turned_on: bool =False
    
    def turn_on(self) -> None:
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on")
        else:
            self.turned_on =True
            print(f"Microwave ({self.brand}) is now turned on")
            
    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on =False
            print(f"Microwave ({self.brand}) is now turned off")
        else:
            print(f"Microwave ({self.brand}) is alrady turned off")
            
    def run(self,seconds: int) -> None:
        if self.turned_on:
            print(f"Running ({self.brand}) for { seconds} seconds")
            time.sleep(seconds)
        else:
            print("Turn on Microwave first . . ")
  
            
  
    #String dunder method
    def __add__(self,other):
        return f"{self.brand} + {other.brand}"
    def __mul__(self,other):
        return f"{self.brand} * {other.brand}"
        
    def __str__(self) -> str:
        return f"{self.brand} (Rating:{self.power_rating})"
    
    def __repr__(self) -> str:
        return f'Microwave (brand=(self.brand},power rating'

#Type annotation
smeg: Microwave = Microwave(brand='Smeg',power_rating='B')
bosch: Microwave = Microwave(brand='Bosch',power_rating='C')
smeg.turn_on()
smeg.turn_on()
smeg.run(10)
smeg.turn_off()

bosch.turn_on()
bosch.turn_on()
bosch.run(10)
bosch.turn_off()

print(smeg + bosch)
print(smeg * bosch)


print(repr(smeg))
'''
print(smeg)
print(smeg.brand)
print(smeg.power_rating)

bosch: Microwave = Microwave(brand='Bosch',power_rating='C')
print(bosch)
print(bosch.brand)
print(bosch.power_rating)
'''