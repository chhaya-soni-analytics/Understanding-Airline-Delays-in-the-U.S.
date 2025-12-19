# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 16:38:58 2025

@author: WIN10
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/WIN10/Downloads/Airline_Delay_Cause.csv")
df.head() 
df.info() 

df.shape
df.describe() 
df.isnull().sum() 
df.isnull() 

df["carrier"] = df["carrier"].fillna("NA")

df["airport"] = df["airport"].fillna("NA")

df["arr_flights"] = df["arr_flights"].fillna(df["arr_flights"].mean()) 

df["carrier_name"] = df["carrier_name"].fillna("NA") 

df["arr_flights"] = df["arr_flights"].fillna(df["arr_flights"].mean()) 

df["arr_del15"] = df["arr_del15"].fillna(df["arr_del15"].mean()) 
df["carrier_ct"] = df["carrier_ct"].fillna(df["carrier_ct"].mean()) 
df["weather_ct"] = df["weather_ct"].fillna(df["weather_ct"].mean()) 
df["nas_ct"] = df["nas_ct"].fillna(df["nas_ct"].mean()) 
df["security_ct"] = df["security_ct"].fillna(df["security_ct"].mean()) 
df["late_aircraft_ct"] = df["late_aircraft_ct"].fillna(df["late_aircraft_ct"].mean()) 

df["arr_cancelled"] = df["arr_cancelled"].fillna(df["arr_cancelled"].mean()) 
df["arr_diverted"] = df["arr_diverted"].fillna(df["arr_diverted"].mean()) 
df["arr_delay"] = df["arr_delay"].fillna(df["arr_delay"].mean()) 
df["carrier_delay"] = df["carrier_delay"].fillna(df["carrier_delay"].mean()) 
df["weather_delay"] = df["weather_delay"].fillna(df["weather_delay"].mean()) 
df["nas_delay"] = df["nas_delay"].fillna(df["nas_delay"].mean()) 
df["security_delay"] = df["security_delay"].fillna(df["security_delay"].mean()) 
df["late_aircraft_delay"] = df["late_aircraft_delay"].fillna(df["late_aircraft_delay"].mean()) 

df["delay_rate"] = (df["arr_del15"] / df["arr_flights"]) * 100
overall_delay_rate = df["delay_rate"].mean()
print("Overall Delay Rate (%):", overall_delay_rate)
 


#EDA

df.groupby("year")["arr_flights"].sum() 

delay_cols = ["carrier_delay","weather_delay","nas_delay","security_delay","late_aircraft_delay"]
df[delay_cols].sum() 

df.groupby("airport")["arr_del15"].sum().sort_values(ascending=False).head(10) 

airline_delay = df.groupby("carrier")["arr_del15"].sum().sort_values(ascending=False) 
print("Delayed Flights by Airline:\n", airline_delay)


airline_delay.plot(kind="bar", figsize=(10,5))
plt.title("Delayed Flights by Airline")
plt.ylabel("Delayed Flights")
plt.show()


df.groupby("year")["arr_flights"].sum().plot(kind="bar")
plt.title("Total Flights Per Year")
plt.ylabel("Flights")
plt.show()



df[delay_cols].sum().plot(kind="bar")
plt.title("Total Delay by Type")
plt.ylabel("Minutes of Delay")
plt.show()


airport_delay = df.groupby("airport_name")["arr_del15"].sum().sort_values().tail(10).plot(kind="barh")
plt.title("Top 10 Airports with Most Delays")
plt.xlabel("Delayed Flights")
plt.show()

monthly_delay = df.groupby("month")["arr_delay"].mean()
print(monthly_delay)
    
monthly_delay.plot(kind="line", marker="o")
plt.title("Average Delay Per Month")
plt.ylabel("Delay (Minutes)")
plt.xlabel("Month")
plt.show()

#late aircraft delay trend

late_aircraft = df.groupby("year")["late_aircraft_delay"].sum()
late_aircraft.plot(kind="line",marker="o")
plt.title("Late Aircraft Delay Trend Over Years")
plt.ylabel("Minutes")
plt.show()





df["delay_severity"] = (df["arr_delay"] / df["arr_flights"]) * 100

severity_airport = df.groupby("airport_name")["delay_severity"].mean().sort_values(ascending=False)
print(severity_airport.head(10))
severity_airport.head(10).plot(kind="barh")
plt.title("Worst Airports by Delay Severity")
plt.xlabel("Severity Index (%)")
plt.show()


#🧭 15. Airline–Airport Interaction (Which airline is bad where?)
pair = df.groupby(["carrier","airport_name"])["arr_del15"].sum().sort_values(ascending=False)
print(pair.head(15))


monthly_cancel_divert = df.groupby("month")[["arr_cancelled","arr_diverted"]].sum()
print(monthly_cancel_divert)

monthly_cancel_divert.plot(kind="bar")
plt.title("Monthly Cancellations & Diversions")
plt.ylabel("Count")
plt.show()


df["delay_probability"] = df["arr_del15"] / df["arr_flights"]
print(df["delay_probability"].mean())
