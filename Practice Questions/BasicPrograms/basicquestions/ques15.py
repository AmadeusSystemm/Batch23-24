tileLen=eval(input("Enter the length of tile-"))
tilewid=eval(input("Enter the width of tile-"))
floorlen=eval(input("Enter the Length of floor-"))
floorwid=eval(input("Enter the Width of floor-"))
arfloor=floorlen*floorwid
artile=tileLen*tilewid
noftile=arfloor//artile
print("Number of tiles required required are",noftile)