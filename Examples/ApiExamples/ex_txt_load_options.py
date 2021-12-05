import unittest
import io
import textwrap

import aspose.words as aw
import aspose.pydrawing as drawing

from api_example_base import ApiExampleBase, my_dir, artifacts_dir

MY_DIR = my_dir
ARTIFACTS_DIR = artifacts_dir

class ExTxtLoadOptions(ApiExampleBase):

    def test_detect_numbering_with_whitespaces(self):
    
        for detect_numbering_with_whitespaces in (False, True):
            with self.subTest(detect_numbering_with_whitespaces=detect_numbering_with_whitespaces):
                #ExStart
                #ExFor:TxtLoadOptions.DetectNumberingWithWhitespaces
                #ExSummary:Shows how to detect lists when loading plaintext documents.
                # Create a plaintext document in a string with four separate parts that we may interpret as lists,
                # with different delimiters. Upon loading the plaintext document into a "Document" object,
                # Aspose.Words will always detect the first three lists and will add a "List" object
                # for each to the document's "lists" property.
                text_doc = textwrap.dedent("""
                Full stop delimiters:
                1. First list item 1
                2. First list item 2
                3. First list item 3

                Right bracket delimiters:
                1) Second list item 1
                2) Second list item 2
                3) Second list item 3

                Bullet delimiters:
                • Third list item 1
                • Third list item 2
                • Third list item 3

                Whitespace delimiters:
                1 Fourth list item 1
                2 Fourth list item 2
                3 Fourth list item 3""").lstrip()

                # Create a "TxtLoadOptions" object, which we can pass to a document's constructor
                # to modify how we load a plaintext document.
                load_options = aw.loading.TxtLoadOptions()

                # Set the "detect_numbering_with_whitespaces" property to "True" to detect numbered items
                # with whitespace delimiters, such as the fourth list in our document, as lists.
                # This may also falsely detect paragraphs that begin with numbers as lists.
                # Set the "detect_numbering_with_whitespaces" property to "False"
                # to not create lists from numbered items with whitespace delimiters.
                load_options.detect_numbering_with_whitespaces = detect_numbering_with_whitespaces

                doc = aw.Document(io.BytesIO(text_doc.encode("utf-8")), load_options)

                if detect_numbering_with_whitespaces:
                    self.assertEqual(4, doc.lists.count)
                    self.assertTrue(any("Fourth list" in p.get_text() and p.as_paragraph().is_list_item
                                        for p in doc.first_section.body.paragraphs))
                else:
                    self.assertEqual(3, doc.lists.count)
                    self.assertFalse(any("Fourth list" in p.get_text() and p.as_paragraph().is_list_item
                                         for p in doc.first_section.body.paragraphs))
                #ExEnd

    def test_trail_spaces(self):

        parameters = [
            (aw.loading.TxtLeadingSpacesOptions.PRESERVE, aw.loading.TxtTrailingSpacesOptions.PRESERVE),
            (aw.loading.TxtLeadingSpacesOptions.CONVERT_TO_INDENT, aw.loading.TxtTrailingSpacesOptions.PRESERVE),
            (aw.loading.TxtLeadingSpacesOptions.TRIM, aw.loading.TxtTrailingSpacesOptions.TRIM)]

        for txt_leading_spaces_options, txt_trailing_spaces_options in parameters:
            with self.subTest(txt_leading_spaces_options=txt_leading_spaces_options, txt_trailing_spaces_options=txt_trailing_spaces_options):
                #ExStart
                #ExFor:TxtLoadOptions.TrailingSpacesOptions
                #ExFor:TxtLoadOptions.LeadingSpacesOptions
                #ExFor:TxtTrailingSpacesOptions
                #ExFor:TxtLeadingSpacesOptions
                #ExSummary:Shows how to trim whitespace when loading plaintext documents.
                text_doc = (
                    "      Line 1 \n" +
                    "    Line 2   \n" +
                    " Line 3       ")

                # Create a "TxtLoadOptions" object, which we can pass to a document's constructor
                # to modify how we load a plaintext document.
                load_options = aw.loading.TxtLoadOptions()

                # Set the "leading_spaces_options" property to "TxtLeadingSpacesOptions.PRESERVE"
                # to preserve all whitespace characters at the start of every line.
                # Set the "leading_spaces_options" property to "TxtLeadingSpacesOptions.CONVERT_TO_INDENT"
                # to remove all whitespace characters from the start of every line,
                # and then apply a left first line indent to the paragraph to simulate the effect of the whitespaces.
                # Set the "leading_spaces_options" property to "TxtLeadingSpacesOptions.TRIM"
                # to remove all whitespace characters from every line's start.
                load_options.leading_spaces_options = txt_leading_spaces_options

                # Set the "trailing_spaces_options" property to "TxtTrailingSpacesOptions.PRESERVE"
                # to preserve all whitespace characters at the end of every line.
                # Set the "trailing_spaces_options" property to "TxtTrailingSpacesOptions.TRIM" to
                # remove all whitespace characters from the end of every line.
                load_options.trailing_spaces_options = txt_trailing_spaces_options

                doc = aw.Document(io.BytesIO(text_doc.encode("utf-8")), load_options)
                paragraphs = doc.first_section.body.paragraphs

                if txt_leading_spaces_options == aw.loading.TxtLeadingSpacesOptions.CONVERT_TO_INDENT:
                    self.assertEqual(37.8, paragraphs[0].paragraph_format.first_line_indent)
                    self.assertEqual(25.2, paragraphs[1].paragraph_format.first_line_indent)
                    self.assertEqual(6.3, paragraphs[2].paragraph_format.first_line_indent)

                    self.assertTrue(paragraphs[0].get_text().startswith("Line 1"))
                    self.assertTrue(paragraphs[1].get_text().startswith("Line 2"))
                    self.assertTrue(paragraphs[2].get_text().startswith("Line 3"))
                
                elif txt_leading_spaces_options == aw.loading.TxtLeadingSpacesOptions.PRESERVE:
                    self.assertTrue(all(p.as_paragraph().paragraph_format.first_line_indent == 0.0 
                                        for p in paragraphs))

                    self.assertTrue(paragraphs[0].get_text().startswith("      Line 1"))
                    self.assertTrue(paragraphs[1].get_text().startswith("    Line 2"))
                    self.assertTrue(paragraphs[2].get_text().startswith(" Line 3"))
                
                elif txt_leading_spaces_options == aw.loading.TxtLeadingSpacesOptions.TRIM:
                    self.assertTrue(all(p.as_paragraph().paragraph_format.first_line_indent == 0.0
                                        for p in paragraphs))

                    self.assertTrue(paragraphs[0].get_text().startswith("Line 1"))
                    self.assertTrue(paragraphs[1].get_text().startswith("Line 2"))
                    self.assertTrue(paragraphs[2].get_text().startswith("Line 3"))

                if txt_trailing_spaces_options == aw.loading.TxtTrailingSpacesOptions.PRESERVE:
                    self.assertTrue(paragraphs[0].get_text().endswith("Line 1 \r"))
                    self.assertTrue(paragraphs[1].get_text().endswith("Line 2   \r"))
                    self.assertTrue(paragraphs[2].get_text().endswith("Line 3       \f"))
                
                elif txt_trailing_spaces_options == aw.loading.TxtTrailingSpacesOptions.TRIM:
                    self.assertTrue(paragraphs[0].get_text().endswith("Line 1\r"))
                    self.assertTrue(paragraphs[1].get_text().endswith("Line 2\r"))
                    self.assertTrue(paragraphs[2].get_text().endswith("Line 3\f"))
                #ExEnd

    def test_detect_document_direction(self):

        #ExStart
        #ExFor:TxtLoadOptions.DocumentDirection
        #ExFor:ParagraphFormat.Bidi
        #ExSummary:Shows how to detect plaintext document text direction.
        # Create a "TxtLoadOptions" object, which we can pass to a document's constructor
        # to modify how we load a plaintext document.
        load_options = aw.loading.TxtLoadOptions()

        # Set the "document_direction" property to "DocumentDirection.AUTO" automatically detects
        # the direction of every paragraph of text that Aspose.Words loads from plaintext.
        # Each paragraph's "bidi" property will store its direction.
        load_options.document_direction = aw.loading.DocumentDirection.AUTO

        # Detect Hebrew text as right-to-left.
        doc = aw.Document(MY_DIR + "Hebrew text.txt", load_options)

        self.assertTrue(doc.first_section.body.first_paragraph.paragraph_format.bidi)

        # Detect English text as right-to-left.
        doc = aw.Document(MY_DIR + "English text.txt", load_options)

        self.assertFalse(doc.first_section.body.first_paragraph.paragraph_format.bidi)
        #ExEnd
