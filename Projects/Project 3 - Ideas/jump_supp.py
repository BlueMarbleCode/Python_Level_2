def JUMP(pos, i, h, floaty = False):

      if floaty == True:
            tup_heights = 0,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6

      else:
            tup_heights = 0,-3,0,-2,0,-1,0,0,0,1,0,2,0,3
      
      pos[1] += h * tup_heights[i]
      i += 1
      
      if i > len(tup_heights)-1:
            i = 0
            t = False
      else:
            t = True
      
      return pos, [t,i]
