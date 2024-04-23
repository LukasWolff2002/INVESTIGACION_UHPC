import math

# Velocidad angular en revoluciones por segundo
revolutions_per_second = 97.1

# Convertir a radianes por segundo
angular_velocity_radians_per_second = revolutions_per_second * 2 * math.pi

# Calcular el período de una revolución
revolution_period = 1 / angular_velocity_radians_per_second

# Calcular el tiempo para media vuelta
half_turn_time = 0.08 * revolution_period

print("Tiempo para media vuelta:", half_turn_time, "segundos")