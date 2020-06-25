# PrimePyramidSolver
This project was made for solving pyramids made from Prime Numbers and Non Prime Numbers. Just like this example below.

                                215
                              193 124
                            117 237 442
                          218 935 347 235
                        320 804 522 417 345
                      229 601 723 835 133 124
                    248 202 277 433 207 263 257
                  359 464 504 528 516 716 871 182
                461 441 426 656 863 560 380 171 923
              381 348 573 533 447 632 387 176 975 449
            223 711 445 645 245 543 931 532 937 541 444
          330 131 333 928 377 733 017 778 839 168 197 197
        131 171 522 137 217 224 291 413 528 520 227 229 928
      223 626 034 683 839 053 627 310 713 999 629 817 410 121
    924 622 911 233 325 139 721 218 253 223 107 233 230 124 233


The code will find the path with the higgest total while avoiding the prime numbers. It will print all available options while printing the highest totaled solution just like this: 
                                            *215		
                                          193		*124		
                                      117		*237		442		
                                  218		*935		347		235		
                              320		804		*522		417		345		
                            229		601		723		*835		133		124		
                        248		202		277		433		*207		263		257		
                      359		464		504		528		516		*716		871		182		
                    461		441		426		656		863		*560		380		171		923		
                 381 	348		573		533		447		*632		387		176		975		449		
              223		711		445		645		245		543		*931		532		937		541		444		
           330		131		333		928		377		733		17		*778		839		168		197		197		
        131		171		522		137		217		224		291		413		*528		520		227		229		928		
    223		626		34		683		839		53		627		310		*713		999		629		817		410		121		
924		622		911		233		325		139		721		218		*253		223		107		233		230		124		233		

Path with the biggest value total:   [215, 124, 237, 935, 522, 835, 207, 716, 560, 632, 931, 778, 528, 713, 253]	Value total:   8186


# How to use 

You need to change the example_1 from the PyramidSource
