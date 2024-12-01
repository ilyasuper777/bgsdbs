import re
import xml.etree.ElementTree as ET
import pytest 
from task1 import interface, create_array_of_interfaces

file_name = "network_device_output.txt"
f = open(file_name, "r")
text = f.read().split("\n \n")

def test_1_define_Id():
    eth33 = interface()
    assert eth33.define_Id(text[0]) == "LAN" 

def test_2_define_Id():
    eth33 = interface()
    assert eth33.define_Id(text[1]) == "ether1" 

def test_3_define_Id():
    eth33 = interface()
    assert eth33.define_Id(text[2]) == "ether3"

def test_4_define_Id():
    eth33 = interface()
    assert eth33.define_Id(text[3]) == "ether4"

def test_1_define_Name():
    eth33 = interface()
    assert eth33.define_Name(text[0]) == "ether2" 

def test_2_define_Name():
    eth33 = interface()
    assert eth33.define_Name(text[1]) == "ether1" 

def test_3_define_Name():
    eth33 = interface()
    assert eth33.define_Name(text[2]) == "ether3"

def test_4_define_Name():
    eth33 = interface()
    assert eth33.define_Name(text[3]) == "ether4"

def test_1_define_Description():
    eth33 = interface()
    assert eth33.define_Description(text[0]) == "LAN" 

def test_2_define_Description():
    eth33 = interface()
    assert eth33.define_Description(text[1]) == None 

def test_3_define_Description():
    eth33 = interface()
    assert eth33.define_Description(text[2]) == None

def test_4_define_Descriptione():
    eth33 = interface()
    assert eth33.define_Description(text[3]) == "bla bla description for the ether4 interface"

def test_1_define_MacAddress():
    eth33 = interface()
    assert eth33.define_MacAddress(text[0]) == "50:00:00:31:00:01" 

def test_2_define_MacAddressn():
    eth33 = interface()
    assert eth33.define_MacAddress(text[1]) == "50:00:00:31:00:00"

def test_3_define_MacAddress():
    eth33 = interface()
    assert eth33.define_MacAddress(text[2]) == "50:00:00:31:00:02"
def test_4_define_MacAddress():
    eth33 = interface()
    assert eth33.define_MacAddress(text[3]) == "50:00:00:31:00:03"

def test_1_define_Status():
    eth33 = interface()
    assert eth33.define_Status(text[0]) == "up" 

def test_2_define_Status():
    eth33 = interface()
    assert eth33.define_Status(text[1]) == "up" 

def test_3_define_Status():
    eth33 = interface()
    assert eth33.define_Status(text[2]) == "up"
def test_4_define_Status():
    eth33 = interface()
    assert eth33.define_Status(text[3]) == "down"