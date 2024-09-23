def collision(b = (0,0,0,0),a = (0,0,0,0)):
      ''' a,b are rectangles,(x,y,l,h)
       this code checks if a enters b's domain '''
      
      if b[0] <= a[0] <= b[0] + b[2] or b[0] <= a[0] + a[2] <= b[0] + b[2]:
            if b[1] <= a[1] + a[3] <= b[1] + b[3] or b[1] <= a[1] <= b[1] + b[3]:
                  return True      
      return False
