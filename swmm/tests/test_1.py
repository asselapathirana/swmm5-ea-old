from swmm5.swmm5tools import SWMM5Simulation, SWMM5Error
import unittest

class testSWMM5(unittest.TestCase):
    
    
    def test_running_with_nonsensical_swmm_input_file(self):
        """ should raise a SWMM5Error exception"""
        self.assertRaises(SWMM5Error,SWMM5Simulation,"foo-bar-bat-box.inp")
        try:
            with SWMM5Simulation("foo-bar-bat-box.inp") as st:
                pass
        except SWMM5Error as e:
            pass
        self.assertEqual(str(e),'66: \n  ERROR 303: cannot open input file.')
        
    def test_running_with_good_input_file(self):
        """should not raise exceptoins"""
        with SWMM5Simulation("swmm5/examples/simple/swmm5Example.inp") as st:
            pass

    def test_GetSwmmResult_for_runoff_should_return_correct_runoff(self):
        with SWMM5Simulation("swmm5/examples/simple/swmm5Example.inp") as st:
            pass
        
    def test_SWMM5Simulation_should_have_attributes(self):
        with SWMM5Simulation("swmm5/examples/simple/swmm5Example.inp") as st:
            st.SWMM_Nperiods
        
if __name__=="__main__":
    unittest.main()