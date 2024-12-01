import re
import xml.etree.ElementTree as ET
def create_array_of_interfaces(file_name):
    array_of_interfaces = []
    f = open(file_name, "r")
    text = f.read().split("\n \n")
    for i in range(len(text)):
        eth33 = interface()
        eth33.define_everything(text[i])
        array_of_interfaces.append(eth33)
    return array_of_interfaces    

def serial_to_xml_for_all_interfaces(array_of_interfaces):
    for inter in array_of_interfaces:
        inter.serial_to_xml()

class interface():
    Id = -1
    Name = ""
    Description = None # не всегда есть описание
    MacAddress = ""
    Status = ""
    def __init__(self, Id, Name, Description, MacAddress, Status):
        self.Id = Id
        self.Name = Name
        self.Description = Description
        self.MacAddress = MacAddress
        self.Status = Status
    def __init__(self):
        pass
    def define_Id(self, str_for_parsing):
        IdRegex = re.compile(r'name="([^"]*)"')
        mo = IdRegex.search(str_for_parsing)
        self.Id = mo.group(1)
        return self.Id
    def define_Name(self, str_for_parsing):
        NameRegex = re.compile(r'default-name="([^"]*)"')
        mo = NameRegex.search(str_for_parsing)
        self.Name = mo.group(1)
        return self.Name
    def define_Description(self, str_for_parsing):
        DescriptionRegex = re.compile(r';;; ([^\n]*?)\r?\n')
        mo = DescriptionRegex.search(str_for_parsing)
        if mo is not None:
            self.Description = mo.group(1)
        return self.Description
    def define_MacAddress(self, str_for_parsing):
        MacAddressRegex = re.compile(r'mac-address=([0-9a-f:]+)')
        mo = MacAddressRegex.search(str_for_parsing)
        self.MacAddress = mo.group(1)
        return self.MacAddress
    def define_Status(self, str_for_parsing):
        StatusRegex = re.compile(r'\d+ ([RSX]{1,3}) ')
        mo = StatusRegex.search(str_for_parsing)
        self.Status = "down"
        if mo.group(1).find("R") != -1:
            self.Status = "up"
        return self.Status
    def define_everything(self, str_for_parsing):
        self.Id =  self.define_Id(str_for_parsing)
        self.Name = self.define_Name(str_for_parsing)
        self.Description = self.define_Description(str_for_parsing)
        self.MacAddress = self.define_MacAddress(str_for_parsing)
        self.Status = self.define_Status(str_for_parsing)
    def print_everything(self):
        print(f"Id: {self.Id}")
        print(f"Name: {self.Name}")
        print(f"Description: {self.Description}")
        print(f"MacAddress: {self.MacAddress}")
        print(f"Status: {self.Status}")
    def serial_to_xml(self):
        root = ET.Element("interface")
        ET.SubElement(root, "Id").text = self.Id
        ET.SubElement(root, "Name").text = self.Name
        ET.SubElement(root, "Description").text = self.Description
        ET.SubElement(root, "MacAddress").text = self.MacAddress
        ET.SubElement(root, "Status").text = self.Status
        tree = ET.ElementTree(root)
        tree.write(f"{self.Id}.xml", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    file_name = "network_device_output.txt"
    array_of_interfaces = create_array_of_interfaces(file_name)
    serial_to_xml_for_all_interfaces(array_of_interfaces)

    