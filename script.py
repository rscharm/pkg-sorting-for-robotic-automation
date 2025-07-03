def sort(width, height, length, mass):
  if mass >= 20:
      volume = width * height * length
      if volume >= 1000000 or max(width, height, length) >= 150:
          return "REJECTED"
      else:
          return "SPECIAL"
  
  volume = width * height * length
  if volume >= 1000000 or max(width, height, length) >= 150:
      return "SPECIAL"
  
  return "STANDARD"