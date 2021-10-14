import unittest
import os
import sys
import io

base_dir = os.path.abspath(os.curdir) + "/"
base_dir = base_dir[:base_dir.find("Aspose.Words-for-Python-via-.NET")]
base_dir = base_dir + "Aspose.Words-for-Python-via-.NET/Examples/DocsExamples/DocsExamples"
sys.path.insert(0, base_dir)

import docs_examples_base as docs_base

import aspose.words as aw

class WorkingWithLicense(docs_base.DocsExamplesBase):
    
    def test_apply_license_from_file(self) :
        
        #ExStart:ApplyLicenseFromFile
        lic = aw.License()

        # Try to set license from the folder with the python script.
        try :
            lic.set_license("Aspose.Words.Python.NET.lic")
            print("License set successfully.")
        except RuntimeError as err :
            # We do not ship any license with this example, visit the Aspose site to obtain either a temporary or permanent license. 
            print("\nThere was an error setting the license: {0}".format(err))
        #ExEnd:ApplyLicenseFromFile
        
    def test_apply_license_from_stream(self) :
        
        #ExStart:ApplyLicenseFromStream
        lic = aw.License()

        # Try to set license from the stream.
        try :
            lic_stream = io.FileIO("C:\\Temp\\Aspose.Words.Python.NET.lic")
            lic.set_license(lic_stream)
            lic_stream.close()
            print("License set successfully.")
        except RuntimeError as err :
            # We do not ship any license with this example, visit the Aspose site to obtain either a temporary or permanent license. 
            print("\nThere was an error setting the license: {0}".format(err))
        #ExEnd:ApplyLicenseFromStream

    def test_apply_metered_license(self) :
        
        #ExStart:ApplyMeteredLicense
        # set metered public and private keys
        metered = aw.Metered()
        # Access the setMeteredKey property and pass public and private keys as parameters
        metered.set_metered_key("*****", "*****")

        # Load the document from disk.
        doc = aw.Document(docs_base.my_dir + "Document.docx")
        #Get the page count of document
        print(doc.page_count)
        #ExEnd:ApplyMeteredLicense


if __name__ == '__main__':
    unittest.main()