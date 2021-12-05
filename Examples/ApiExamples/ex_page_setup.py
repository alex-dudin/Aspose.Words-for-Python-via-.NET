import unittest
import io

import aspose.words as aw
import aspose.pydrawing as drawing

from api_example_base import ApiExampleBase, my_dir, artifacts_dir
from document_helper import DocumentHelper

MY_DIR = my_dir
ARTIFACTS_DIR = artifacts_dir

class ExPageSetup(ApiExampleBase):

    def test_clear_formatting(self):

        #ExStart
        #ExFor:DocumentBuilder.PageSetup
        #ExFor:DocumentBuilder.InsertBreak
        #ExFor:DocumentBuilder.Document
        #ExFor:PageSetup
        #ExFor:PageSetup.Orientation
        #ExFor:PageSetup.VerticalAlignment
        #ExFor:PageSetup.ClearFormatting
        #ExFor:Orientation
        #ExFor:PageVerticalAlignment
        #ExFor:BreakType
        #ExSummary:Shows how to apply and revert page setup settings to sections in a document.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Modify the page setup properties for the builder's current section and add text.
        builder.page_setup.orientation = aw.Orientation.LANDSCAPE
        builder.page_setup.vertical_alignment = aw.PageVerticalAlignment.CENTER
        builder.writeln("This is the first section, which landscape oriented with vertically centered text.")

        # If we start a new section using a document builder,
        # it will inherit the builder's current page setup properties.
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)

        self.assertEqual(aw.Orientation.LANDSCAPE, doc.sections[1].page_setup.orientation)
        self.assertEqual(aw.PageVerticalAlignment.CENTER, doc.sections[1].page_setup.vertical_alignment)

        # We can revert its page setup properties to their default values using the "ClearFormatting" method.
        builder.page_setup.clear_formatting()

        self.assertEqual(aw.Orientation.PORTRAIT, doc.sections[1].page_setup.orientation)
        self.assertEqual(aw.PageVerticalAlignment.TOP, doc.sections[1].page_setup.vertical_alignment)

        builder.writeln("This is the second section, which is in default Letter paper size, portrait orientation and top alignment.")

        doc.save(ARTIFACTS_DIR + "PageSetup.clear_formatting.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.clear_formatting.docx")

        self.assertEqual(aw.Orientation.LANDSCAPE, doc.sections[0].page_setup.orientation)
        self.assertEqual(aw.PageVerticalAlignment.CENTER, doc.sections[0].page_setup.vertical_alignment)

        self.assertEqual(aw.Orientation.PORTRAIT, doc.sections[1].page_setup.orientation)
        self.assertEqual(aw.PageVerticalAlignment.TOP, doc.sections[1].page_setup.vertical_alignment)

    def test_different_first_page_header_footer(self):

        for different_first_page_header_footer in (False, True):
            with self.subTest(different_first_page_header_footer=different_first_page_header_footer):
                #ExStart
                #ExFor:PageSetup.DifferentFirstPageHeaderFooter
                #ExSummary:Shows how to enable or disable primary headers/footers.
                doc = aw.Document()
                builder = aw.DocumentBuilder(doc)

                # Below are two types of header/footers.
                # 1 -  The "First" header/footer, which appears on the first page of the section.
                builder.move_to_header_footer(aw.HeaderFooterType.HEADER_FIRST)
                builder.writeln("First page header.")

                builder.move_to_header_footer(aw.HeaderFooterType.FOOTER_FIRST)
                builder.writeln("First page footer.")

                # 2 -  The "Primary" header/footer, which appears on every page in the section.
                # We can override the primary header/footer by a first and an even page header/footer.
                builder.move_to_header_footer(aw.HeaderFooterType.HEADER_PRIMARY)
                builder.writeln("Primary header.")

                builder.move_to_header_footer(aw.HeaderFooterType.FOOTER_PRIMARY)
                builder.writeln("Primary footer.")

                builder.move_to_section(0)
                builder.writeln("Page 1.")
                builder.insert_break(aw.BreakType.PAGE_BREAK)
                builder.writeln("Page 2.")
                builder.insert_break(aw.BreakType.PAGE_BREAK)
                builder.writeln("Page 3.")

                # Each section has a "page_setup" object that specifies page appearance-related properties
                # such as orientation, size, and borders.
                # Set the "DifferentFirstPageHeaderFooter" property to "True" to apply the first header/footer to the first page.
                # Set the "DifferentFirstPageHeaderFooter" property to "False"
                # to make the first page display the primary header/footer.
                builder.page_setup.different_first_page_header_footer = different_first_page_header_footer

                doc.save(ARTIFACTS_DIR + "PageSetup.different_first_page_header_footer.docx")
                #ExEnd

                doc = aw.Document(ARTIFACTS_DIR + "PageSetup.different_first_page_header_footer.docx")

                self.assertEqual(different_first_page_header_footer, doc.first_section.page_setup.different_first_page_header_footer)

    def test_odd_and_even_pages_header_footer(self):

        for odd_and_even_pages_header_footer in (False, True):
            with self.subTest(odd_and_even_pages_header_footer=odd_and_even_pages_header_footer):
                #ExStart
                #ExFor:PageSetup.OddAndEvenPagesHeaderFooter
                #ExSummary:Shows how to enable or disable even page headers/footers.
                doc = aw.Document()
                builder = aw.DocumentBuilder(doc)

                # Below are two types of header/footers.
                # 1 -  The "Primary" header/footer, which appears on every page in the section.
                # We can override the primary header/footer by a first and an even page header/footer.
                builder.move_to_header_footer(aw.HeaderFooterType.HEADER_PRIMARY)
                builder.writeln("Primary header.")

                builder.move_to_header_footer(aw.HeaderFooterType.FOOTER_PRIMARY)
                builder.writeln("Primary footer.")

                # 2 -  The "Even" header/footer, which appears on every even page of this section.
                builder.move_to_header_footer(aw.HeaderFooterType.HEADER_EVEN)
                builder.writeln("Even page header.")

                builder.move_to_header_footer(aw.HeaderFooterType.FOOTER_EVEN)
                builder.writeln("Even page footer.")

                builder.move_to_section(0)
                builder.writeln("Page 1.")
                builder.insert_break(aw.BreakType.PAGE_BREAK)
                builder.writeln("Page 2.")
                builder.insert_break(aw.BreakType.PAGE_BREAK)
                builder.writeln("Page 3.")

                # Each section has a "page_setup" object that specifies page appearance-related properties
                # such as orientation, size, and borders.
                # Set the "odd_and_even_pages_header_Footer" property to "True"
                # to display the even page header/footer on even pages.
                # Set the "odd_and_even_pages_header_Footer" property to "False"
                # to display the primary header/footer on even pages.
                builder.page_setup.odd_and_even_pages_header_footer = odd_and_even_pages_header_footer

                doc.save(ARTIFACTS_DIR + "PageSetup.odd_and_even_pages_header_footer.docx")
                #ExEnd

                doc = aw.Document(ARTIFACTS_DIR + "PageSetup.odd_and_even_pages_header_footer.docx")

                self.assertEqual(odd_and_even_pages_header_footer, doc.first_section.page_setup.odd_and_even_pages_header_footer)

    def test_characters_per_line(self):

        #ExStart
        #ExFor:PageSetup.CharactersPerLine
        #ExFor:PageSetup.LayoutMode
        #ExFor:SectionLayoutMode
        #ExSummary:Shows how to specify a for the number of characters that each line may have.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Enable pitching, and then use it to set the number of characters per line in this section.
        builder.page_setup.layout_mode = aw.SectionLayoutMode.GRID
        builder.page_setup.characters_per_line = 10

        # The number of characters also depends on the size of the font.
        doc.styles.get_by_name("Normal").font.size = 20

        self.assertEqual(8, doc.first_section.page_setup.characters_per_line)

        builder.writeln("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

        doc.save(ARTIFACTS_DIR + "PageSetup.characters_per_line.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.characters_per_line.docx")

        self.assertEqual(aw.SectionLayoutMode.GRID, doc.first_section.page_setup.layout_mode)
        self.assertEqual(8, doc.first_section.page_setup.characters_per_line)

    def test_lines_per_page(self):

        #ExStart
        #ExFor:PageSetup.LinesPerPage
        #ExFor:PageSetup.LayoutMode
        #ExFor:ParagraphFormat.SnapToGrid
        #ExFor:SectionLayoutMode
        #ExSummary:Shows how to specify a limit for the number of lines that each page may have.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Enable pitching, and then use it to set the number of lines per page in this section.
        # A large enough font size will push some lines down onto the next page to avoid overlapping characters.
        builder.page_setup.layout_mode = aw.SectionLayoutMode.LINE_GRID
        builder.page_setup.lines_per_page = 15

        builder.paragraph_format.snap_to_grid = True

        for i in range(30):
            builder.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ")

        doc.save(ARTIFACTS_DIR + "PageSetup.lines_per_page.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.lines_per_page.docx")

        self.assertEqual(aw.SectionLayoutMode.LINE_GRID, doc.first_section.page_setup.layout_mode)
        self.assertEqual(15, doc.first_section.page_setup.lines_per_page)

        for paragraph in doc.first_section.body.paragraphs:
            paragraph = paragraph.as_paragraph()
            self.assertTrue(paragraph.paragraph_format.snap_to_grid)

    def test_set_section_start(self):

        #ExStart
        #ExFor:SectionStart
        #ExFor:PageSetup.SectionStart
        #ExFor:Document.Sections
        #ExSummary:Shows how to specify how a new section separates itself from the previous.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.writeln("This text is in section 1.")

        # Section break types determine how a new section separates itself from the previous section.
        # Below are five types of section breaks.
        # 1 -  Starts the next section on a new page:
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.writeln("This text is in section 2.")

        self.assertEqual(aw.SectionStart.NEW_PAGE, doc.sections[1].page_setup.section_start)

        # 2 -  Starts the next section on the current page:
        builder.insert_break(aw.BreakType.SECTION_BREAK_CONTINUOUS)
        builder.writeln("This text is in section 3.")

        self.assertEqual(aw.SectionStart.CONTINUOUS, doc.sections[2].page_setup.section_start)

        # 3 -  Starts the next section on a new even page:
        builder.insert_break(aw.BreakType.SECTION_BREAK_EVEN_PAGE)
        builder.writeln("This text is in section 4.")

        self.assertEqual(aw.SectionStart.EVEN_PAGE, doc.sections[3].page_setup.section_start)

        # 4 -  Starts the next section on a new odd page:
        builder.insert_break(aw.BreakType.SECTION_BREAK_ODD_PAGE)
        builder.writeln("This text is in section 5.")

        self.assertEqual(aw.SectionStart.ODD_PAGE, doc.sections[4].page_setup.section_start)

        # 5 -  Starts the next section on a new column:
        columns = builder.page_setup.text_columns
        columns.set_count(2)

        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_COLUMN)
        builder.writeln("This text is in section 6.")

        self.assertEqual(aw.SectionStart.NEW_COLUMN, doc.sections[5].page_setup.section_start)

        doc.save(ARTIFACTS_DIR + "PageSetup.set_section_start.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.set_section_start.docx")

        self.assertEqual(aw.SectionStart.NEW_PAGE, doc.sections[0].page_setup.section_start)
        self.assertEqual(aw.SectionStart.NEW_PAGE, doc.sections[1].page_setup.section_start)
        self.assertEqual(aw.SectionStart.CONTINUOUS, doc.sections[2].page_setup.section_start)
        self.assertEqual(aw.SectionStart.EVEN_PAGE, doc.sections[3].page_setup.section_start)
        self.assertEqual(aw.SectionStart.ODD_PAGE, doc.sections[4].page_setup.section_start)
        self.assertEqual(aw.SectionStart.NEW_COLUMN, doc.sections[5].page_setup.section_start)

    ## Run only when the printer driver is installed
    #def test_default_paper_tray(self):

    #    #ExStart
    #    #ExFor:PageSetup.FirstPageTray
    #    #ExFor:PageSetup.OtherPagesTray
    #    #ExSummary:Shows how to get all the sections in a document to use the default paper tray of the selected printer.
    #    doc = aw.Document()

    #    # Find the default printer that we will use for printing this document.
    #    # You can define a specific printer using the "PrinterName" property of the PrinterSettings object.
    #    settings = PrinterSettings()

    #    # The paper tray value stored in documents is printer specific.
    #    # This means the code below resets all page tray values to use the current printers default tray.
    #    # You can enumerate PrinterSettings.PaperSources to find the other valid paper tray values of the selected printer.
    #    for section in doc.sections:
    #        section = section.as_section()
    #        section.page_setup.first_page_tray = settings.default_page_settings.paper_source.raw_kind
    #        section.page_setup.other_pages_tray = settings.default_page_settings.paper_source.raw_kind

    #    #ExEnd

    #    for section in DocumentHelper.save_open(doc).sections:
    #        section = section.as_section()
    #        self.assertEqual(settings.default_page_settings.paper_source.raw_kind, section.page_setup.first_page_tray)
    #        self.assertEqual(settings.default_page_settings.paper_source.raw_kind, section.page_setup.other_pages_tray)

    ## Run only when the printer driver is installed
    #def test_paper_tray_for_different_paper_type(self):

    #    #ExStart
    #    #ExFor:PageSetup.FirstPageTray
    #    #ExFor:PageSetup.OtherPagesTray
    #    #ExSummary:Shows how to set up printing using different printer trays for different paper sizes.
    #    doc = aw.Document()

    #    # Find the default printer that we will use for printing this document.
    #    # You can define a specific printer using the "PrinterName" property of the PrinterSettings object.
    #    settings = PrinterSettings()

    #    # This is the tray we will use for pages in the "A4" paper size.
    #    printer_tray_for_a4 = settings.paper_sources[0].raw_kind

    #    # This is the tray we will use for pages in the "Letter" paper size.
    #    printer_tray_for_letter = settings.paper_sources[1].raw_kind

    #    # Modify the PageSettings object of this section to get Microsoft Word to instruct the printer
    #    # to use one of the trays we identified above, depending on this section's paper size.
    #    for section in doc.sections:
    #        section = section.as_section()

    #        if section.page_setup.paper_size == aw.PaperSize.LETTER:
    #            section.page_setup.first_page_tray = printer_tray_for_letter
    #            section.page_setup.other_pages_tray = printer_tray_for_letter

    #        elif section.page_setup.paper_size == aw.PaperSize.A4:
    #            section.page_setup.first_page_tray = printer_tray_for_a4
    #            section.page_setup.other_pages_tray = printer_tray_for_a4

    #    #ExEnd

    #    for section in DocumentHelper.save_open(doc).sections:
    #        section = section.as_section()

    #        if section.page_setup.paper_size == aw.PaperSize.LETTER:
    #            self.assertEqual(printer_tray_for_letter, section.page_setup.first_page_tray)
    #            self.assertEqual(printer_tray_for_letter, section.page_setup.other_pages_tray)

    #        elif section.page_setup.paper_size == aw.PaperSize.A4:
    #            self.assertEqual(printer_tray_for_a4, section.page_setup.first_page_tray)
    #            self.assertEqual(printer_tray_for_a4, section.page_setup.other_pages_tray)

    def test_page_margins(self):

        #ExStart
        #ExFor:ConvertUtil
        #ExFor:ConvertUtil.InchToPoint
        #ExFor:PaperSize
        #ExFor:PageSetup.PaperSize
        #ExFor:PageSetup.Orientation
        #ExFor:PageSetup.TopMargin
        #ExFor:PageSetup.BottomMargin
        #ExFor:PageSetup.LeftMargin
        #ExFor:PageSetup.RightMargin
        #ExFor:PageSetup.HeaderDistance
        #ExFor:PageSetup.FooterDistance
        #ExSummary:Shows how to adjust paper size, orientation, margins, along with other settings for a section.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.page_setup.paper_size = aw.PaperSize.LEGAL
        builder.page_setup.orientation = aw.Orientation.LANDSCAPE
        builder.page_setup.top_margin = aw.ConvertUtil.inch_to_point(1.0)
        builder.page_setup.bottom_margin = aw.ConvertUtil.inch_to_point(1.0)
        builder.page_setup.left_margin = aw.ConvertUtil.inch_to_point(1.5)
        builder.page_setup.right_margin = aw.ConvertUtil.inch_to_point(1.5)
        builder.page_setup.header_distance = aw.ConvertUtil.inch_to_point(0.2)
        builder.page_setup.footer_distance = aw.ConvertUtil.inch_to_point(0.2)

        builder.writeln("Hello world!")

        doc.save(ARTIFACTS_DIR + "PageSetup.page_margins.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.page_margins.docx")

        self.assertEqual(aw.PaperSize.LEGAL, doc.first_section.page_setup.paper_size)
        self.assertEqual(1008.0, doc.first_section.page_setup.page_width)
        self.assertEqual(612.0, doc.first_section.page_setup.page_height)
        self.assertEqual(aw.Orientation.LANDSCAPE, doc.first_section.page_setup.orientation)
        self.assertEqual(72.0, doc.first_section.page_setup.top_margin)
        self.assertEqual(72.0, doc.first_section.page_setup.bottom_margin)
        self.assertEqual(108.0, doc.first_section.page_setup.left_margin)
        self.assertEqual(108.0, doc.first_section.page_setup.right_margin)
        self.assertEqual(14.4, doc.first_section.page_setup.header_distance)
        self.assertEqual(14.4, doc.first_section.page_setup.footer_distance)

    def test_paper_sizes(self):

        #ExStart
        #ExFor:PaperSize
        #ExFor:PageSetup.PaperSize
        #ExSummary:Shows how to set page sizes.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # We can change the current page's size to a pre-defined size
        # by using the "PaperSize" property of this section's PageSetup object.
        builder.page_setup.paper_size = aw.PaperSize.TABLOID

        self.assertEqual(792.0, builder.page_setup.page_width)
        self.assertEqual(1224.0, builder.page_setup.page_height)

        builder.writeln(f"This page is {builder.page_setup.page_width}x{builder.page_setup.page_height}.")

        # Each section has its own PageSetup object. When we use a document builder to make a new section,
        # that section's PageSetup object inherits all the previous section's PageSetup object's values.
        builder.insert_break(aw.BreakType.SECTION_BREAK_EVEN_PAGE)

        self.assertEqual(aw.PaperSize.TABLOID, builder.page_setup.paper_size)

        builder.page_setup.paper_size = aw.PaperSize.A5
        builder.writeln(f"This page is {builder.page_setup.page_width}x{builder.page_setup.page_height}.")

        self.assertEqual(419.55, builder.page_setup.page_width)
        self.assertEqual(595.30, builder.page_setup.page_height)

        builder.insert_break(aw.BreakType.SECTION_BREAK_EVEN_PAGE)

        # Set a custom size for this section's pages.
        builder.page_setup.page_width = 620
        builder.page_setup.page_height = 480

        self.assertEqual(aw.PaperSize.CUSTOM, builder.page_setup.paper_size)

        builder.writeln(f"This page is {builder.page_setup.page_width}x{builder.page_setup.page_height}.")

        doc.save(ARTIFACTS_DIR + "PageSetup.paper_sizes.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.paper_sizes.docx")

        self.assertEqual(aw.PaperSize.TABLOID, doc.sections[0].page_setup.paper_size)
        self.assertEqual(792.0, doc.sections[0].page_setup.page_width)
        self.assertEqual(1224.0, doc.sections[0].page_setup.page_height)
        self.assertEqual(aw.PaperSize.A5, doc.sections[1].page_setup.paper_size)
        self.assertEqual(419.55, doc.sections[1].page_setup.page_width)
        self.assertEqual(595.30, doc.sections[1].page_setup.page_height)
        self.assertEqual(aw.PaperSize.CUSTOM, doc.sections[2].page_setup.paper_size)
        self.assertEqual(620.0, doc.sections[2].page_setup.page_width)
        self.assertEqual(480.0, doc.sections[2].page_setup.page_height)

    def test_columns_same_width(self):

        #ExStart
        #ExFor:PageSetup.TextColumns
        #ExFor:TextColumnCollection
        #ExFor:TextColumnCollection.Spacing
        #ExFor:TextColumnCollection.SetCount
        #ExSummary:Shows how to create multiple evenly spaced columns in a section.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        columns = builder.page_setup.text_columns
        columns.spacing = 100
        columns.set_count(2)

        builder.writeln("Column 1.")
        builder.insert_break(aw.BreakType.COLUMN_BREAK)
        builder.writeln("Column 2.")

        doc.save(ARTIFACTS_DIR + "PageSetup.columns_same_width.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.columns_same_width.docx")

        self.assertEqual(100.0, doc.first_section.page_setup.text_columns.spacing)
        self.assertEqual(2, doc.first_section.page_setup.text_columns.count)

    def test_custom_column_width(self):

        #ExStart
        #ExFor:TextColumnCollection.EvenlySpaced
        #ExFor:TextColumnCollection.Item
        #ExFor:TextColumn
        #ExFor:TextColumn.Width
        #ExFor:TextColumn.SpaceAfter
        #ExSummary:Shows how to create unevenly spaced columns.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        page_setup = builder.page_setup

        columns = page_setup.text_columns
        columns.evenly_spaced = False
        columns.set_count(2)

        # Determine the amount of room that we have available for arranging columns.
        content_width = page_setup.page_width - page_setup.left_margin - page_setup.right_margin

        self.assertAlmostEqual(470.30, content_width, delta=0.01)

        # Set the first column to be narrow.
        column = columns[0]
        column.width = 100
        column.space_after = 20

        # Set the second column to take the rest of the space available within the margins of the page.
        column = columns[1]
        column.width = content_width - column.width - column.space_after

        builder.writeln("Narrow column 1.")
        builder.insert_break(aw.BreakType.COLUMN_BREAK)
        builder.writeln("Wide column 2.")

        doc.save(ARTIFACTS_DIR + "PageSetup.custom_column_width.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.custom_column_width.docx")
        page_setup = doc.first_section.page_setup

        self.assertFalse(page_setup.text_columns.evenly_spaced)
        self.assertEqual(2, page_setup.text_columns.count)
        self.assertEqual(100.0, page_setup.text_columns[0].width)
        self.assertEqual(20.0, page_setup.text_columns[0].space_after)
        self.assertEqual(470.3, page_setup.text_columns[1].width)
        self.assertEqual(0.0, page_setup.text_columns[1].space_after)

    def test_vertical_line_between_columns(self):

        for line_between in (False, True):
            with self.subTest(line_between=line_between):
                #ExStart
                #ExFor:TextColumnCollection.LineBetween
                #ExSummary:Shows how to separate columns with a vertical line.
                doc = aw.Document()
                builder = aw.DocumentBuilder(doc)

                # Configure the current section's PageSetup object to divide the text into several columns.
                # Set the "line_between" property to "True" to put a dividing line between columns.
                # Set the "line_between" property to "False" to leave the space between columns blank.
                columns = builder.page_setup.text_columns
                columns.line_between = line_between
                columns.set_count(3)

                builder.writeln("Column 1.")
                builder.insert_break(aw.BreakType.COLUMN_BREAK)
                builder.writeln("Column 2.")
                builder.insert_break(aw.BreakType.COLUMN_BREAK)
                builder.writeln("Column 3.")

                doc.save(ARTIFACTS_DIR + "PageSetup.vertical_line_between_columns.docx")
                #ExEnd

                doc = aw.Document(ARTIFACTS_DIR + "PageSetup.vertical_line_between_columns.docx")

                self.assertEqual(line_between, doc.first_section.page_setup.text_columns.line_between)

    def test_line_numbers(self):

        #ExStart
        #ExFor:PageSetup.LineStartingNumber
        #ExFor:PageSetup.LineNumberDistanceFromText
        #ExFor:PageSetup.LineNumberCountBy
        #ExFor:PageSetup.LineNumberRestartMode
        #ExFor:ParagraphFormat.SuppressLineNumbers
        #ExFor:LineNumberRestartMode
        #ExSummary:Shows how to enable line numbering for a section.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # We can use the section's PageSetup object to display numbers to the left of the section's text lines.
        # This is the same behavior as a List object,
        # but it covers the entire section and does not modify the text in any way.
        # Our section will restart the numbering on each new page from 1 and display the number,
        # if it is a multiple of 3, at 50pt to the left of the line.
        page_setup = builder.page_setup
        page_setup.line_starting_number = 1
        page_setup.line_number_count_by = 3
        page_setup.line_number_restart_mode = aw.LineNumberRestartMode.RESTART_PAGE
        page_setup.line_number_distance_from_text = 50.0

        for i in range(1, 26):
            builder.writeln(f"Line {i}.")

        # The line counter will skip any paragraph with the "suppress_line_numbers" flag set to "True".
        # This paragraph is on the 15th line, which is a multiple of 3, and thus would normally display a line number.
        # The section's line counter will also ignore this line, treat the next line as the 15th,
        # and continue the count from that point onward.
        doc.first_section.body.paragraphs[14].paragraph_format.suppress_line_numbers = True

        doc.save(ARTIFACTS_DIR + "PageSetup.line_numbers.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.line_numbers.docx")
        page_setup = doc.first_section.page_setup

        self.assertEqual(1, page_setup.line_starting_number)
        self.assertEqual(3, page_setup.line_number_count_by)
        self.assertEqual(aw.LineNumberRestartMode.RESTART_PAGE, page_setup.line_number_restart_mode)
        self.assertEqual(50.0, page_setup.line_number_distance_from_text)

    def test_page_border_properties(self):

        #ExStart
        #ExFor:Section.PageSetup
        #ExFor:PageSetup.BorderAlwaysInFront
        #ExFor:PageSetup.BorderDistanceFrom
        #ExFor:PageSetup.BorderAppliesTo
        #ExFor:PageBorderDistanceFrom
        #ExFor:PageBorderAppliesTo
        #ExFor:Border.DistanceFromText
        #ExSummary:Shows how to create a wide blue band border at the top of the first page.
        doc = aw.Document()

        page_setup = doc.sections[0].page_setup
        page_setup.border_always_in_front = False
        page_setup.border_distance_from = aw.PageBorderDistanceFrom.PAGE_EDGE
        page_setup.border_applies_to = aw.PageBorderAppliesTo.FIRST_PAGE

        border = page_setup.borders[aw.BorderType.TOP]
        border.line_style = aw.LineStyle.SINGLE
        border.line_width = 30
        border.color = drawing.Color.blue
        border.distance_from_text = 0

        doc.save(ARTIFACTS_DIR + "PageSetup.page_border_properties.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.page_border_properties.docx")
        page_setup = doc.first_section.page_setup

        self.assertFalse(page_setup.border_always_in_front)
        self.assertEqual(aw.PageBorderDistanceFrom.PAGE_EDGE, page_setup.border_distance_from)
        self.assertEqual(aw.PageBorderAppliesTo.FIRST_PAGE, page_setup.border_applies_to)

        border = page_setup.borders[aw.BorderType.TOP]

        self.assertEqual(aw.LineStyle.SINGLE, border.line_style)
        self.assertEqual(30.0, border.line_width)
        self.assertEqual(drawing.Color.blue.to_argb(), border.color.to_argb())
        self.assertEqual(0.0, border.distance_from_text)

    def test_page_borders(self):

        #ExStart
        #ExFor:PageSetup.Borders
        #ExFor:Border.Shadow
        #ExFor:BorderCollection.LineStyle
        #ExFor:BorderCollection.LineWidth
        #ExFor:BorderCollection.Color
        #ExFor:BorderCollection.DistanceFromText
        #ExFor:BorderCollection.Shadow
        #ExSummary:Shows how to create green wavy page border with a shadow.
        doc = aw.Document()
        page_setup = doc.sections[0].page_setup

        page_setup.borders.line_style = aw.LineStyle.DOUBLE_WAVE
        page_setup.borders.line_width = 2
        page_setup.borders.color = drawing.Color.green
        page_setup.borders.distance_from_text = 24
        page_setup.borders.shadow = True

        doc.save(ARTIFACTS_DIR + "PageSetup.page_borders.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.page_borders.docx")
        page_setup = doc.first_section.page_setup

        for border in page_setup.borders:

            self.assertEqual(aw.LineStyle.DOUBLE_WAVE, border.line_style)
            self.assertEqual(2.0, border.line_width)
            self.assertEqual(drawing.Color.green.to_argb(), border.color.to_argb())
            self.assertEqual(24.0, border.distance_from_text)
            self.assertTrue(border.shadow)

    def test_page_numbering(self):

        #ExStart
        #ExFor:PageSetup.RestartPageNumbering
        #ExFor:PageSetup.PageStartingNumber
        #ExFor:PageSetup.PageNumberStyle
        #ExFor:DocumentBuilder.InsertField(String, String)
        #ExSummary:Shows how to set up page numbering in a section.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.writeln("Section 1, page 1.")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.writeln("Section 1, page 2.")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.writeln("Section 1, page 3.")
        builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)
        builder.writeln("Section 2, page 1.")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.writeln("Section 2, page 2.")
        builder.insert_break(aw.BreakType.PAGE_BREAK)
        builder.writeln("Section 2, page 3.")

        # Move the document builder to the first section's primary header,
        # which every page in that section will display.
        builder.move_to_section(0)
        builder.move_to_header_footer(aw.HeaderFooterType.HEADER_PRIMARY)

        # Insert a PAGE field, which will display the number of the current page.
        builder.write("Page ")
        builder.insert_field("PAGE", "")

        # Configure the section to have the page count that PAGE fields display start from 5.
        # Also, configure all PAGE fields to display their page numbers using uppercase Roman numerals.
        page_setup = doc.sections[0].page_setup
        page_setup.restart_page_numbering = True
        page_setup.page_starting_number = 5
        page_setup.page_number_style = aw.NumberStyle.UPPERCASE_ROMAN

        # Create another primary header for the second section, with another PAGE field.
        builder.move_to_section(1)
        builder.move_to_header_footer(aw.HeaderFooterType.HEADER_PRIMARY)
        builder.paragraph_format.alignment = aw.ParagraphAlignment.CENTER
        builder.write(" - ")
        builder.insert_field("PAGE", "")
        builder.write(" - ")

        # Configure the section to have the page count that PAGE fields display start from 10.
        # Also, configure all PAGE fields to display their page numbers using Arabic numbers.
        page_setup = doc.sections[1].page_setup
        page_setup.page_starting_number = 10
        page_setup.restart_page_numbering = True
        page_setup.page_number_style = aw.NumberStyle.ARABIC

        doc.save(ARTIFACTS_DIR + "PageSetup.page_numbering.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.page_numbering.docx")
        page_setup = doc.sections[0].page_setup

        self.assertTrue(page_setup.restart_page_numbering)
        self.assertEqual(5, page_setup.page_starting_number)
        self.assertEqual(aw.NumberStyle.UPPERCASE_ROMAN, page_setup.page_number_style)

        page_setup = doc.sections[1].page_setup

        self.assertTrue(page_setup.restart_page_numbering)
        self.assertEqual(10, page_setup.page_starting_number)
        self.assertEqual(aw.NumberStyle.ARABIC, page_setup.page_number_style)

    def test_footnote_options(self):

        #ExStart
        #ExFor:PageSetup.EndnoteOptions
        #ExFor:PageSetup.FootnoteOptions
        #ExSummary:Shows how to configure options affecting footnotes/endnotes in a section.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.write("Hello world!")
        builder.insert_footnote(aw.notes.FootnoteType.FOOTNOTE, "Footnote reference text.")

        # Configure all footnotes in the first section to restart the numbering from 1
        # at each new page and display themselves directly beneath the text on every page.
        footnote_options = doc.sections[0].page_setup.footnote_options
        footnote_options.position = aw.notes.FootnotePosition.BENEATH_TEXT
        footnote_options.restart_rule = aw.notes.FootnoteNumberingRule.RESTART_PAGE
        footnote_options.start_number = 1

        builder.write(" Hello again.")
        builder.insert_footnote(aw.notes.FootnoteType.FOOTNOTE, "Endnote reference text.")

        # Configure all endnotes in the first section to maintain a continuous count throughout the section,
        # starting from 1. Also, set them all to appear collected at the end of the document.
        endnote_options = doc.sections[0].page_setup.endnote_options
        endnote_options.position = aw.notes.EndnotePosition.END_OF_DOCUMENT
        endnote_options.restart_rule = aw.notes.FootnoteNumberingRule.CONTINUOUS
        endnote_options.start_number = 1

        doc.save(ARTIFACTS_DIR + "PageSetup.footnote_options.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.footnote_options.docx")
        footnote_options = doc.first_section.page_setup.footnote_options

        self.assertEqual(aw.notes.FootnotePosition.BENEATH_TEXT, footnote_options.position)
        self.assertEqual(aw.notes.FootnoteNumberingRule.RESTART_PAGE, footnote_options.restart_rule)
        self.assertEqual(1, footnote_options.start_number)

        endnote_options = doc.first_section.page_setup.endnote_options

        self.assertEqual(aw.notes.EndnotePosition.END_OF_DOCUMENT, endnote_options.position)
        self.assertEqual(aw.notes.FootnoteNumberingRule.CONTINUOUS, endnote_options.restart_rule)
        self.assertEqual(1, endnote_options.start_number)

    def test_bidi(self):

        for reverse_columns in (False, True):
            with self.subTest(reverse_columns=reverse_columns):
                #ExStart
                #ExFor:PageSetup.Bidi
                #ExSummary:Shows how to set the order of text columns in a section.
                doc = aw.Document()

                page_setup = doc.sections[0].page_setup
                page_setup.text_columns.set_count(3)

                builder = aw.DocumentBuilder(doc)
                builder.write("Column 1.")
                builder.insert_break(aw.BreakType.COLUMN_BREAK)
                builder.write("Column 2.")
                builder.insert_break(aw.BreakType.COLUMN_BREAK)
                builder.write("Column 3.")

                # Set the "bidi" property to "True" to arrange the columns starting from the page's right side.
                # The order of the columns will match the direction of the right-to-left text.
                # Set the "bidi" property to "False" to arrange the columns starting from the page's left side.
                # The order of the columns will match the direction of the left-to-right text.
                page_setup.bidi = reverse_columns

                doc.save(ARTIFACTS_DIR + "PageSetup.bidi.docx")
                #ExEnd

                doc = aw.Document(ARTIFACTS_DIR + "PageSetup.bidi.docx")
                page_setup = doc.first_section.page_setup

                self.assertEqual(3, page_setup.text_columns.count)
                self.assertEqual(reverse_columns, page_setup.bidi)

    def test_page_border(self):

        #ExStart
        #ExFor:PageSetup.BorderSurroundsFooter
        #ExFor:PageSetup.BorderSurroundsHeader
        #ExSummary:Shows how to apply a border to the page and header/footer.
        doc = aw.Document()

        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world! This is the main body text.")
        builder.move_to_header_footer(aw.HeaderFooterType.HEADER_PRIMARY)
        builder.write("This is the header.")
        builder.move_to_header_footer(aw.HeaderFooterType.FOOTER_PRIMARY)
        builder.write("This is the footer.")
        builder.move_to_document_end()

        # Insert a blue double-line border.
        page_setup = doc.sections[0].page_setup
        page_setup.borders.line_style = aw.LineStyle.DOUBLE
        page_setup.borders.color = drawing.Color.blue

        # A section's PageSetup object has "border_surrounds_header" and "border_surrounds_footer" flags that determine
        # whether a page border surrounds the main body text, also includes the header or footer, respectively.
        # Set the "border_surrounds_header" flag to "True" to surround the header with our border,
        # and then set the "border_surrounds_footer" flag to leave the footer outside of the border.
        page_setup.border_surrounds_header = True
        page_setup.border_surrounds_footer = False

        doc.save(ARTIFACTS_DIR + "PageSetup.page_border.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.page_border.docx")
        page_setup = doc.first_section.page_setup

        self.assertTrue(page_setup.border_surrounds_header)
        self.assertFalse(page_setup.border_surrounds_footer)

    def test_gutter(self):

        #ExStart
        #ExFor:PageSetup.Gutter
        #ExFor:PageSetup.RtlGutter
        #ExFor:PageSetup.MultiplePages
        #ExSummary:Shows how to set gutter margins.
        doc = aw.Document()

        # Insert text that spans several pages.
        builder = aw.DocumentBuilder(doc)
        for i in range(6):
            builder.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, " +
                          "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
            builder.insert_break(aw.BreakType.PAGE_BREAK)

        # A gutter adds whitespaces to either the left or right page margin,
        # which makes up for the center folding of pages in a book encroaching on the page's layout.
        page_setup = doc.sections[0].page_setup

        # Determine how much space our pages have for text within the margins and then add an amount to pad a margin.
        self.assertAlmostEqual(470.30, page_setup.page_width - page_setup.left_margin - page_setup.right_margin, delta=0.01)

        page_setup.gutter = 100.0

        # Set the "rtl_gutter" property to "True" to place the gutter in a more suitable position for right-to-left text.
        page_setup.rtl_gutter = True

        # Set the "multiple_pages" property to "MultiplePagesType.MIRROR_MARGINS" to alternate
        # the left/right page side position of margins every page.
        page_setup.multiple_pages = aw.settings.MultiplePagesType.MIRROR_MARGINS

        doc.save(ARTIFACTS_DIR + "PageSetup.gutter.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.gutter.docx")
        page_setup = doc.first_section.page_setup

        self.assertEqual(100.0, page_setup.gutter)
        self.assertTrue(page_setup.rtl_gutter)
        self.assertEqual(aw.settings.MultiplePagesType.MIRROR_MARGINS, page_setup.multiple_pages)

    def test_booklet(self):

        #ExStart
        #ExFor:PageSetup.Gutter
        #ExFor:PageSetup.MultiplePages
        #ExFor:PageSetup.SheetsPerBooklet
        #ExSummary:Shows how to configure a document that can be printed as a book fold.
        doc = aw.Document()

        # Insert text that spans 16 pages.
        builder = aw.DocumentBuilder(doc)
        builder.writeln("My Booklet:")

        for i in range(15):

            builder.insert_break(aw.BreakType.PAGE_BREAK)
            builder.write(f"Booklet face #{i}")

        # Configure the first section's "page_setup" property to print the document in the form of a book fold.
        # When we print this document on both sides, we can take the pages to stack them
        # and fold them all down the middle at once. The contents of the document will line up into a book fold.
        page_setup = doc.sections[0].page_setup
        page_setup.multiple_pages = aw.settings.MultiplePagesType.BOOK_FOLD_PRINTING

        # We can only specify the number of sheets in multiples of 4.
        page_setup.sheets_per_booklet = 4

        doc.save(ARTIFACTS_DIR + "PageSetup.booklet.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.booklet.docx")
        page_setup = doc.first_section.page_setup

        self.assertEqual(aw.settings.MultiplePagesType.BOOK_FOLD_PRINTING, page_setup.multiple_pages)
        self.assertEqual(4, page_setup.sheets_per_booklet)

    def test_set_text_orientation(self):

        #ExStart
        #ExFor:PageSetup.TextOrientation
        #ExSummary:Shows how to set text orientation.
        doc = aw.Document()

        builder = aw.DocumentBuilder(doc)
        builder.writeln("Hello world!")

        # Set the "text_orientation" property to "TextOrientation.UPWARD" to rotate all the text 90 degrees
        # to the right so that all left-to-right text now goes top-to-bottom.
        page_setup = doc.sections[0].page_setup
        page_setup.text_orientation = aw.TextOrientation.UPWARD

        doc.save(ARTIFACTS_DIR + "PageSetup.set_text_orientation.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "PageSetup.set_text_orientation.docx")
        page_setup = doc.first_section.page_setup

        self.assertEqual(aw.TextOrientation.UPWARD, page_setup.text_orientation)

    #ExStart
    #ExFor:PageSetup.SuppressEndnotes
    #ExFor:Body.ParentSection
    #ExSummary:Shows how to store endnotes at the end of each section, and modify their positions.
    def test_suppress_endnotes(self):

        doc = aw.Document()
        doc.remove_all_children()

        # By default, a document compiles all endnotes at its end.
        self.assertEqual(aw.notes.EndnotePosition.END_OF_DOCUMENT, doc.endnote_options.position)

        # We use the "position" property of the document's "EndnoteOptions" object
        # to collect endnotes at the end of each section instead.
        doc.endnote_options.position = aw.notes.EndnotePosition.END_OF_SECTION

        self.insert_section_with_endnote(doc, "Section 1", "Endnote 1, will stay in section 1")
        self.insert_section_with_endnote(doc, "Section 2", "Endnote 2, will be pushed down to section 3")
        self.insert_section_with_endnote(doc, "Section 3", "Endnote 3, will stay in section 3")

        # While getting sections to display their respective endnotes, we can set the "suppress_endnotes" flag
        # of a section's "page_setup" object to "True" to revert to the default behavior and pass its endnotes
        # onto the next section.
        page_setup = doc.sections[1].page_setup
        page_setup.suppress_endnotes = True

        doc.save(ARTIFACTS_DIR + "PageSetup.suppress_endnotes.docx")
        self._test_suppress_endnotes(aw.Document(ARTIFACTS_DIR + "PageSetup.suppress_endnotes.docx")) #ExSkip

    def insert_section_with_endnote(self, doc: aw.Document, section_body_text: str, endnote_text: str):
        """Append a section with text and an endnote to a document."""

        section = aw.Section(doc)

        doc.append_child(section)

        body = aw.Body(doc)
        section.append_child(body)

        self.assertEqual(section, body.parent_node)

        para = aw.Paragraph(doc)
        body.append_child(para)

        self.assertEqual(body, para.parent_node)

        builder = aw.DocumentBuilder(doc)
        builder.move_to(para)
        builder.write(section_body_text)
        builder.insert_footnote(aw.notes.FootnoteType.ENDNOTE, endnote_text)

    #ExEnd

    def _test_suppress_endnotes(self, doc: aw.Document):

        page_setup = doc.sections[1].page_setup

        self.assertTrue(page_setup.suppress_endnotes)
