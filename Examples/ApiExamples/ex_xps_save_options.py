import unittest
import io
import os

import aspose.words as aw
import aspose.pydrawing as drawing

from api_example_base import ApiExampleBase, my_dir, artifacts_dir

MY_DIR = my_dir
ARTIFACTS_DIR = artifacts_dir

class ExXpsSaveOptions(ApiExampleBase):

    def test_outline_levels(self):

        #ExStart
        #ExFor:XpsSaveOptions
        #ExFor:XpsSaveOptions.#ctor
        #ExFor:XpsSaveOptions.OutlineOptions
        #ExFor:XpsSaveOptions.SaveFormat
        #ExSummary:Shows how to limit the headings' level that will appear in the outline of a saved XPS document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Insert headings that can serve as TOC entries of levels 1, 2, and then 3.
        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING1

        self.assertTrue(builder.paragraph_format.is_heading)

        builder.writeln("Heading 1")

        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING2

        builder.writeln("Heading 1.1")
        builder.writeln("Heading 1.2")

        builder.paragraph_format.style_identifier = aw.StyleIdentifier.HEADING3

        builder.writeln("Heading 1.2.1")
        builder.writeln("Heading 1.2.2")

        # Create an "XpsSaveOptions" object that we can pass to the document's "save" method
        # to modify how that method converts the document to .XPS.
        save_options = aw.saving.XpsSaveOptions()

        self.assertEqual(aw.SaveFormat.XPS, save_options.save_format)

        # The output XPS document will contain an outline, a table of contents that lists headings in the document body.
        # Clicking on an entry in this outline will take us to the location of its respective heading.
        # Set the "headings_outline_levels" property to "2" to exclude all headings whose levels are above 2 from the outline.
        # The last two headings we have inserted above will not appear.
        save_options.outline_options.headings_outline_levels = 2

        doc.save(ARTIFACTS_DIR + "XpsSaveOptions.OutlineLevels.xps", save_options)
        #ExEnd

    def test_book_fold(self):

        for render_text_as_book_fold in (False, True):
            with self.subTest(render_text_as_book_fold=render_text_as_book_fold):
                #ExStart
                #ExFor:XpsSaveOptions.#ctor(SaveFormat)
                #ExFor:XpsSaveOptions.UseBookFoldPrintingSettings
                #ExSummary:Shows how to save a document to the XPS format in the form of a book fold.
                doc = aw.Document(MY_DIR + "Paragraphs.docx")

                # Create an "XpsSaveOptions" object that we can pass to the document's "save" method
                # to modify how that method converts the document to .XPS.
                xps_options = aw.saving.XpsSaveOptions(aw.SaveFormat.XPS)

                # Set the "use_book_fold_printing_settings" property to "true" to arrange the contents
                # in the output XPS in a way that helps us use it to make a booklet.
                # Set the "use_book_fold_printing_settings" property to "false" to render the XPS normally.
                xps_options.use_book_fold_printing_settings = render_text_as_book_fold

                # If we are rendering the document as a booklet, we must set the "multiple_pages"
                # properties of the page setup objects of all sections to "MultiplePagesType.BOOK_FOLD_PRINTING".
                if render_text_as_book_fold:
                    for section in doc.sections:
                        section = section.as_section()
                        section.page_setup.multiple_pages = aw.settings.MultiplePagesType.BOOK_FOLD_PRINTING

                # Once we print this document, we can turn it into a booklet by stacking the pages
                # to come out of the printer and folding down the middle.
                doc.save(ARTIFACTS_DIR + "XpsSaveOptions.BookFold.xps", xps_options)
                #ExEnd

    def test_optimize_output(self):

        for optimize_output in (False, True):
            with self.subTest(optimize_output=optimize_output):
                #ExStart
                #ExFor:FixedPageSaveOptions.OptimizeOutput
                #ExSummary:Shows how to optimize document objects while saving to xps.
                doc = aw.Document(MY_DIR + "Unoptimized document.docx")

                # Create an "XpsSaveOptions" object to pass to the document's "save" method
                # to modify how that method converts the document to .XPS.
                save_options = aw.saving.XpsSaveOptions()

                # Set the "optimize_output" property to "true" to take measures such as removing nested or empty canvases
                # and concatenating adjacent runs with identical formatting to optimize the output document's content.
                # This may affect the appearance of the document.
                # Set the "optimize_output" property to "false" to save the document normally.
                save_options.optimize_output = optimize_output

                doc.save(ARTIFACTS_DIR + "XpsSaveOptions.OptimizeOutput.xps", save_options)
                #ExEnd

                out_file_size = os.path.getsize(ARTIFACTS_DIR + "XpsSaveOptions.OptimizeOutput.xps")

                if optimize_output:
                    self.assertLess(out_file_size, 50000)
                else:
                    self.assertGreater(out_file_size, 60000)

                #TestUtil.DocPackageFileContainsString(
                #    optimizeOutput
                #        ? "Glyphs OriginX=\"34.294998169\" OriginY=\"10.31799984\" " +
                #          "UnicodeString=\"This document contains complex content which can be optimized to save space when \""
                #        : "<Glyphs OriginX=\"34.294998169\" OriginY=\"10.31799984\" UnicodeString=\"This\"",
                #    ARTIFACTS_DIR + "XpsSaveOptions.OptimizeOutput.xps", "1.fpage")

    def test_export_exact_pages(self):

        #ExStart
        #ExFor:FixedPageSaveOptions.PageSet
        #ExFor:PageSet.#ctor(int[])
        #ExSummary:Shows how to extract pages based on exact page indices.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Add five pages to the document.
        for i in range(1, 6):
            builder.write(f"Page {i}")
            builder.insert_break(aw.BreakType.PAGE_BREAK)

        # Create an "XpsSaveOptions" object, which we can pass to the document's "save" method
        # to modify how that method converts the document to .XPS.
        xps_options = aw.saving.XpsSaveOptions()

        # Use the "page_set" property to select a set of the document's pages to save to output XPS.
        # In this case, we will choose, via a zero-based index, only three pages: page 1, page 2, and page 4.
        xps_options.page_set = aw.saving.PageSet([0, 1, 3])

        doc.save(ARTIFACTS_DIR + "XpsSaveOptions.ExportExactPages.xps", xps_options)
        #ExEnd
