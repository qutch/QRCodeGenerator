def textToBinary(string):
  finalBinary = []
  for letter in string:
    asciiCode = ord(letter) # Converts each character into its ascii code
    binary = "00000000" # Initial binary code to be edited
    
    curPow = 0
    idx = 7

    for i in range(0, 7): # Loops through 0 to 7 to find the max power of 2 needed to subtract and finds the index of the array to place the binary 1 at
      if asciiCode >= 2 ** (i + 1):
        curPow += 1
        idx -= 1
      else:
        break
    
    
    while curPow >= 0: # Goes through the array of binary as a list and puts in 1's where needed
      if asciiCode >= 2 ** curPow:

        binary = list(binary)
        binary[idx] = '1'


        asciiCode -= 2 ** curPow

      idx += 1
      curPow -= 1
    

    returnBinary = ""
    for l in binary:
      returnBinary += l
    
    finalBinary.append(returnBinary)

  return finalBinary