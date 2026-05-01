# Author: Aidan Callan

def load_interstates(sys):
    # I-2
    sys.add_interstate("I-2/I-69C","I-2/I-69","I-2",29)

    # I-4
    sys.add_interstate("I-4/I-75","I-4/I-95","I-4",122)

    # I-5
    sys.add_interstate("I-5/I-8","I-5/I-10","I-5",113)
    sys.add_interstate("I-5/I-10","I-5/I-80","I-5",387)
    sys.add_interstate("I-5/I-80","I-5/I-84","I-5",575)
    sys.add_interstate("I-5/I-84","I-5/I-90","I-5",170)

    # I-8
    sys.add_interstate("I-5/I-8","I-8/I-15","I-8",5)
    sys.add_interstate("I-8/I-15","I-8/I-10","I-8",341)

    # I-10
    sys.add_interstate("I-5/I-10","I-10/I-15","I-10",39)
    sys.add_interstate("I-10/I-15","I-10/I-17 @ West PHX","I-10",327)
    sys.add_interstate("I-10/I-17 @ West PHX","I-10/I-17 @ East PHX","I-10",6)
    sys.add_interstate("I-10/I-17 @ East PHX","I-8/I-10","I-10",49)
    sys.add_interstate("I-8/I-10","I-10/I-19","I-10",60)
    sys.add_interstate("I-10/I-19","I-10/I-25","I-10",275)
    sys.add_interstate("I-10/I-25","I-10/I-20","I-10",206)
    sys.add_interstate("I-10/I-20","I-10/I-35","I-10",383)
    sys.add_interstate("I-10/I-35","I-10/I-37","I-10",4)
    sys.add_interstate("I-10/I-37","I-10/I-45","I-10",193)
    sys.add_interstate("I-10/I-45","I-10/I-69","I-10",1)
    sys.add_interstate("I-10/I-69","I-10/I-49","I-10",214)
    sys.add_interstate("I-10/I-49","I-10/I-12","I-10",56)
    sys.add_interstate("I-10/I-12","I-10/I-55","I-10",49)
    sys.add_interstate("I-10/I-55","I-10/I-12/I-59","I-10",57)
    sys.add_interstate("I-10/I-12/I-59","I-10/I-65","I-10",103)
    sys.add_interstate("I-10/I-65","I-10/I-75","I-10",341)
    sys.add_interstate("I-10/I-75","I-10/I-95","I-10",65)

    # I-11
    # ONLY INTERSECTION: I-11/I-15

    # I-12
    sys.add_interstate("I-10/I-12","I-12/I-55","I-12",37)
    sys.add_interstate("I-12/I-55","I-10/I-12/I-59","I-12",48)

    # I-14

    # I-15
    sys.add_interstate("I-8/I-15","I-10/I-15","I-15",102)
    sys.add_interstate("I-10/I-15","I-15/I-40","I-15",72)
    sys.add_interstate("I-15/I-40","I-11/I-15","I-15",154)
    sys.add_interstate("I-11/I-15","I-15/I-70","I-15",242)
    sys.add_interstate("I-15/I-70","I-15/I-80","I-15",172)
    sys.add_interstate("I-15/I-80","I-15/I-84 @ Ogden","I-15",34)
    sys.add_interstate("I-15/I-84 @ Ogden","I-15/I-84 @ Tremonton","I-15",39)
    sys.add_interstate("I-15/I-84 @ Tremonton","I-15/I-86","I-15",92)
    sys.add_interstate("I-15/I-86","I-15/I-90","I-15",244)

    # I-16
    sys.add_interstate("I-16/I-75","I-16/I-95","I-16",156)

    # I-17
    sys.add_interstate("I-10/I-17 @ East PHX","I-10/I-17 @ West PHX","I-17",7)
    sys.add_interstate("I-10/I-17 @ West PHX","I-17/I-40","I-17",139)

    # I-19

    # I-20
    sys.add_interstate("I-10/I-20","I-20/I-30","I-20",421)
    sys.add_interstate("I-20/I-30","I-20/I-35W","I-20",18)
    sys.add_interstate("I-20/I-35W","I-20/I-35E","I-20",29)
    sys.add_interstate("I-20/I-35E","I-20/I-45","I-20",5)
    sys.add_interstate("I-20/I-45","I-20/I-49","I-20",179)
    sys.add_interstate("I-20/I-49","I-20/I-55","I-20",216)
    sys.add_interstate("I-20/I-55","I-20/I-59 @ Meridian","I-20",85)
    sys.add_interstate("I-20/I-59 @ Meridian","I-20/I-59/I-65","I-20",147)
    sys.add_interstate("I-20/I-59/I-65","I-20/I-59 @ Birmingham","I-20",5)
    sys.add_interstate("I-20/I-59 @ Birmingham","I-20/I-75/I-85","I-20",141)
    sys.add_interstate("I-20/I-75/I-85","I-20/I-26","I-20",208)
    sys.add_interstate("I-20/I-26","I-20/I-77","I-20",13)
    sys.add_interstate("I-20/I-77","I-20/I-95","I-20",66)

    # I-22

    # I-24
    sys.add_interstate("I-24/I-57","I-24/I-69 @ Calvert City","I-24",63)
    sys.add_interstate("I-24/I-69 @ Calvert City","I-24/I-69 @ Eddyville","I-24",16)
    sys.add_interstate("I-24/I-69 @ Eddyville","I-24/I-65","I-24",97)
    sys.add_interstate("I-24/I-65","I-24/I-40","I-24",5)
    sys.add_interstate("I-24/I-40","I-24/I-59","I-24",117)
    sys.add_interstate("I-24/I-59","I-24/I-75","I-24",18)

    # I-25
    sys.add_interstate("I-10/I-25","I-25/I-40","I-25",227)
    sys.add_interstate("I-25/I-40","I-25/I-70","I-25",447)
    sys.add_interstate("I-25/I-70","I-25/I-76","I-25",3)
    sys.add_interstate("I-25/I-76","I-25/I-80","I-25",91)
    sys.add_interstate("I-25/I-80","I-25/I-90","I-25",291)

    # I-26
    sys.add_interstate("I-26/I-81","I-26/I-40","I-26",77)
    sys.add_interstate("I-26/I-40","I-26/I-85","I-26",58)
    sys.add_interstate("I-26/I-85","I-20/I-26","I-26",89)
    sys.add_interstate("I-20/I-26","I-20/I-77","I-26",8)
    sys.add_interstate("I-26/I-77","I-26/I-95","I-26",53)

    # I-27

    # I-29
    sys.add_interstate("I-29/I-35/I-70","I-29/I-35","I-29",5)
    sys.add_interstate("I-29/I-35","I-29/I-80","I-29",173)
    sys.add_interstate("I-29/I-80","I-29/I-90","I-29",186)
    sys.add_interstate("I-29/I-90","I-29/I-94","I-29",232)

    # I-30
    sys.add_interstate("I-20/I-30","I-30/I-35W","I-30",15)
    sys.add_interstate("I-30/I-35W","I-30/I-35E","I-30",30)
    sys.add_interstate("I-30/I-35E","I-30/I-45","I-30",1)
    sys.add_interstate("I-30/I-45","I-30/I-49","I-30",180)
    sys.add_interstate("I-30/I-49","I-30/I-40","I-30",144)

    # I-35
    sys.add_interstate("I-10/I-35","I-35/I-37","I-35",2)
    sys.add_interstate("I-10/I-37","I-14/I-35","I-35",147)
    sys.add_interstate("I-14/I-35","I-35/I-35W/I-35E @ South DFW","I-35",78)
    sys.add_interstate("I-35/I-35W/I-35E @ South DFW","I-20/I-35W","I-35W",45)
    sys.add_interstate("I-35/I-35W/I-35E @ South DFW","I-20/I-35E","I-35E",47)
    sys.add_interstate("I-20/I-35W","I-30/I-35W","I-35W",5)
    sys.add_interstate("I-20/I-35E","I-30/I-35E","I-35E",9)
    sys.add_interstate("I-30/I-35W","I-35/I-35W/I-35E @ North DFW","I-35W",34)
    sys.add_interstate("I-30/I-35E","I-35/I-35W/I-35E @ North DFW","I-35E",38)
    sys.add_interstate("I-35/I-35W/I-35E @ North DFW","I-35/I-40","I-35",163)
    sys.add_interstate("I-35/I-40","I-35/I-44 @ South OKC","I-35",5)
    sys.add_interstate("I-35/I-44 @ South OKC","I-35/I-44 @ North OKC","I-35",5)
    sys.add_interstate("I-35/I-44 @ North OKC","I-35/I-70","I-35",336)
    sys.add_interstate("I-35/I-70","I-29/I-35/I-70","I-35",1)
    sys.add_interstate("I-29/I-35/I-70","I-29/I-35","I-35",4)
    sys.add_interstate("I-29/I-35","I-35/I-80 @ West Des Moines","I-35",178)
    sys.add_interstate("I-35/I-80 @ West Des Moines","I-35/I-80 @ North Des Moines","I-35",14)
    sys.add_interstate("I-35/I-80 @ North Des Moines","I-35/I-90","I-35",145)
    sys.add_interstate("I-35/I-90","I-35/I-35W/I-35E @ South MSP","I-35",75)
    sys.add_interstate("I-35/I-35W/I-35E @ South MSP","I-35W/I-94","I-35W",17)
    sys.add_interstate("I-35/I-35W/I-35E @ South MSP","I-35E/I-94","I-35E",19)
    sys.add_interstate("I-35W/I-94","I-35/I-35W/I-35E @ North MSP","I-35W",25)
    sys.add_interstate("I-35E/I-94","I-35/I-35W/I-35E @ North MSP","I-35E",20)

    # I-37
    sys.add_interstate("I-37/I-69","I-10/I-37","I-37",124)
    sys.add_interstate("I-10/I-37","I-35/I-37","I-37",3)

    # I-39
    sys.add_interstate("I-39/I-55","I-39/I-80","I-39",60)
    sys.add_interstate("I-39/I-80","I-39/I-88","I-39",38)
    sys.add_interstate("I-39/I-88","I-39/I-90","I-39",26)
    sys.add_interstate("I-39/I-90","I-39/I-43/I-90","I-39",19)
    sys.add_interstate("I-39/I-43/I-90","I-39/I-90/I-94 @ Madison","I-39",46)
    sys.add_interstate("I-39/I-90/I-94 @ Madison","I-39/I-90/I-94 @ Portage","I-39",29)

    # I-40
    sys.add_interstate("I-15/I-40","I-17/I-40","I-40",349)
    sys.add_interstate("I-17/I-40","I-25/I-40","I-40",323)
    sys.add_interstate("I-25/I-40","I-27/I-40","I-40",284)
    sys.add_interstate("I-27/I-40","I-40/I-44","I-40",253)
    sys.add_interstate("I-40/I-44","I-35/I-40","I-40",5)
    sys.add_interstate("I-35/I-40","I-40/I-49","I-40",191)
    sys.add_interstate("I-40/I-49","I-30/I-40","I-40",140)
    sys.add_interstate("I-30/I-40","I-40/I-57","I-40",2)
    sys.add_interstate("I-40/I-57","I-40/I-55","I-40",125)
    sys.add_interstate("I-40/I-55","I-40/I-69","I-40",10)
    sys.add_interstate("I-40/I-69","I-40/I-65","I-40",210)
    sys.add_interstate("I-40/I-65","I-24/I-40","I-40",4)
    sys.add_interstate("I-24/I-40","I-40/I-75 @ Farragut","I-40",155)
    sys.add_interstate("I-40/I-75 @ Farragut","I-40/I-75 @ Knoxville","I-40",17)
    sys.add_interstate("I-40/I-75 @ Knoxville","I-40/I-81","I-40",36)
    sys.add_interstate("I-40/I-81","I-26/I-40","I-40",76)
    sys.add_interstate("I-26/I-40","I-40/I-77","I-40",106)
    sys.add_interstate("I-40/I-77","I-40/I-74","I-40",44)
    sys.add_interstate("I-40/I-74","I-40/I-73","I-40",16)
    sys.add_interstate("I-40/I-73","I-40/I-85 @ Greensboro","I-40",14)
    sys.add_interstate("I-40/I-85 @ Greensboro","I-40/I-85 @ Durham","I-40",32)
    sys.add_interstate("I-40/I-85 @ Durham","I-40/I-42","I-40",52)
    sys.add_interstate("I-40/I-42","I-40/I-95","I-40",18)

    # I-41
    sys.add_interstate("I-41/I-94 @ Kenosha","I-41/I-43/I-94","I-41",33)
    sys.add_interstate("I-41/I-43/I-94","I-41/I-43 @ Milwaukee","I-41",5)
    sys.add_interstate("I-41/I-43 @ Milwaukee","I-41/I-94 @ Milwaukee","I-41",4)
    sys.add_interstate("I-41/I-94 @ Milwaukee","I-41/I-43 @ Green Bay","I-41",132)

    # I-43
    sys.add_interstate("I-39/I-43/I-90","I-41/I-43 @ Milwaukee","I-43",60)
    sys.add_interstate("I-41/I-43 @ Milwaukee","I-41/I-43/I-94","I-43",8)
    sys.add_interstate("I-41/I-43/I-94","I-43/I-94","I-43",6)
    sys.add_interstate("I-43/I-94","I-41/I-43 @ Green Bay","I-43",119)

    # I-44
    sys.add_interstate("I-40/I-44","I-35/I-44 @ South OKC","I-44",11)
    sys.add_interstate("I-35/I-44 @ South OKC","I-35/I-44 @ North OKC","I-44",5)
    sys.add_interstate("I-35/I-44 @ North OKC","I-44/I-49 @ Joplin","I-44",209)
    sys.add_interstate("I-44/I-49 @ Joplin","I-44/I-49 @ Carthage","I-44",7)
    sys.add_interstate("I-44/I-49 @ Carthage","I-44/I-55","I-44",271)
    sys.add_interstate("I-44/I-55","I-44/I-55/I-64","I-44",1)
    sys.add_interstate("I-44/I-55/I-64","I-44/I-70","I-44",2)

    # I-45
    sys.add_interstate("I-45/I-69","I-10/I-45","I-45",3)
    sys.add_interstate("I-10/I-45","I-20/I-45","I-45",227)
    sys.add_interstate("I-20/I-45","I-30/I-45","I-45",8)

    # I-49
    sys.add_interstate("I-10/I-49","I-20/I-49","I-49",207)
    # GAP
    sys.add_interstate("I-40/I-49","I-44/I-49 @ Joplin","I-49",126)
    sys.add_interstate("I-44/I-49 @ Joplin","I-44/I-49 @ Carthage","I-49",6)

    # I-55
    sys.add_interstate("I-10/I-55","I-12/I-55","I-55",28)
    sys.add_interstate("I-12/I-55","I-20/I-55","I-55",129)
    sys.add_interstate("I-20/I-55","I-55/I-69 @ Hernando","I-55",189)
    sys.add_interstate("I-55/I-69 @ Hernando","I-55/I-69 @ Memphis","I-55",15)
    sys.add_interstate("I-55/I-69 @ Memphis","I-40/I-55","I-55",13)
    sys.add_interstate("I-40/I-55","I-55/I-57","I-55",131)
    sys.add_interstate("I-55/I-57","I-44/I-55","I-55",142)
    sys.add_interstate("I-44/I-55","I-44/I-55/I-64","I-55",1)
    sys.add_interstate("I-44/I-55/I-64","I-55/I-64/I-70","I-55",3)
    sys.add_interstate("I-55/I-64/I-70","I-55/I-70 @ Edwardsville","I-55",17)
    sys.add_interstate("I-55/I-70 @ Edwardsville","I-55/I-72 @ South Springfield","I-55",73)
    sys.add_interstate("I-55/I-72 @ South Springfield","I-55/I-72 @ East Springfield","I-55",5)
    sys.add_interstate("I-55/I-72 @ East Springfield","I-55/I-74 @ Bloomington","I-55",59)
    sys.add_interstate("I-55/I-74 @ Bloomington","I-55/I-74 @ Normal","I-55",6)
    sys.add_interstate("I-55/I-74 @ Normal","I-39/I-55","I-55",1)
    sys.add_interstate("I-39/I-55","I-55/I-80","I-55",87)
    sys.add_interstate("I-39/I-80","I-55/I-90/I-94","I-55",42)

    # I-57
    # GAP
    sys.add_interstate("I-55/I-57","I-24/I-57","I-57",66)
    sys.add_interstate("I-24/I-57","I-57/I-64 @ South Mt. Vernon","I-57",48)
    sys.add_interstate("I-57/I-64 @ South Mt. Vernon","I-57/I-64 @ North Mt. Vernon","I-57",5)
    sys.add_interstate("I-57/I-64 @ North Mt. Vernon","I-57/I-70 @ South Effingham","I-57",61)
    sys.add_interstate("I-57/I-70 @ South Effingham","I-57/I-70 @ North Effingham","I-57",6)
    sys.add_interstate("I-57/I-70 @ North Effingham","I-57/I-72","I-57",71)
    sys.add_interstate("I-57/I-72","I-57/I-74","I-57",2)
    sys.add_interstate("I-57/I-74","I-57/I-80","I-57",108)
    sys.add_interstate("I-57/I-80","I-57/I-94","I-57",14)

    # I-59
    sys.add_interstate("I-10/I-12/I-59","I-20/I-59 @ Meridian","I-59",159)
    sys.add_interstate("I-20/I-59 @ Meridian","I-20/I-59/I-65","I-59",148)
    sys.add_interstate("I-20/I-59/I-65","I-20/I-59 @ Birmingham","I-59",6)
    sys.add_interstate("I-20/I-59 @ Birmingham","I-24/I-59","I-59",131)

    # I-64
    sys.add_interstate("I-64/I-70 @ Wentzville","I-44/I-55/I-64","I-64",40)
    sys.add_interstate("I-44/I-55/I-64","I-55/I-64/I-70","I-64",3)
    sys.add_interstate("I-55/I-64/I-70","I-57/I-64 @ North Mt. Vernon","I-64",71)
    sys.add_interstate("I-57/I-64 @ North Mt. Vernon","I-57/I-64 @ South Mt. Vernon","I-64",5)
    sys.add_interstate("I-57/I-64 @ South Mt. Vernon","I-64/I-69","I-64",82)
    sys.add_interstate("I-64/I-69","I-64/I-65/I-71","I-64",82)
    sys.add_interstate("I-64/I-65/I-71","I-64/I-75 @ North Lexington","I-64",69)
    sys.add_interstate("I-64/I-75 @ North Lexington","I-64/I-75 @ East Lexington","I-64",7)
    sys.add_interstate("I-64/I-75 @ East Lexington","I-64/I-77 @ Charleston","I-64",168)
    sys.add_interstate("I-64/I-77 @ Charleston","I-64/I-77 @ Beckley","I-64",62)
    sys.add_interstate("I-64/I-77 @ Beckley","I-64/I-81 @ Lexington","I-64",121)
    sys.add_interstate("I-64/I-81 @ Lexington","I-64/I-81 @ Staunton","I-64",30)
    sys.add_interstate("I-64/I-81 @ Staunton","I-64/I-95 @ North Richmond","I-64",99)
    sys.add_interstate("I-64/I-95 @ North Richmond","I-64/I-95 @ Downtown Richmond","I-64",4)

    # I-65
    sys.add_interstate("I-10/I-65","I-65/I-85","I-65",171)
    sys.add_interstate("I-65/I-85","I-20/I-59/I-65","I-65",89)
    sys.add_interstate("I-20/I-59/I-65","I-22/I-65","I-65",4)
    sys.add_interstate("I-22/I-65","I-40/I-65","I-65",186)
    sys.add_interstate("I-40/I-65","I-24/I-65","I-65",4)
    sys.add_interstate("I-24/I-65","I-64/I-65/I-71","I-65",172)
    sys.add_interstate("I-64/I-65/I-71","I-65/I-69/I-74","I-65",107)
    sys.add_interstate("I-65/I-69/I-74","I-65/I-70","I-65",5)
    sys.add_interstate("I-65/I-70","I-65/I-80/I-94","I-65",148)
    sys.add_interstate("I-65/I-80/I-94","I-65/I-90","I-65",1)

    # I-66

    # I-68
    sys.add_interstate("I-68/I-79","I-68/I-70","I-68",112)

    # I-69
    sys.add_interstate("I-2/I-69","I-37/I-69","I-69",125)
    sys.add_interstate("I-37/I-69","I-45/I-69","I-69",202)
    sys.add_interstate("I-45/I-69","I-10/I-69","I-69",2)
    # GAP
    sys.add_interstate("I-55/I-69 @ Hernando","I-55/I-69 @ Memphis","I-69",15)
    sys.add_interstate("I-55/I-69 @ Memphis","I-40/I-69","I-69",6)
    # GAP
    sys.add_interstate("I-24/I-69 @ Calvert City","I-24/I-69 @ Eddyville","I-69",17)
    sys.add_interstate("I-24/I-69 @ Eddyville","I-64/I-69","I-69",112)
    sys.add_interstate("I-64/I-69","I-69/I-74 @ West Indianapolis","I-69",141)
    sys.add_interstate("I-69/I-74 @ West Indianapolis","I-65/I-69/I-74","I-69",5)
    sys.add_interstate("I-65/I-69/I-74","I-69/I-74 @ East Indianapolis","I-69",5)
    sys.add_interstate("I-69/I-74 @ East Indianapolis","I-69/I-70","I-69",5)
    sys.add_interstate("I-69/I-70","I-69/I-80/I-90","I-69",163)
    sys.add_interstate("I-69/I-80/I-90","I-69/I-94 @ Marshall","I-69",40)
    sys.add_interstate("I-69/I-94 @ Marshall","I-69/I-96 @ South Lansing","I-69",35)
    sys.add_interstate("I-69/I-96 @ South Lansing","I-69/I-96 @ North Lansing","I-69",7)
    sys.add_interstate("I-69/I-96 @ North Lansing","I-69/I-75","I-69",53)
    sys.add_interstate("I-69/I-75","I-69/I-94 @ Port Huron","I-69",66)

    # I-70
    sys.add_interstate("I-15/I-70","I-70/I-76 @ Denver","I-70",501)
    sys.add_interstate("I-70/I-76 @ Denver","I-25/I-70","I-70",2)
    sys.add_interstate("I-25/I-70","I-35/I-70","I-70",600)
    sys.add_interstate("I-35/I-70","I-29/I-35/I-70","I-70",2)
    sys.add_interstate("I-29/I-35/I-70","I-64/I-70 @ Wentzville","I-70",210)
    sys.add_interstate("I-64/I-70 @ Wentzville","I-44/I-70","I-70",39)
    sys.add_interstate("I-44/I-70","I-55/I-64/I-70","I-70",3)
    sys.add_interstate("I-55/I-64/I-70","I-55/I-70 @ Edwardsville","I-70",17)
    sys.add_interstate("I-55/I-70 @ Edwardsville","I-57/I-70 @ South Effingham","I-70",77)
    sys.add_interstate("I-57/I-70 @ South Effingham","I-57/I-70 @ North Effingham","I-70",6)
    sys.add_interstate("I-57/I-70 @ North Effingham","I-70/I-74","I-70",130)
    sys.add_interstate("I-70/I-74","I-65/I-70","I-70",9)
    sys.add_interstate("I-65/I-70","I-69/I-70","I-70",7)
    sys.add_interstate("I-69/I-70","I-70/I-75","I-70",101)
    sys.add_interstate("I-70/I-75","I-70/I-71","I-70",66)
    sys.add_interstate("I-70/I-71","I-70/I-77","I-70",80)
    sys.add_interstate("I-70/I-77","I-70/I-79 @ West Washington","I-70",77)
    sys.add_interstate("I-70/I-79 @ West Washington","I-70/I-79 @ East Washington","I-70",4)
    sys.add_interstate("I-70/I-79 @ East Washington","I-70/I-76 @ New Stanton","I-70",37)
    sys.add_interstate("I-70/I-76 @ New Stanton","I-70/I-76/I-99","I-70",71)
    sys.add_interstate("I-70/I-76/I-99","I-70/I-76 @ Breezewood","I-70",19)
    sys.add_interstate("I-70/I-76 @ Breezewood","I-68/I-70","I-70",24)
    sys.add_interstate("I-68/I-70","I-70/I-81","I-70",25)

    # I-71
    sys.add_interstate("I-64/I-65/I-71","I-71/I-75 @ Walton","I-71",78)
    sys.add_interstate("I-71/I-75 @ Walton","I-71/I-75 @ Cincinnati","I-71",19)
    sys.add_interstate("I-71/I-75 @ Cincinnati","I-70/I-71","I-71",107)
    sys.add_interstate("I-70/I-71","I-71/I-76","I-71",103)
    sys.add_interstate("I-71/I-76","I-71/I-80","I-71",24)
    sys.add_interstate("I-71/I-80","I-71/I-90","I-71",15)

    # I-72
    sys.add_interstate("I-55/I-72 @ South Springfield","I-55/I-72 @ East Springfield","I-72",6)
    sys.add_interstate("I-55/I-72 @ East Springfield","I-57/I-72","I-72",79)

    # I-73
    sys.add_interstate("I-73/I-74 @ Rockingham","I-73/I-74 @ Randleman","I-73",58)
    sys.add_interstate("I-73/I-74 @ Randleman","I-73/I-85","I-73",16)
    sys.add_interstate("I-73/I-85","I-40/I-73","I-73",9)

    # I-74
    sys.add_interstate("I-74/I-80 @ Davenport","I-74/I-80 @ Colona","I-74",20)
    sys.add_interstate("I-74/I-80 @ Colona","I-55/I-74 @ Normal","I-74",114)
    sys.add_interstate("I-55/I-74 @ Normal","I-55/I-74 @ Bloomington","I-74",6)
    sys.add_interstate("I-55/I-74 @ Bloomington","I-57/I-74","I-74",45)
    sys.add_interstate("I-57/I-74","I-70/I-74","I-74",121)
    sys.add_interstate("I-70/I-74","I-69/I-74 @ West Indianapolis","I-74",4)
    sys.add_interstate("I-69/I-74 @ West Indianapolis","I-65/I-69/I-74","I-74",5)
    sys.add_interstate("I-65/I-69/I-74","I-69/I-74 @ East Indianapolis","I-74",5)
    sys.add_interstate("I-69/I-74 @ East Indianapolis","I-74/I-75","I-74",97)
    # GAP
    sys.add_interstate("I-40/I-74","I-74/I-85","I-74",20)
    sys.add_interstate("I-74/I-85","I-73/I-74 @ Randleman","I-74",12)
    sys.add_interstate("I-73/I-74 @ Randleman","I-73/I-74 @ Rockingham","I-74",58)
    sys.add_interstate("I-73/I-74 @ Rockingham","I-74/I-95","I-74",60)

    # I-75
    sys.add_interstate("I-4/I-75","I-10/I-75","I-75",174)
    sys.add_interstate("I-10/I-75","I-16/I-75","I-75",201)
    sys.add_interstate("I-16/I-75","I-75/I-85 @ Downtown ATL","I-75",78)
    sys.add_interstate("I-75/I-85 @ Downtown ATL","I-20/I-75/I-85","I-75",3)
    sys.add_interstate("I-20/I-75/I-85","I-75/I-85 @ North ATL","I-75",3)
    sys.add_interstate("I-75/I-85 @ North ATL","I-24/I-75","I-75",107)
    sys.add_interstate("I-24/I-75","I-40/I-75 @ Farragut","I-75",84)
    sys.add_interstate("I-40/I-75 @ Farragut","I-40/I-75 @ Knoxville","I-75",17)
    sys.add_interstate("I-40/I-75 @ Knoxville","I-64/I-75 @ East Lexington","I-75",168)
    sys.add_interstate("I-64/I-75 @ East Lexington","I-64/I-75 @ North Lexington","I-75",7)
    sys.add_interstate("I-64/I-75 @ North Lexington","I-71/I-75 @ Walton","I-75",56)
    sys.add_interstate("I-71/I-75 @ Walton","I-71/I-75 @ Cincinnati","I-75",19)
    sys.add_interstate("I-71/I-75 @ Cincinnati","I-70/I-75","I-75",61)
    sys.add_interstate("I-70/I-75","I-75/I-80/I-90","I-70",133)
    sys.add_interstate("I-75/I-80/I-90","I-75/I-96","I-70",65)
    sys.add_interstate("I-75/I-96","I-75/I-94","I-75",4)
    sys.add_interstate("I-75/I-94","I-69/I-75","I-75",63)

    # I-76
    sys.add_interstate("I-70/I-76 @ Denver","I-25/I-76","I-76",6)
    sys.add_interstate("I-25/I-76","I-76/I-80 @ Big Springs","I-76",182)
    # GAP
    sys.add_interstate("I-71/I-76","I-76/I-77 @ West Akron","I-76",20)
    sys.add_interstate("I-76/I-77 @ West Akron","I-76/I-77 @ Downtown Akron","I-76",4)
    sys.add_interstate("I-76/I-77 @ Downtown Akron","I-76/I-80 @ Youngstown","I-76",38)
    sys.add_interstate("I-76/I-80 @ Youngstown","I-76/I-79","I-76",53)
    sys.add_interstate("I-76/I-79","I-70/I-76 @ New Stanton","I-76",48)
    sys.add_interstate("I-70/I-76 @ New Stanton","I-70/I-76/I-99","I-76",72)
    sys.add_interstate("I-70/I-76/I-99","I-70/I-76 @ Breezewood","I-76",19)
    sys.add_interstate("I-70/I-76 @ Breezewood","I-76/I-81","I-76",68)
    sys.add_interstate("I-76/I-81","I-76/I-83","I-76",16)
    sys.add_interstate("I-76/I-83","I-76/I-95","I-76",108)

    # I-77
    sys.add_interstate("I-26/I-77","I-20/I-77","I-77",16)
    sys.add_interstate("I-20/I-77","I-77/I-85","I-77",89)
    sys.add_interstate("I-77/I-85","I-40/I-77","I-77",40)
    sys.add_interstate("I-40/I-77","I-77/I-81 @ Fort Chiswell","I-77",87)
    sys.add_interstate("I-77/I-81 @ Fort Chiswell","I-77/I-81 @ Wytheville","I-77",9)
    sys.add_interstate("I-77/I-81 @ Wytheville","I-64/I-77 @ Beckley","I-77",66)
    sys.add_interstate("I-64/I-77 @ Beckley","I-64/I-77 @ Charleston","I-77",62)
    sys.add_interstate("I-64/I-77 @ Charleston","I-77/I-79","I-77",2)
    sys.add_interstate("I-77/I-79","I-70/I-77","I-77",129)
    sys.add_interstate("I-70/I-77","I-76/I-77 @ Downtown Akron","I-77",82)
    sys.add_interstate("I-76/I-77 @ Downtown Akron","I-76/I-77 @ West Akron","I-77",4)
    sys.add_interstate("I-76/I-77 @ West Akron","I-77/I-80","I-77",19)
    sys.add_interstate("I-77/I-80","I-77/I-90","I-77",17)

    # I-78
    sys.add_interstate("I-78/I-81","I-78/I-95","I-78",136)

    # I-79
    sys.add_interstate("I-77/I-79","I-68/I-79","I-79",148)
    sys.add_interstate("I-68/I-79","I-70/I-79 @ East Washington","I-79",45)
    sys.add_interstate("I-70/I-79 @ East Washington","I-70/I-79 @ West Washington","I-79",3)
    sys.add_interstate("I-70/I-79 @ West Washington","I-76/I-79","I-79",40)
    sys.add_interstate("I-76/I-79","I-79/I-80","I-79",39)
    sys.add_interstate("I-79/I-80","I-79/I-90","I-79",61)

    # I-80
    sys.add_interstate("I-5/I-80","I-15/I-80","I-80",647)
    sys.add_interstate("I-15/I-80","I-80/I-84","I-80",46)
    sys.add_interstate("I-80/I-84","I-25/I-80","I-80",388)
    sys.add_interstate("I-25/I-80","I-76/I-80 @ Big Springs","I-80",145)
    sys.add_interstate("I-76/I-80 @ Big Springs","I-29/I-80","I-80",354)
    sys.add_interstate("I-29/I-80","I-35/I-80 @ West Des Moines","I-80",121)
    sys.add_interstate("I-35/I-80 @ West Des Moines","I-35/I-80 @ North Des Moines","I-35",14)
    sys.add_interstate("I-35/I-80 @ North Des Moines","I-74/I-80 @ Davenport","I-80",160)
    sys.add_interstate("I-74/I-80 @ Davenport","I-80/I-88","I-80",12)
    sys.add_interstate("I-80/I-88","I-74/I-80 @ Colona","I-80",7)
    sys.add_interstate("I-74/I-80 @ Colona","I-39/I-80","I-80",68)
    sys.add_interstate("I-39/I-80","I-55/I-80","I-80",48)
    sys.add_interstate("I-55/I-80","I-57/I-80","I-80",26)
    sys.add_interstate("I-57/I-80","I-80/I-94","I-80",9)
    sys.add_interstate("I-80/I-94","I-65/I-80/I-94","I-80",15)
    sys.add_interstate("I-65/I-80/I-94","I-80/I-90/I-94","I-80",4)
    sys.add_interstate("I-80/I-90/I-94","I-69/I-80/I-90","I-80",123)
    sys.add_interstate("I-69/I-80/I-90","I-75/I-80/I-90","I-80",78)
    sys.add_interstate("I-75/I-80/I-90","I-80/I-90","I-80",79)
    sys.add_interstate("I-80/I-90","I-71/I-80","I-80",20)
    sys.add_interstate("I-71/I-80","I-77/I-80","I-80",12)
    sys.add_interstate("I-77/I-80","I-76/I-80 @ Youngstown","I-80",48)
    sys.add_interstate("I-76/I-80 @ Youngstown","I-79/I-80","I-80",39)
    sys.add_interstate("I-79/I-80","I-80/I-99","I-80",141)
    sys.add_interstate("I-80/I-99","I-80/I-81","I-80",99)
    sys.add_interstate("I-80/I-81","I-80/I-95","I-80",120)

    # I-81
    sys.add_interstate("I-40/I-81","I-26/I-81","I-81",57)
    sys.add_interstate("I-26/I-81","I-77/I-81 @ Wytheville","I-81",92)
    sys.add_interstate("I-77/I-81 @ Wytheville","I-77/I-81 @ Fort Chiswell","I-81",9)
    sys.add_interstate("I-77/I-81 @ Fort Chiswell","I-64/I-81 @ Lexington","I-81",110)
    sys.add_interstate("I-64/I-81 @ Lexington","I-64/I-81 @ Staunton","I-81",30)
    sys.add_interstate("I-64/I-81 @ Staunton","I-66/I-81","I-81",79)
    sys.add_interstate("I-66/I-81","I-70/I-81","I-81",54)
    sys.add_interstate("I-70/I-81","I-76/I-81","I-81",61)
    sys.add_interstate("I-76/I-81","I-81/I-83","I-81",19)
    sys.add_interstate("I-81/I-83","I-78/I-81","I-81",19)
    sys.add_interstate("I-78/I-81","I-80/I-81","I-81",62)
    sys.add_interstate("I-80/I-81","I-81/I-84","I-81",36)
    sys.add_interstate("I-81/I-84","I-81/I-86 @ East Binghamton","I-81",54)
    sys.add_interstate("I-81/I-86 @ East Binghamton","I-81/I-86 @ Downtown Binghamton","I-81",6)
    sys.add_interstate("I-81/I-86 @ Downtown Binghamton","I-81/I-88","I-81",2)
    sys.add_interstate("I-81/I-88","I-81/I-90","I-81",74)

    # I-82
    sys.add_interstate("I-82/I-84","I-82/I-90","I-82",143)

    # I-83
    sys.add_interstate("I-76/I-83","I-81/I-83","I-83",11)

    # I-84
    sys.add_interstate("I-5/I-84","I-82/I-84","I-84",177)
    sys.add_interstate("I-82/I-84","I-84/I-86 @ Declo","I-84",420)
    sys.add_interstate("I-84/I-86 @ Declo","I-15/I-84 @ Tremonton","I-84",96)
    sys.add_interstate("I-15/I-84 @ Tremonton","I-15/I-84 @ Ogden","I-84",39)
    sys.add_interstate("I-15/I-84 @ Ogden","I-80/I-84","I-84",39)
    # GAP
    sys.add_interstate("I-81/I-84","I-84/I-86 @ Middletown","I-84",73)
    sys.add_interstate("I-84/I-86 @ Middletown","I-84/I-87","I-84",18)
    sys.add_interstate("I-84/I-87","I-84/I-91","I-84",98)
    sys.add_interstate("I-84/I-91","I-84/I-90","I-84",44)

    # I-85
    sys.add_interstate("I-65/I-85","I-75/I-85 @ Downtown ATL","I-85",158)
    sys.add_interstate("I-75/I-85 @ Downtown ATL","I-20/I-75/I-85","I-85",3)
    sys.add_interstate("I-20/I-75/I-85","I-75/I-85 @ North ATL","I-85",3)
    sys.add_interstate("I-75/I-85 @ North ATL","I-26/I-85","I-85",166)
    sys.add_interstate("I-26/I-85","I-77/I-85","I-85",74)
    sys.add_interstate("I-77/I-85","I-74/I-85","I-85",75)
    sys.add_interstate("I-74/I-85","I-73/I-85","I-85",7)
    sys.add_interstate("I-73/I-85","I-40/I-85 @ Greensboro","I-85",11)
    sys.add_interstate("I-40/I-85 @ Greensboro","I-40/I-85 @ Durham","I-85",31)
    sys.add_interstate("I-40/I-85 @ Durham","I-85/I-95","I-85",140)

    # I-86
    sys.add_interstate("I-84/I-86 @ Declo","I-15/I-86","I-86",63)
    # GAP
    sys.add_interstate("I-86/I-90","I-86/I-99","I-86",176)
    sys.add_interstate("I-86/I-99","I-81/I-86 @ Downtown Binghamton","I-86",77)
    sys.add_interstate("I-81/I-86 @ Downtown Binghamton","I-81/I-86 @ East Binghamton","I-86",6)
    sys.add_interstate("I-81/I-86 @ East Binghamton","I-84/I-86 @ Middletown","I-86",113)
    sys.add_interstate("I-84/I-86 @ Middletown","I-86/I-87","I-86",18)

    # I-87
    sys.add_interstate("I-87/I-95","I-86/I-87","I-87",51)
    sys.add_interstate("I-86/I-87","I-84/I-87","I-87",15)
    sys.add_interstate("I-84/I-87","I-87/I-90","I-87",88)

    # I-88
    sys.add_interstate("I-80/I-88","I-39/I-88","I-88",79)
    # GAP
    sys.add_interstate("I-81/I-88","I-88/I-90","I-88",118)

    # I-89
    sys.add_interstate("I-89/I-93","I-89/I-91","I-89",62)

    # I-90
    sys.add_interstate("I-5/I-90","I-82/I-90","I-90",108)
    sys.add_interstate("I-82/I-90","I-15/I-90","I-90",478)
    sys.add_interstate("I-15/I-90","I-90/I-94 @ Billings","I-90",237)
    sys.add_interstate("I-90/I-94 @ Billings","I-25/I-90","I-90",156)
    sys.add_interstate("I-25/I-90","I-29/I-90","I-90",546)
    sys.add_interstate("I-29/I-90","I-35/I-90","I-90",177)
    sys.add_interstate("I-35/I-90","I-90/I-94 @ Tomah","I-90",164)
    sys.add_interstate("I-90/I-94 @ Tomah","I-39/I-90/I-94 @ Portage","I-90",63)
    sys.add_interstate("I-39/I-90/I-94 @ Portage","I-39/I-90/I-94 @ Madison","I-90",30)
    sys.add_interstate("I-39/I-90/I-94 @ Madison","I-39/I-43/I-90","I-90",47)
    sys.add_interstate("I-39/I-43/I-90","I-39/I-90","I-90",21)
    sys.add_interstate("I-39/I-90","I-90/I-94 @ North Chicago","I-90",67)
    sys.add_interstate("I-90/I-94 @ North Chicago","I-55/I-90/I-94","I-90",11)
    sys.add_interstate("I-55/I-90/I-94","I-90/I-94 @ South Chicago","I-90",6)
    sys.add_interstate("I-90/I-94 @ South Chicago","I-65/I-90","I-90",25)
    sys.add_interstate("I-65/I-90","I-80/I-90/I-94","I-90",5)
    sys.add_interstate("I-80/I-90/I-94","I-69/I-80/I-90","I-90",123)
    sys.add_interstate("I-69/I-80/I-90","I-75/I-80/I-90","I-90",78)
    sys.add_interstate("I-75/I-80/I-90","I-80/I-90","I-90",79)
    sys.add_interstate("I-80/I-90","I-71/I-90","I-90",29)
    sys.add_interstate("I-71/I-90","I-77/I-90","I-90",2)
    sys.add_interstate("I-77/I-90","I-79/I-90","I-90",93)
    sys.add_interstate("I-79/I-90","I-86/I-90","I-90",15)
    sys.add_interstate("I-86/I-90","I-81/I-90","I-90",223)
    sys.add_interstate("I-81/I-90","I-88/I-90","I-90",124)
    sys.add_interstate("I-88/I-90","I-87/I-90","I-90",11)
    sys.add_interstate("I-87/I-90","I-90/I-91","I-90",85)
    sys.add_interstate("I-90/I-91","I-84/I-90","I-90",33)
    sys.add_interstate("I-84/I-90","I-90/I-95","I-90",45)
    sys.add_interstate("I-90/I-95","I-90/I-93","I-90",12)

    # I-91
    sys.add_interstate("I-91/I-95","I-84/I-91","I-91",39)
    sys.add_interstate("I-84/I-91","I-90/I-91","I-91",32)
    sys.add_interstate("I-90/I-91","I-89/I-91","I-91",114)
    sys.add_interstate("I-89/I-91","I-91/I-93","I-91",59)

    # I-93
    sys.add_interstate("I-93/I-95 @ Canton","I-90/I-93","I-93",16)
    sys.add_interstate("I-90/I-93","I-93/I-95 @ Reading","I-93",12)
    sys.add_interstate("I-93/I-95 @ Reading","I-89/I-93","I-93",53)
    sys.add_interstate("I-89/I-93","I-91/I-93","I-93",108)

    # I-94
    sys.add_interstate("I-90/I-94 @ Billings","I-29/I-94","I-94",597)
    sys.add_interstate("I-29/I-94","I-35W/I-94","I-94",237)
    sys.add_interstate("I-35W/I-94","I-35E/I-94","I-94",8)
    sys.add_interstate("I-35E/I-94","I-90/I-94 @ Tomah","I-94",163)
    sys.add_interstate("I-90/I-94 @ Tomah","I-39/I-90/I-94 @ Portage","I-94",63)
    sys.add_interstate("I-39/I-90/I-94 @ Portage","I-39/I-90/I-94 @ Madison","I-94",30)
    sys.add_interstate("I-39/I-90/I-94 @ Madison","I-41/I-94 @ Milwaukee","I-94",65)
    sys.add_interstate("I-41/I-94 @ Milwaukee","I-43/I-94","I-94",6)
    sys.add_interstate("I-43/I-94","I-41/I-43/I-94","I-94",6)
    sys.add_interstate("I-41/I-43/I-94","I-41/I-94 @ Kenosha","I-94",32)
    sys.add_interstate("I-41/I-94 @ Kenosha","I-90/I-94 @ North Chicago","I-94",44)
    sys.add_interstate("I-90/I-94 @ North Chicago","I-55/I-90/I-94","I-94",10)
    sys.add_interstate("I-55/I-90/I-94","I-90/I-94 @ South Chicago","I-94",5)
    sys.add_interstate("I-90/I-94 @ South Chicago","I-57/I-94","I-94",4)
    sys.add_interstate("I-57/I-94","I-80/I-94","I-94",12)
    sys.add_interstate("I-80/I-94","I-65/I-80/I-94","I-94",13)
    sys.add_interstate("I-65/I-80/I-94","I-80/I-90/I-94","I-94",5)
    sys.add_interstate("I-80/I-90/I-94","I-69/I-94 @ Marshall","I-94",139)
    sys.add_interstate("I-69/I-94 @ Marshall","I-94/I-96","I-94",105)
    sys.add_interstate("I-94/I-96","I-75/I-94","I-94",3)
    sys.add_interstate("I-75/I-94","I-69/I-94 @ Port Huron","I-94",56)

    # I-95
    sys.add_interstate("I-4/I-95","I-10/I-95","I-95",91)
    sys.add_interstate("I-10/I-95","I-16/I-95","I-95",129)
    sys.add_interstate("I-16/I-95","I-26/I-95","I-95",99)
    sys.add_interstate("I-26/I-95","I-20/I-95","I-95",75)
    sys.add_interstate("I-20/I-95","I-74/I-95","I-95",51)
    sys.add_interstate("I-74/I-95","I-40/I-95","I-95",68)
    sys.add_interstate("I-40/I-95","I-85/I-95","I-95",151)
    sys.add_interstate("I-85/I-95","I-64/I-95 @ Downtown Richmond","I-95",24)
    sys.add_interstate("I-64/I-95 @ Downtown Richmond","I-64/I-95 @ North Richmond","I-95",4)
    sys.add_interstate("I-64/I-95 @ North Richmond","I-76/I-95","I-95",249)
    sys.add_interstate("I-76/I-95","I-78/I-95","I-95",84)
    sys.add_interstate("I-78/I-95","I-80/I-95","I-95",14)
    sys.add_interstate("I-80/I-95","I-87/I-95","I-95",6)
    sys.add_interstate("I-87/I-95","I-91/I-95","I-95",70)
    sys.add_interstate("I-91/I-95","I-93/I-95 @ Canton","I-95",133)
    sys.add_interstate("I-93/I-95 @ Canton","I-90/I-95","I-95",12)
    sys.add_interstate("I-90/I-95","I-93/I-95 @ Reading","I-95",17)

    # I-96
    sys.add_interstate("I-69/I-96 @ North Lansing","I-69/I-96 @ South Lansing","I-96",7)
    sys.add_interstate("I-69/I-96 @ South Lansing","I-94/I-96","I-94",94)
    sys.add_interstate("I-94/I-96","I-75/I-96","I-96",2)

    # I-97

    # I-99
    sys.add_interstate("I-70/I-76/I-99","I-80/I-99","I-99",87)