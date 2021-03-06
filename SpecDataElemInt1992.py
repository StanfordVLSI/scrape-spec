from SpecDataElem1992 import *

class SpecDataElemInt1992(SpecDataElem1992):
    "A class that holds spec int data for a given processor"

    def __init__(self):
        tests = ["008.espresso",
                 "022.li",
                 "023.eqntott",
                 "026.compress",
                 "072.sc",
                 "085.gcc"]

        self.__tests = tests

        attrMap = {"SPECint92" : "peakmean",
                   "SPECbase_int92" : "basemean"}
        #attrMap = {"099 Base": "099_go",
        #           "124 Base": "124_m88ksim",
        #           "126 Base": "126_gcc",
        #           "129 Base": "129_compress",
        #           "130 Base": "130_li",
        #           "132 Base": "132_ijpeg",
        #           "134 Base": "134_perl",
        #           "147 Base": "147_vortex"}

        SpecDataElem1992.__init__(self, tests=tests, attrMap=attrMap)

    def tests(self):
        return self.__tests


    
