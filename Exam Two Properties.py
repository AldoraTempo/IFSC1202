data = """059 Manufacturers Alley,Little Rock,AR,72203,175698
39500 Division Avenue,Little Rock,AR,72210,131583
4281 Elka Junction,Little Rock,AR,72207,125101
0051 Harper Street,Little Rock,AR,72201,166462
6020 Lake View Street,Little Rock,AR,72209,189605
7753 Dottie Hill,Little Rock,AR,72202,165830
94894 Becker Court,Little Rock,AR,72202,172254
9 Little Fleur Point,Little Rock,AR,72211,133232
3 Buhler Way,Little Rock,AR,72201,1917670908 
Hintze Way,Little Rock,AR,72211,181696
463 Blue Bill Park Court,Little Rock,AR,72211,101246
659 Prairieview Court,Little Rock,AR,72202,142334
9908 Russell Parkway,Little Rock,AR,72201,167982
8443 Morningstar Pass,Little Rock,AR,72204,181476
49 Lotheville Avenue,Little Rock,AR,72211,158312
1845 Bashford Alley,Little Rock,AR,72211,134862
13 Lakewood Gardens Trail,Little Rock,AR,72204,128958
5217 Starling Trail,Little Rock,AR,72207,197032
34405 Orin Trail,Little Rock,AR,72209,112963
3293 Pankratz Lane,Little Rock,AR,72208,157523
4 Haas Pass,Little Rock,AR,72207,1918371810 
Lakeland Park,Little Rock,AR,72204,181223
5 Arkansas Crossing,Little Rock,AR,72204,117110
6090 Fisk Way,Little Rock,AR,72212,128931
2 Tennessee Hill,Little Rock,AR,72208,125434
54957 Arizona Alley,Little Rock,AR,72205,198821
9 Bluejay Hill,Little Rock,AR,72209,111076
25588 Fordem Way,Little Rock,AR,72209,106311
0602 Clemons Point,Little Rock,AR,72210,197008
36369 Eastlawn Parkway,Little Rock,AR,72202,140790
64 Novick Park,Little Rock,AR,72202,183065
002 Dunning Junction,Little Rock,AR,72204,173228
0659 Calypso Way,Little Rock,AR,72212,175881
120 Gina Point,Little Rock,AR,72203,116163
403 Elmside Court,Little Rock,AR,72207,194442
11 La Follette Pass,Little Rock,AR,72209,134469
525 Golden Leaf Plaza,Little Rock,AR,72210,176651
534 Havey Lane,Little Rock,AR,72201,170284
10 Russell Center,Little Rock,AR,72201,120882
99176 Forest Dale Trail,Little Rock,AR,72209,102722
0998 Pennsylvania Lane,Little Rock,AR,72206,158116
377 South Terrace,Little Rock,AR,72204,131828
202 Sutherland Street,Little Rock,AR,72205,131678
4442 Tennessee Way,Little Rock,AR,72203,162751
0883 Monica Point,Little Rock,AR,72204,111032
3 Magdeline Park,Little Rock,AR,72207,177268
24 Gateway Junction,Little Rock,AR,72207,162185
85 Karstens Street,Little Rock,AR,72207,167212
94 Stang Parkway,Little Rock,AR,72202,181151
29 Bartillon Lane,Little Rock,AR,72203,110047
73026 Union Lane,Little Rock,AR,72207,195593
5028 Troy Lane,Little Rock,AR,72206,150712
0102 Mcbride Junction,Little Rock,AR,72205,112318
18 Sachtjen Hill,Little Rock,AR,72204,118558
71 Dorton Crossing,Little Rock,AR,72202,145340
045 Upham Crossing,Little Rock,AR,72201,101077
884 Porter Park,Little Rock,AR,72206,155051
3237 Hudson Road,Little Rock,AR,72211,176980
2 Crest Line Hill,Little Rock,AR,72206,134856
63 Mayfield Pass,Little Rock,AR,72209,173839
615 Colorado Road,Little Rock,AR,72205,128944
643 Daystar Park,Little Rock,AR,72211,172910
661 Browning Drive,Little Rock,AR,72212,115549
02574 Springs Avenue,Little Rock,AR,72211,135663
62 Continental Parkway,Little Rock,AR,72212,134294
80 Haas Circle,Little Rock,AR,72208,135438
099 Buhler Street,Little Rock,AR,72210,183480
93164 Talisman Avenue,Little Rock,AR,72209,124993
83820 3rd Center,Little Rock,AR,72203,158908
1296 American Road,Little Rock,AR,72204,186895
03430 Marcy Court,Little Rock,AR,72208,174788
8 American Center,Little Rock,AR,72204,173532
2891 Reindahl Parkway,Little Rock,AR,72205,199151
89 Butternut Plaza,Little Rock,AR,72202,132403
11238 Southridge Alley,Little Rock,AR,72201,195688
7022 Steensland Pass,Little Rock,AR,72208,158612
27 Dawn Place,Little Rock,AR,72211,153451
225 Autumn Leaf Street,Little Rock,AR,72204,149674
7121 Division Hill,Little Rock,AR,72205,101253
520 Mockingbird Point,Little Rock,AR,72201,176456
088 David Point,Little Rock,AR,72202,164599
17878 Vera Alley,Little Rock,AR,72206,199500
89261 Clyde Gallagher Alley,Little Rock,AR,72212,187743
2216 Dapin Terrace,Little Rock,AR,72203,104616
93364 Fremont Plaza,Little Rock,AR,72207,176958
9 Quincy Terrace,Little Rock,AR,72202,171171
285 Express Pass,Little Rock,AR,72207,152820
73478 Colorado Alley,Little Rock,AR,72206,151084
757 School Hill,Little Rock,AR,72201,146380
8 Mcguire Point,Little Rock,AR,72207,105486
59 Gale Way,Little Rock,AR,72202,112377
256 Caliangt Point,Little Rock,AR,72203,119768
213 East Place,Little Rock,AR,72205,156275
24 Dawn Center,Little Rock,AR,72207,193896
9715 Banding Point,Little Rock,AR,72202,180041
0423 Dryden Place,Little Rock,AR,72201,166105
76852 Towne Court,Little Rock,AR,72205,136950
1801 Havey Pass,Little Rock,AR,72209,104072
24766 Springs Park,Little Rock,AR,72202,153282
5918 Buhler Place,Little Rock,AR,72208,149203"""

properties = []
zipcodes = []

for line in data.splitlines():
  ds = line.split(',')
  ad = ds[0]
  c = ds[1]
  s = ds[2]
  zc = ds[3]
  pr = float(ds[4])
  properties.append([ad, c, s, zc, pr])

for prop in properties:
  zc = prop[3]
  pr = prop[4]
  
  for zip_row in zipcodes:
      if zip_row[0] == zc:
          zip_row[1] += 1
          zip_row[2] += pr
          break
        
  else:
      zipcodes.append([zc, 1, pr])

print(f"{'Zipcode':<10} {'Count':<20} {'Average':<25}")

for zip_row in zipcodes:
    zc = zip_row[0]
    ct = zip_row[1]
    tp = zip_row[2]
    ap = tp / ct if ct > 0 else 0
    print(f"{zc:<10} {ct:<20} {ap:<25.2f}")