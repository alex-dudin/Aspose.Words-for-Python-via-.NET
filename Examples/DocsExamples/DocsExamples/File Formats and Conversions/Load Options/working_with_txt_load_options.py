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

class WorkingWithTxtLoadOptions(docs_base.DocsExamplesBase):

    def test_detect_numbering_with_whitespaces(self):

        #ExStart:DetectNumberingWithWhitespaces
        # Create a plaintext document in the form of a string with parts that may be interpreted as lists.
        # Upon loading, the first three lists will always be detected by Aspose.words,
        # and List objects will be created for them after loading.
        text_doc = """Full stop delimiters:\n
                    1. First list item 1\n
                    2. First list item 2\n
                    3. First list item 3\n\n
                    Right bracket delimiters:\n
                    1) Second list item 1\n
                    2) Second list item 2\n
                    3) Second list item 3\n\n
                    Bullet delimiters:\n
                    • Third list item 1\n
                    • Third list item 2\n
                    • Third list item 3\n\n
                    Whitespace delimiters:\n
                    1 Fourth list item 1\n
                    2 Fourth list item 2\n
                    3 Fourth list item 3"""

        # The fourth list, with whitespace inbetween the list number and list item contents,
        # will only be detected as a list if "DetectNumberingWithWhitespaces" in a LoadOptions object is set to true,
        # to avoid paragraphs that start with numbers being mistakenly detected as lists.
        load_options = aw.loading.TxtLoadOptions()
        load_options.detect_numbering_with_whitespaces = True

        # Load the document while applying LoadOptions as a parameter and verify the result.
        doc = aw.Document(io.BytesIO(text_doc.encode("utf-8")), load_options)

        doc.save(docs_base.artifacts_dir + "WorkingWithTxtLoadOptions.detect_numbering_with_whitespaces.docx")
        #ExEnd:DetectNumberingWithWhitespaces


    def test_handle_spaces_options(self):

        #ExStart:HandleSpacesOptions
        text_doc = "      Line 1 \n" + "    Line 2   \n" +  " Line 3       "

        load_options = aw.loading.TxtLoadOptions()
        load_options.leading_spaces_options = aw.loading.TxtLeadingSpacesOptions.TRIM
        load_options.trailing_spaces_options = aw.loading.TxtTrailingSpacesOptions.TRIM

        stream = io.BytesIO(text_doc.encode("utf-8"))

        doc = aw.Document(stream, load_options)

        doc.save(docs_base.artifacts_dir + "WorkingWithTxtLoadOptions.handle_spaces_options.docx")
        #ExEnd:HandleSpacesOptions


    def test_document_text_direction(self):

        #ExStart:DocumentTextDirection
        load_options = aw.loading.TxtLoadOptions()
        load_options.document_direction = aw.loading.DocumentDirection.AUTO

        doc = aw.Document(docs_base.my_dir + "Hebrew text.txt", load_options)

        paragraph = doc.first_section.body.first_paragraph
        print(paragraph.paragraph_format.bidi)

        doc.save(docs_base.artifacts_dir + "WorkingWithTxtLoadOptions.document_text_direction.docx")
        #ExEnd:DocumentTextDirection


if __name__ == '__main__':
    unittest.main()
