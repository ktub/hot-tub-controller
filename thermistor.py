
voltage_table = [
(0.97,-40.0),
(0.96,-32.8),
(0.95,-25.6),
(0.94,-20.2),
(0.93,-14.8),
(0.92,-11.2),
(0.91,-5.8),
(0.90,-2.2),
(0.89,1.4),
(0.88,5.0),
(0.87,6.8),
(0.86,10.4),
(0.85,12.2),
(0.84,15.8),
(0.83,17.6),
(0.82,19.4),
(0.81,23.0),
(0.80,24.8),
(0.79,26.6),
(0.78,28.4),
(0.77,30.2),
(0.76,33.8),
(0.75,35.6),
(0.74,37.4),
(0.73,39.2),
(0.72,41.0),
(0.71,42.8),
(0.70,44.6),
(0.69,46.4),
(0.68,48.2),
(0.67,50.0),
(0.65,51.8),
(0.64,53.6),
(0.63,55.4),
(0.62,57.2),
(0.61,59.0),
(0.60,60.8),
(0.59,62.6),
(0.58,64.4),
(0.57,66.2),
(0.56,68.0),
(0.54,69.8),
(0.53,71.6),
(0.52,73.4),
(0.51,75.2),
(0.50,77.0),
(0.49,78.8),
(0.48,80.6),
(0.47,82.4),
(0.46,84.2),
(0.45,86.0),
(0.44,87.8),
(0.43,89.6),
(0.42,91.4),
(0.41,93.2),
(0.40,95.0),
(0.39,96.8),
(0.38,98.6),
(0.37,100.4),
(0.36,102.2),
(0.35,104.0),
(0.34,105.8),
(0.33,107.6),
(0.32,109.4),
(0.31,111.2),
(0.30,113.0),
(0.29,116.6),
(0.28,118.4),
(0.27,120.2),
(0.26,122.0),
(0.25,125.6),
(0.24,127.4),
(0.23,131.0),
(0.22,132.8),
(0.21,136.4),
(0.20,140.0),
(0.19,141.8),
(0.18,145.4),
(0.17,149.0),
(0.16,152.6),
(0.15,156.2),
(0.14,159.8),
(0.13,165.2),
(0.12,170.6),
(0.11,174.2),
(0.10,181.4),
(0.09,186.8),
(0.08,194.0),
(0.07,201.2),
(0.06,212.0),
]

def adc_value_to_F(adc_value):
    value = adc_value / 1024.0
    value = 1.0 - value   # IF WIRED BACKWARD FROM ORIGINAL
    for i in range(1, len(voltage_table) - 1):
        if value <= voltage_table[i - 1][0] and value > voltage_table[i][0]:
            # interpolate between the two values
            delta = value - voltage_table[i - 1][0]
            step = voltage_table[i][0] - voltage_table[i-1][0]
            return voltage_table[i-1][1] + ((delta / (1.0 * step)) * (voltage_table[i][1] - voltage_table[i-1][1]))
    return 0  # raise Exception("No matching value in table: {}".format(value))
