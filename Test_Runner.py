import sys
import pytest
sys.path.append('Test_Case')
sys.path.append('Utils')
from Utils.Log import Log


if __name__ == '__main__':
    # Main Program
    debug_mode = False  #  Debug模式開關
    case_path = './Test_Case/Test_API_System.py'  # Test Case 路徑
    
    #  判斷是否開啟Debug模式
    if debug_mode:
        Log.set_Level = "DEBUG"
    else:
        Log.set_Level = "ERROR"

    pytest.main(['-v','-s','--disable-warnings',
                #   '-k test_No3',
                case_path])  # run test case
    
