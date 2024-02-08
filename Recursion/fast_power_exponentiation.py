def fast_power_exponentation(a, power):
  if power == 0:
    return 1

  v = fast_power_exponentation(a, power//2)

  if power % 2 == 0:
    return v * v
  else:
    return v * v * a

a = 2
power = 5
ans = fast_power_exponentation(a, power)
print(ans)