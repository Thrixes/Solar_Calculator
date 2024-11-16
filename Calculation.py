#1kwh to usd : 0.17$
country_avg_kWh = 0.17



#1 Calculate Monthly Electricty Consumption
#cost per KWh varries from country to country. 
kWh_consumption = monthly_bill/country_avg_kWh
  print(kWh_consumption)

#2 Daily average consumption
daily_kWh_consumption = kWh_consumption / 30 
  #result is daily avg
  print(daily_kWh_consumption)

#3 Solar energy requirement 
#peak sun hours differs from country to country 
solar_daily_requirement = daily_kWh_consumption/ peak_sun_hours
