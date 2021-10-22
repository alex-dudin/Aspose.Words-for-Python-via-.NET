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

class WorkingWithHtmlLoadOptions(docs_base.DocsExamplesBase):

    def test_preferred_control_type(self) :

        #ExStart:LoadHtmlElementsWithPreferredControlType
        html = """
            <html>
                <select name='ComboBox' size='1'>
                    <option value='val1'>item1</option>
                    <option value='val2'></option>
                </select>
            </html>
        """

        load_options = aw.loading.HtmlLoadOptions()
        load_options.preferred_control_type = aw.loading.HtmlControlType.STRUCTURED_DOCUMENT_TAG

        doc = aw.Document(io.BytesIO(html.encode("utf-8")), load_options)

        doc.save(docs_base.artifacts_dir + "WorkingWithHtmlLoadOptions.preferred_control_type.docx", aw.SaveFormat.DOCX)
        #ExEnd:LoadHtmlElementsWithPreferredControlType


if __name__ == '__main__':
    unittest.main()
