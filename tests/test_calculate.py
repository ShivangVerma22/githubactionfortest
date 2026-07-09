from src.Calculate import add,sub,mul,div


#now making function for testing and usinf assert keyword for output varify
def test_add():
    assert add(5,6)==11
    assert add(-1,-1)==-2
    assert add(7,9)==16

def test_sub():
    assert sub(5,6)==-1
    assert sub(-1,-1)==0
    assert sub(9,7)==2

def test_mul():
    assert mul(5,6)==30
    assert mul(-1,-1)==1
    assert mul(-7,9)==-63

def test_div():
    assert div(6,6)==1
    assert div(-1,1)==-1
    assert div(14,7)==2

def test_mod():
    assert div(6,6)==0
    assert div(1,1)==0
    assert div(14,7)==0
    
    
    