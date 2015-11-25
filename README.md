Front Face : Black
Left : Red
Right : Orange
Up : Blue
Down : Green
Back : Yellow

Visible faces:

                 +-------+-------+-------+
                /       /       /       /|
               /  30   /   4   /  27   / |
              +-------+-------+-------+  |
             /       /       /       /|28+
            /   6   /       /   2   / | /|
           +-------+-------+-------+  |/ |
          /       /       /       /|3 +  |
         /  33   /   0   /  24   / | /|21+
        +-------+-------+-------+  |/ | /|
        |       |       |       |26+  |/ |
        |  35   |   1   |   25  | /|  +  |
        |       |       |       |/ | /|47+
        +-------+-------+-------+  |/ | /
        |       |       |       |17+  |/
        |  18   |       |  16   | /|11+
        |       |       |       |/ | /
        +-------+-------+-------+  |/
        |       |       |       |37+
        |  40   |   9   |  38   | /
        |       |       |       |/
        +-------+-------+-------+


Hidden faces:

                 +-------+-------+-------+
                /|       |       |       |
               / |  31   |   5   |  29   |
              +  |       |       |       |
             /|32+-------+-------+-------+
            / | /|       |       |       |
           +  |/ |  22   |       |  20   |
          /|7 +  |       |       |       |
         / | /|23+-------+-------+-------+
        +  |/ | /|       |       |       |
        |34+  |/ |  44   |  13   |  46   |
        | /|  +  |       |       |       |
        |/ | /|43+-------+-------+-------+
        +  |/ | /       /       /       /
        |19+  |/  42   /  12   /  45   /
        | /|15+-------+-------+-------+
        |/ | /       /       /       /
        +  |/  14   /       /  10   /
        |41+-------+-------+-------+
        | /       /       /       /
        |/  39   /   8   /   36  /
        +-------+-------+-------+

Edge pieces:

0 - 1 = orange - blue
2 - 3 = orange - yellow
4 - 5 = orange - green
6 - 7 = orange - white
8 - 9 = red - blue
10 - 11 = red - yellow
12 - 13 = red - green
14 - 15 = red - white
16 - 17 = blue - yellow
18 - 19 = blue - white
20 - 21 = green - yellow
22 - 23 = green - white

Corner Pieces:

24-25-26 = orange-blue-yellow
27-28-29 = orange-yellow-green
30-31-32 = orange-green-white
33-34-35 = orange-white-blue
36-37-38 = red-yellow-blue
39-40-41 = red-blue-white
42-43-44 = red-white-green
45-46-47 = red-green-yellow

Take image 
Crop for cube
Extract colors
Create grids
Take centroid of bounding box
Locate the centroid in seperate grid boxes
find colors attached to that cubie and form a graph 

1> Get colors
2> Locate every color
3> Create graph of all colors
4> Name all the nodes according to color groups 
                                   _____________________________________________
                                  |     _________________________________       |  
                                  |    |     ______________________      |      |
                                  |    |    |                      |     |      |
                        	 ____ ____ ____                    |     |      | 
                                | t1 | t2 | t3 |_____________      |     |      |
                    		|____|____|____|             |     |     |      |
                        	| t4 |orng| t6 |_________    |     |     |      |
                        	|____|top_|____|         |   |     |     |      |
                                | t7 | t8 | t9 |___      |   |     |     |      | 
                         	|____|____|____|   |     |   |     |     |      |
               ____ ____ ____    ____ ____ ____   ____ ____ ____   ____ ____ ____
              | l1 | l2 | l3 |  | f1 | f2 | f3 | | r1 | r2 | r3 | | b1 | b2 | b3 |
              |____|____|____|	|____|____|____| |____|____|____| |____|____|____| 
              | l4 |whte| l6 |	| f4 |Blue| f6 | | r4 |ylw | r6 | | b4 |grn | b6 |
              |____|left|____|	|____|frnt|____| |____|rigt|____| |____|back|____|
              | l7 | l8 | l9 |	| f7 | f8 | f9 | | r7 | r8 | r9 | | b7 | b8 | b9 |
              |____|____|____|	|____|____|____| |____|____|____| |____|____|____|						
                        	 ____ ____ ____
                                |bo1 |bo2 |bo3 |
                      		|____|____|____|
                        	|bo4 |red |bo6 |
                        	|____|botm|____|
                                |bo7 |bo8 |bo9 |	
                         	|____|____|____|	
