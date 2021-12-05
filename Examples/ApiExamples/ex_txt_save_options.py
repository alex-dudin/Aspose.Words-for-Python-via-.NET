import unittest
import io

import aspose.words as aw
import aspose.pydrawing as drawing

from api_example_base import ApiExampleBase, my_dir, artifacts_dir

MY_DIR = my_dir
ARTIFACTS_DIR = artifacts_dir

class ExTxtSaveOptions(ApiExampleBase):

    def test_page_breaks(self):

        for force_page_breaks in (False, True):
            with self.subTest(force_page_breaks=force_page_breaks):
                #ExStart
                #ExFor:TxtSaveOptionsBase.ForcePageBreaks
                #ExSummary:Shows how to specify whether to preserve page breaks when exporting a document to plaintext.
                doc = aw.Document()
                builder = aw.DocumentBuilder(doc)

                builder.writeln("Page 1")
                builder.insert_break(aw.BreakType.PAGE_BREAK)
                builder.writeln("Page 2")
                builder.insert_break(aw.BreakType.PAGE_BREAK)
                builder.writeln("Page 3")

                # Create a "TxtSaveOptions" object, which we can pass to the document's "save"
                # method to modify how we save the document to plaintext.
                save_options = aw.saving.TxtSaveOptions()

                # The Aspose.Words "Document" objects have page breaks, just like Microsoft Word documents.
                # Save formats such as ".txt" are one continuous body of text without page breaks.
                # Set the "force_page_breaks" property to "True" to preserve all page breaks in the form of '\f' characters.
                # Set the "force_page_breaks" property to "False" to discard all page breaks.
                save_options.force_page_breaks = force_page_breaks

                doc.save(ARTIFACTS_DIR + "TxtSaveOptions.PageBreaks.txt", save_options)

                # If we load a plaintext document with page breaks,
                # the "Document" object will use them to split the body into pages.
                doc = aw.Document(ARTIFACTS_DIR + "TxtSaveOptions.PageBreaks.txt")

                self.assertEqual(3 if force_page_breaks else 1, doc.page_count)
                #ExEnd

                #TestUtil.file_contains_string(
                #    "Page 1\r\n\fPage 2\r\n\fPage 3\r\n\r\n" if force_page_breaks else "Page 1\r\nPage 2\r\nPage 3\r\n\r\n",
                #    ARTIFACTS_DIR + "TxtSaveOptions.PageBreaks.txt")

    def test_add_bidi_marks(self):

        for add_bidi_marks in (False, True):
            with self.subTest(add_bidi_marks=add_bidi_marks):
                #ExStart
                #ExFor:TxtSaveOptions.AddBidiMarks
                #ExSummary:Shows how to insert Unicode Character 'RIGHT-TO-LEFT MARK' (U+200F) before each bi-directional Run in text.
                doc = aw.Document()
                builder = aw.DocumentBuilder(doc)

                builder.writeln("Hello world!")
                builder.paragraph_format.bidi = True
                builder.writeln("שלום עולם!")
                builder.writeln("مرحبا بالعالم!")

                # Create a "TxtSaveOptions" object, which we can pass to the document's "save" method
                # to modify how we save the document to plaintext.
                save_options = aw.saving.TxtSaveOptions()
                save_options.encoding = "utf-8"

                # Set the "add_bidi_marks" property to "True" to add marks before runs
                # with right-to-left text to indicate the fact.
                # Set the "add_bidi_marks" property to "False" to write all left-to-right
                # and right-to-left run equally with nothing to indicate which is which.
                save_options.add_bidi_marks = add_bidi_marks

                doc.save(ARTIFACTS_DIR + "TxtSaveOptions.AddBidiMarks.txt", save_options)

                with open(ARTIFACTS_DIR + "TxtSaveOptions.AddBidiMarks.txt", "rb") as file:
                    doc_text = file.read().decode('utf-8')

                if add_bidi_marks:
                    self.assertEqual("\uFEFFHello world!‎\r\nשלום עולם!‏\r\nمرحبا بالعالم!‏\r\n\r\n", doc_text)
                    self.assertIn("\u200f", doc_text)
                else:
                    self.assertEqual("\uFEFFHello world!\r\nשלום עולם!\r\nمرحبا بالعالم!\r\n\r\n", doc_text)
                    self.assertNotIn("\u200f", doc_text)

                #ExEnd

    def test_export_headers_footers(self):

        for txt_export_headers_footers_mode in (aw.saving.TxtExportHeadersFootersMode.ALL_AT_END,
                                                aw.saving.TxtExportHeadersFootersMode.PRIMARY_ONLY,
                                                aw.saving.TxtExportHeadersFootersMode.NONE):
            with self.subTest(txt_export_headers_footers_mode=txt_export_headers_footers_mode):
                #ExStart
                #ExFor:TxtSaveOptionsBase.ExportHeadersFootersMode
                #ExFor:TxtExportHeadersFootersMode
                #ExSummary:Shows how to specify how to export headers and footers to plain text format.
                doc = aw.Document()

                # Insert even and primary headers/footers into the document.
                # The primary header/footers will override the even headers/footers.
                doc.first_section.headers_footers.add(aw.HeaderFooter(doc, aw.HeaderFooterType.HEADER_EVEN))
                doc.first_section.headers_footers[aw.HeaderFooterType.HEADER_EVEN].append_paragraph("Even header")
                doc.first_section.headers_footers.add(aw.HeaderFooter(doc, aw.HeaderFooterType.FOOTER_EVEN))
                doc.first_section.headers_footers[aw.HeaderFooterType.FOOTER_EVEN].append_paragraph("Even footer")
                doc.first_section.headers_footers.add(aw.HeaderFooter(doc, aw.HeaderFooterType.HEADER_PRIMARY))
                doc.first_section.headers_footers[aw.HeaderFooterType.HEADER_PRIMARY].append_paragraph("Primary header")
                doc.first_section.headers_footers.add(aw.HeaderFooter(doc, aw.HeaderFooterType.FOOTER_PRIMARY))
                doc.first_section.headers_footers[aw.HeaderFooterType.FOOTER_PRIMARY].append_paragraph("Primary footer")

                # Insert pages to display these headers and footers.
                builder = aw.DocumentBuilder(doc)
                builder.writeln("Page 1")
                builder.insert_break(aw.BreakType.PAGE_BREAK)
                builder.writeln("Page 2")
                builder.insert_break(aw.BreakType.PAGE_BREAK)
                builder.write("Page 3")

                # Create a "TxtSaveOptions" object, which we can pass to the document's "save" method
                # to modify how we save the document to plaintext.
                save_options = aw.saving.TxtSaveOptions()

                # Set the "export_headers_footers_mode" property to "TxtExportHeadersFootersMode.NONE"
                # to not export any headers/footers.
                # Set the "export_headers_footers_mode" property to "TxtExportHeadersFootersMode.PRIMARY_ONLY"
                # to only export primary headers/footers.
                # Set the "export_headers_footers_mode" property to "TxtExportHeadersFootersMode.ALL_AT_END"
                # to place all headers and footers for all section bodies at the end of the document.
                save_options.export_headers_footers_mode = txt_export_headers_footers_mode

                doc.save(ARTIFACTS_DIR + "TxtSaveOptions.ExportHeadersFooters.txt", save_options)

                with open(ARTIFACTS_DIR + "TxtSaveOptions.ExportHeadersFooters.txt", "rb") as file:
                    doc_text = file.read().decode("utf-8-sig")

                if txt_export_headers_footers_mode == aw.saving.TxtExportHeadersFootersMode.ALL_AT_END:
                    self.assertEqual(
                        "Page 1\r\n" +
                        "Page 2\r\n" +
                        "Page 3\r\n" +
                        "Even header\r\n\r\n" +
                        "Primary header\r\n\r\n" +
                        "Even footer\r\n\r\n" +
                        "Primary footer\r\n\r\n", doc_text)
                elif txt_export_headers_footers_mode ==  aw.saving.TxtExportHeadersFootersMode.PRIMARY_ONLY:
                    self.assertEqual(
                        "Primary header\r\n" +
                        "Page 1\r\n" +
                        "Page 2\r\n" +
                        "Page 3\r\n" +
                        "Primary footer\r\n", doc_text)
                elif txt_export_headers_footers_mode == aw.saving.TxtExportHeadersFootersMode.NONE:
                    self.assertEqual(
                        "Page 1\r\n" +
                        "Page 2\r\n" +
                        "Page 3\r\n", doc_text)

                #ExEnd

    def test_txt_list_indentation(self):

        #ExStart
        #ExFor:TxtListIndentation
        #ExFor:TxtListIndentation.Count
        #ExFor:TxtListIndentation.Character
        #ExFor:TxtSaveOptions.ListIndentation
        #ExSummary:Shows how to configure list indenting when saving a document to plaintext.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Create a list with three levels of indentation.
        builder.list_format.apply_number_default()
        builder.writeln("Item 1")
        builder.list_format.list_indent()
        builder.writeln("Item 2")
        builder.list_format.list_indent()
        builder.write("Item 3")

        # Create a "TxtSaveOptions" object, which we can pass to the document's "save" method
        # to modify how we save the document to plaintext.
        txt_save_options = aw.saving.TxtSaveOptions()

        # Set the "character" property to assign a character to use
        # for padding that simulates list indentation in plaintext.
        txt_save_options.list_indentation.character = ' '

        # Set the "count" property to specify the number of times
        # to place the padding character for each list indent level.
        txt_save_options.list_indentation.count = 3

        doc.save(ARTIFACTS_DIR + "TxtSaveOptions.TxtListIndentation.txt", txt_save_options)

        with open(ARTIFACTS_DIR + "TxtSaveOptions.TxtListIndentation.txt", "rb") as file:
            doc_text = file.read().decode("utf-8-sig")

        self.assertEqual(
            "1. Item 1\r\n" +
            "   a. Item 2\r\n" +
            "      i. Item 3\r\n", doc_text)
        #ExEnd

    def test_simplify_list_labels(self):

        for simplify_list_labels in (False, True):
            with self.subTest(simplify_list_labels=simplify_list_labels):
                #ExStart
                #ExFor:TxtSaveOptions.SimplifyListLabels
                #ExSummary:Shows how to change the appearance of lists when saving a document to plaintext.
                doc = aw.Document()
                builder = aw.DocumentBuilder(doc)

                # Create a bulleted list with five levels of indentation.
                builder.list_format.apply_bullet_default()
                builder.writeln("Item 1")
                builder.list_format.list_indent()
                builder.writeln("Item 2")
                builder.list_format.list_indent()
                builder.writeln("Item 3")
                builder.list_format.list_indent()
                builder.writeln("Item 4")
                builder.list_format.list_indent()
                builder.write("Item 5")

                # Create a "TxtSaveOptions" object, which we can pass to the document's "save" method
                # to modify how we save the document to plaintext.
                txt_save_options = aw.saving.TxtSaveOptions()

                # Set the "simplify_list_labels" property to "True" to convert some list
                # symbols into simpler ASCII characters, such as '*', 'o', '+', '>', etc.
                # Set the "simplify_list_labels" property to "False" to preserve as many original list symbols as possible.
                txt_save_options.simplify_list_labels = simplify_list_labels

                doc.save(ARTIFACTS_DIR + "TxtSaveOptions.SimplifyListLabels.txt", txt_save_options)

                with open(ARTIFACTS_DIR + "TxtSaveOptions.SimplifyListLabels.txt", "rb") as file:
                    doc_text = file.read().decode("utf-8-sig")

                if simplify_list_labels:
                    self.assertEqual(
                        "* Item 1\r\n" +
                        "  > Item 2\r\n" +
                        "    + Item 3\r\n" +
                        "      - Item 4\r\n" +
                        "        o Item 5\r\n", doc_text)
                else:
                    self.assertEqual(
                        "· Item 1\r\n" +
                        "o Item 2\r\n" +
                        "§ Item 3\r\n" +
                        "· Item 4\r\n" +
                        "o Item 5\r\n", doc_text)
                #ExEnd

    def test_paragraph_break(self):

        #ExStart
        #ExFor:TxtSaveOptions
        #ExFor:TxtSaveOptions.SaveFormat
        #ExFor:TxtSaveOptionsBase
        #ExFor:TxtSaveOptionsBase.ParagraphBreak
        #ExSummary:Shows how to save a .txt document with a custom paragraph break.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.writeln("Paragraph 1.")
        builder.writeln("Paragraph 2.")
        builder.write("Paragraph 3.")

        # Create a "TxtSaveOptions" object, which we can pass to the document's "Save" method
        # to modify how we save the document to plaintext.
        txt_save_options = aw.saving.TxtSaveOptions()

        self.assertEqual(aw.SaveFormat.TEXT, txt_save_options.save_format)

        # Set the "paragraph_break" to a custom value that we wish to put at the end of every paragraph.
        txt_save_options.paragraph_break = " End of paragraph.\n\n\t"

        doc.save(ARTIFACTS_DIR + "TxtSaveOptions.ParagraphBreak.txt", txt_save_options)

        with open(ARTIFACTS_DIR + "TxtSaveOptions.ParagraphBreak.txt", "rb") as file:
            doc_text = file.read().decode("utf-8-sig")

        self.assertEqual(
            "Paragraph 1. End of paragraph.\n\n\t" +
            "Paragraph 2. End of paragraph.\n\n\t" +
            "Paragraph 3. End of paragraph.\n\n\t", doc_text)
        #ExEnd

    def test_encoding(self):

        #ExStart
        #ExFor:TxtSaveOptionsBase.Encoding
        #ExSummary:Shows how to set encoding for a .txt output document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Add some text with characters from outside the ASCII character set.
        builder.write("À È Ì Ò Ù.")

        # Create a "TxtSaveOptions" object, which we can pass to the document's "save" method
        # to modify how we save the document to plaintext.
        txt_save_options = aw.saving.TxtSaveOptions()

        # Verify that the "encoding" property contains the appropriate encoding for our document's contents.
        self.assertEqual("utf-8", txt_save_options.encoding)

        doc.save(ARTIFACTS_DIR + "TxtSaveOptions.Encoding.UTF8.txt", txt_save_options)

        with open(ARTIFACTS_DIR + "TxtSaveOptions.Encoding.UTF8.txt", "rb") as file:
            doc_text = file.read().decode('utf-8')

        self.assertEqual("\uFEFFÀ È Ì Ò Ù.\r\n", doc_text)

        # Using an unsuitable encoding may result in a loss of document contents.
        txt_save_options.encoding = "ascii"
        doc.save(ARTIFACTS_DIR + "TxtSaveOptions.Encoding.ASCII.txt", txt_save_options)

        with open(ARTIFACTS_DIR + "TxtSaveOptions.Encoding.ASCII.txt", "rb") as file:
            doc_text = file.read().decode('ascii')
        
        self.assertEqual("? ? ? ? ?.\r\n", doc_text)
        #ExEnd

    def test_preserve_table_layout(self):

        for preserve_table_layout in (False, True):
            with self.subTest(preserve_table_layout=preserve_table_layout):
                #ExStart
                #ExFor:TxtSaveOptions.PreserveTableLayout
                #ExSummary:Shows how to preserve the layout of tables when converting to plaintext.
                doc = aw.Document()
                builder = aw.DocumentBuilder(doc)

                builder.start_table()
                builder.insert_cell()
                builder.write("Row 1, cell 1")
                builder.insert_cell()
                builder.write("Row 1, cell 2")
                builder.end_row()
                builder.insert_cell()
                builder.write("Row 2, cell 1")
                builder.insert_cell()
                builder.write("Row 2, cell 2")
                builder.end_table()

                # Create a "TxtSaveOptions" object, which we can pass to the document's "Save" method
                # to modify how we save the document to plaintext.
                txt_save_options = aw.saving.TxtSaveOptions()

                # Set the "preserve_table_layout" property to "True" to apply whitespace padding to the contents
                # of the output plaintext document to preserve as much of the table's layout as possible.
                # Set the "preserve_table_layout" property to "False" to save all tables' contents
                # as a continuous body of text, with just a new line for each row.
                txt_save_options.preserve_table_layout = preserve_table_layout

                doc.save(ARTIFACTS_DIR + "TxtSaveOptions.PreserveTableLayout.txt", txt_save_options)

                with open(ARTIFACTS_DIR + "TxtSaveOptions.PreserveTableLayout.txt", "rb") as file:
                    doc_text = file.read().decode("utf-8-sig")

                if preserve_table_layout:
                    self.assertEqual(
                        "Row 1, cell 1                                            Row 1, cell 2\r\n" +
                        "Row 2, cell 1                                            Row 2, cell 2\r\n\r\n", doc_text)
                else:
                    self.assertEqual(
                        "Row 1, cell 1\r" +
                        "Row 1, cell 2\r" +
                        "Row 2, cell 1\r" +
                        "Row 2, cell 2\r\r\n", doc_text)
                #ExEnd

    def test_max_characters_per_line(self):

        #ExStart
        #ExFor:TxtSaveOptions.MaxCharactersPerLine
        #ExSummary:Shows how to set maximum number of characters per line.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " +
                      "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")

        # Set 30 characters as maximum allowed per one line.
        save_options = aw.saving.TxtSaveOptions()
        save_options.max_characters_per_line = 30

        doc.save(ARTIFACTS_DIR + "TxtSaveOptions.MaxCharactersPerLine.txt", save_options)
        #ExEnd
