#D = (V**2*sin(2*angle))/g
#H = (V**2*sin**2(angle))/2g
#T = (2*V*sin(angle))/g
import math
#На вход V и angle в градусах
#Время, максимальная высота, дальность


# P - Па
# Temp - в K
# R = 287.05
# p = P/(R*T) - плотность возд.

# С - коэф. сопротивления
# A - площадь сечения пули
#F = 0.5*C*p*A*V**2

#rho = 1.225
#dt = 0.001

#vx, vy = V * cos(angle_rad), V * sin(angle_rad)
#x, y = 0, 0 
# x_vals, y_vals = [x], [y]

# v = sqrt(vx**2 + vy**2)
# F = 0.5*C*p*A*V**2
# ax = -F * (vx/v) / m
# ay = -g*F * (vx/v) / m

# vx += ax * dt 
# vy += ay * dt 

# x += vx *dt 
# y += vy *dt 