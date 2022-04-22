from etlapp import __version__
import etlapp

from etlapp import transform
def test_read():
    s="shubham kumar"
    c=""
    with open("testfile.txt") as file:
        for line in file:
            l = line.split(' ')
            for word in l:
                c+=word
                c+=" "
    assert s==c.strip()
    
def test1_transform():
    t="shubham kumar"
    s="SHUBHAM KUMAR"
    assert transform.transform1(t)==s
    
def test2_transform():
    dic = {"kumar":1,"shubham":1}
    t="shubham kumar"
    assert transform.transform2(t)==dic

def test_write():
    dic = {"kumar":1,"shubham":1}
    s="SHUBHAM KUMAR"
    with open("testout.txt") as file:
        for line in file:
            assert (line==dic or line==s)

    
        
if __name__ == "__main__":
    test_read()
    print("read passed")
    test1_transform()
    print("first part transform test passed")
    test2_transform()
    print("second part transform test passed")
    test_write()
    print("second write test passed")
    print("every test passed")
