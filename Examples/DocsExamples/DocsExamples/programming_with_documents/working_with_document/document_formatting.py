import aspose.words as aw
import aspose.pydrawing as drawing
from docs_examples_base import DocsExamplesBase, MY_DIR, ARTIFACTS_DIR

class DocumentFormatting(DocsExamplesBase):

    def test_space_between_asian_and_latin_text(self):

        #ExStart:SpaceBetweenAsianAndLatinText
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        paragraph_format = builder.paragraph_format
        paragraph_format.add_space_between_far_east_and_alpha = True
        paragraph_format.add_space_between_far_east_and_digit = True

        builder.writeln("Automatically adjust space between Asian and Latin text")
        builder.writeln("Automatically adjust space between Asian text and numbers")

        doc.save(ARTIFACTS_DIR + "DocumentFormatting.space_between_asian_and_latin_text.docx")
        #ExEnd:SpaceBetweenAsianAndLatinText

    def test_asian_typography_line_break_group(self):

        #ExStart:AsianTypographyLineBreakGroup
        doc = aw.Document(MY_DIR + "Asian typography.docx")

        paragraph_format = doc.first_section.body.paragraphs[0].paragraph_format
        paragraph_format.far_east_line_break_control = False
        paragraph_format.word_wrap = True
        paragraph_format.hanging_punctuation = False

        doc.save(ARTIFACTS_DIR + "DocumentFormatting.asian_typography_line_break_group.docx")
        #ExEnd:AsianTypographyLineBreakGroup

    def test_paragraph_formatting(self):

        #ExStart:ParagraphFormatting
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        paragraph_format = builder.paragraph_format
        paragraph_format.alignment = aw.ParagraphAlignment.CENTER
        paragraph_format.left_indent = 50
        paragraph_format.right_indent = 50
        paragraph_format.space_after = 25

        builder.writeln(
            "I'm a very nice formatted paragraph. I'm intended to demonstrate how the left and right indents affect word wrapping.")
        builder.writeln(
            "I'm another nice formatted paragraph. I'm intended to demonstrate how the space after paragraph looks like.")

        doc.save(ARTIFACTS_DIR + "DocumentFormatting.paragraph_formatting.docx")
        #ExEnd:ParagraphFormatting

    def test_multilevel_list_formatting(self):

        #ExStart:MultilevelListFormatting
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.list_format.apply_number_default()
        builder.writeln("Item 1")
        builder.writeln("Item 2")

        builder.list_format.list_indent()
        builder.writeln("Item 2.1")
        builder.writeln("Item 2.2")

        builder.list_format.list_indent()
        builder.writeln("Item 2.2.1")
        builder.writeln("Item 2.2.2")

        builder.list_format.list_outdent()
        builder.writeln("Item 2.3")

        builder.list_format.list_outdent()
        builder.writeln("Item 3")

        builder.list_format.remove_numbers()

        doc.save(ARTIFACTS_DIR + "DocumentFormatting.multilevel_list_formatting.docx")
        #ExEnd:MultilevelListFormatting

    def test_apply_paragraph_style(self):

        #ExStart:ApplyParagraphStyle
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.paragraph_format.style_identifier = aw.StyleIdentifier.TITLE
        builder.write("Hello")

        doc.save(ARTIFACTS_DIR + "DocumentFormatting.apply_paragraph_style.docx")
        #ExEnd:ApplyParagraphStyle

    def test_apply_borders_and_shading_to_paragraph(self):

        #ExStart:ApplyBordersAndShadingToParagraph
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        borders = builder.paragraph_format.borders
        borders.distance_from_text = 20
        borders.get_by_border_type(aw.BorderType.LEFT).line_style = aw.LineStyle.DOUBLE
        borders.get_by_border_type(aw.BorderType.RIGHT).line_style = aw.LineStyle.DOUBLE
        borders.get_by_border_type(aw.BorderType.TOP).line_style = aw.LineStyle.DOUBLE
        borders.get_by_border_type(aw.BorderType.BOTTOM).line_style = aw.LineStyle.DOUBLE

        shading = builder.paragraph_format.shading
        shading.texture = aw.TextureIndex.TEXTURE_DIAGONAL_CROSS
        shading.background_pattern_color = drawing.Color.light_coral
        shading.foreground_pattern_color = drawing.Color.light_salmon

        builder.write("I'm a formatted paragraph with double border and nice shading.")

        doc.save(ARTIFACTS_DIR + "DocumentFormatting.apply_borders_and_shading_to_paragraph.doc")
        #ExEnd:ApplyBordersAndShadingToParagraph

    def test_change_asian_paragraph_spacing_and_indents(self):

        #ExStart:ChangeAsianParagraphSpacingAndIndents
        doc = aw.Document(MY_DIR + "Asian typography.docx")

        paragraph_format = doc.first_section.body.first_paragraph.paragraph_format
        paragraph_format.character_unit_left_indent = 10       # ParagraphFormat.left_indent will be updated
        paragraph_format.character_unit_right_indent = 10      # ParagraphFormat.right_indent will be updated
        paragraph_format.character_unit_first_line_indent = 20 # ParagraphFormat.first_line_indent will be updated
        paragraph_format.line_unit_before = 5                  # ParagraphFormat.space_before will be updated
        paragraph_format.line_unit_after = 10                  # ParagraphFormat.space_after will be updated

        doc.save(ARTIFACTS_DIR + "DocumentFormatting.change_asian_paragraph_spacing_and_indents.doc")
        #ExEnd:ChangeAsianParagraphSpacingAndIndents

    def test_snap_to_grid(self):

        #ExStart:SetSnapToGrid
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Optimize the layout when typing in Asian characters.
        par = doc.first_section.body.first_paragraph
        par.paragraph_format.snap_to_grid = True

        builder.writeln("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod " +
                        "tempor incididunt ut labore et dolore magna aliqua.")

        par.runs[0].font.snap_to_grid = True

        doc.save(ARTIFACTS_DIR + "Paragraph.snap_to_grid.docx")
        #ExEnd:SetSnapToGrid

    def test_get_paragraph_style_separator(self):

        #ExStart:GetParagraphStyleSeparator
        doc = aw.Document(MY_DIR + "Document.docx")

        for paragraph in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True):
            paragraph = paragraph.as_paragraph()
            if paragraph.break_is_style_separator:
                print("Separator Found!")
        #ExEnd:GetParagraphStyleSeparator
