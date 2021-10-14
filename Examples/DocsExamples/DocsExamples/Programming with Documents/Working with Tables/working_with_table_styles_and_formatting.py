import unittest
import os
import sys

base_dir = os.path.abspath(os.curdir) + "/"
base_dir = base_dir[:base_dir.find("Aspose.Words-for-Python-via-.NET")]
base_dir = base_dir + "Aspose.Words-for-Python-via-.NET/Examples/DocsExamples/DocsExamples"
sys.path.insert(0, base_dir)

import docs_examples_base as docs_base

import aspose.words as aw
import aspose.pydrawing as drawing

class WorkingWithTableStylesAndFormatting(docs_base.DocsExamplesBase):
    
    def test_get_distance_between_table_surrounding_text(self) :
        
        #ExStart:GetDistancebetweenTableSurroundingText
        doc = aw.Document(docs_base.my_dir + "Tables.docx")

        print("\nGet distance between table left, right, bottom, top and the surrounding text.")
        table = doc.get_child(aw.NodeType.TABLE, 0, True).as_table()

        print(table.distance_top)
        print(table.distance_bottom)
        print(table.distance_right)
        print(table.distance_left)
        #ExEnd:GetDistancebetweenTableSurroundingText
        

    def test_apply_outline_border(self) :
        
        #ExStart:ApplyOutlineBorder
        doc = aw.Document(docs_base.my_dir + "Tables.docx")

        table = doc.get_child(aw.NodeType.TABLE, 0, True).as_table()
        # Align the table to the center of the page.
        table.alignment = aw.tables.TableAlignment.CENTER
        # Clear any existing borders from the table.
        table.clear_borders()

        # Set a green border around the table but not inside.
        table.set_border(aw.BorderType.LEFT, aw.LineStyle.SINGLE, 1.5, drawing.Color.green, True)
        table.set_border(aw.BorderType.RIGHT, aw.LineStyle.SINGLE, 1.5, drawing.Color.green, True)
        table.set_border(aw.BorderType.TOP, aw.LineStyle.SINGLE, 1.5, drawing.Color.green, True)
        table.set_border(aw.BorderType.BOTTOM, aw.LineStyle.SINGLE, 1.5, drawing.Color.green, True)

        # Fill the cells with a light green solid color.
        table.set_shading(aw.TextureIndex.TEXTURE_SOLID, drawing.Color.light_green, drawing.Color.empty())

        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.apply_outline_border.docx")
        #ExEnd:ApplyOutlineBorder
        

    def test_build_table_with_borders(self) :
        
        #ExStart:BuildTableWithBorders
        doc = aw.Document(docs_base.my_dir + "Tables.docx")

        table = doc.get_child(aw.NodeType.TABLE, 0, True).as_table()
            
        # Clear any existing borders from the table.
        table.clear_borders()
            
        # Set a green border around and inside the table.
        table.set_borders(aw.LineStyle.SINGLE, 1.5, drawing.Color.green)

        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.build_table_with_borders.docx")
        #ExEnd:BuildTableWithBorders
        

    def test_modify_row_formatting(self) :
        
        #ExStart:ModifyRowFormatting
        doc = aw.Document(docs_base.my_dir + "Tables.docx")

        table = doc.get_child(aw.NodeType.TABLE, 0, True).as_table()
            
        # Retrieve the first row in the table.
        firstRow = table.first_row
        firstRow.row_format.borders.line_style = aw.LineStyle.NONE
        firstRow.row_format.height_rule = aw.HeightRule.AUTO
        firstRow.row_format.allow_break_across_pages = True
        #ExEnd:ModifyRowFormatting
        

    def test_apply_row_formatting(self) :
        
        #ExStart:ApplyRowFormatting
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        table = builder.start_table()
        builder.insert_cell()

        rowFormat = builder.row_format
        rowFormat.height = 100
        rowFormat.height_rule = aw.HeightRule.EXACTLY
            
        # These formatting properties are set on the table and are applied to all rows in the table.
        table.left_padding = 30
        table.right_padding = 30
        table.top_padding = 30
        table.bottom_padding = 30

        builder.writeln("I'm a wonderful formatted row.")

        builder.end_row()
        builder.end_table()

        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.apply_row_formatting.docx")
        #ExEnd:ApplyRowFormatting
        

    def test_set_cell_padding(self) :
        
        #ExStart:SetCellPadding
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.start_table()
        builder.insert_cell()

        # Sets the amount of space (in points) to add to the left/top/right/bottom of the cell's contents.
        builder.cell_format.set_paddings(30, 50, 30, 50)
        builder.writeln("I'm a wonderful formatted cell.")

        builder.end_row()
        builder.end_table()

        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.set_cell_padding.docx")
        #ExEnd:SetCellPadding
        

    # <summary>
    # Shows how to modify formatting of a table cell.
    # </summary>
    def test_modify_cell_formatting(self) :
        
        #ExStart:ModifyCellFormatting
        doc = aw.Document(docs_base.my_dir + "Tables.docx")
        table = doc.get_child(aw.NodeType.TABLE, 0, True).as_table()

        firstCell = table.first_row.first_cell
        firstCell.cell_format.width = 30
        firstCell.cell_format.orientation = aw.TextOrientation.DOWNWARD
        firstCell.cell_format.shading.foreground_pattern_color = drawing.Color.light_green
        #ExEnd:ModifyCellFormatting
        

    def test_format_table_and_cell_with_different_borders(self) :
        
        #ExStart:FormatTableAndCellWithDifferentBorders
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        table = builder.start_table()
        builder.insert_cell()

        # Set the borders for the entire table.
        table.set_borders(aw.LineStyle.SINGLE, 2.0, drawing.Color.black)
            
        # Set the cell shading for this cell.
        builder.cell_format.shading.background_pattern_color = drawing.Color.red
        builder.writeln("Cell #1")

        builder.insert_cell()
            
        # Specify a different cell shading for the second cell.
        builder.cell_format.shading.background_pattern_color = drawing.Color.green
        builder.writeln("Cell #2")

        builder.end_row()

        # Clear the cell formatting from previous operations.
        builder.cell_format.clear_formatting()

        builder.insert_cell()

        # Create larger borders for the first cell of this row. This will be different
        # compared to the borders set for the table.
        builder.cell_format.borders.left.line_width = 4.0
        builder.cell_format.borders.right.line_width = 4.0
        builder.cell_format.borders.top.line_width = 4.0
        builder.cell_format.borders.bottom.line_width = 4.0
        builder.writeln("Cell #3")

        builder.insert_cell()
        builder.cell_format.clear_formatting()
        builder.writeln("Cell #4")
            
        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.format_table_and_cell_with_different_borders.docx")
        #ExEnd:FormatTableAndCellWithDifferentBorders
        

    def test_set_table_title_and_description(self) :
        
        #ExStart:SetTableTitleAndDescription
        doc = aw.Document(docs_base.my_dir + "Tables.docx")

        table = doc.get_child(aw.NodeType.TABLE, 0, True).as_table()
        table.title = "Test title"
        table.description = "Test description"

        options = aw.saving.OoxmlSaveOptions()
        options.compliance = aw.saving.OoxmlCompliance.ISO29500_2008_STRICT 

        doc.compatibility_options.optimize_for(aw.settings.MsWordVersion.WORD2016)

        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.set_table_title_and_description.docx", options)
        #ExEnd:SetTableTitleAndDescription
        

    def test_allow_cell_spacing(self) :
        
        #ExStart:AllowCellSpacing
        doc = aw.Document(docs_base.my_dir + "Tables.docx")

        table = doc.get_child(aw.NodeType.TABLE, 0, True).as_table()
        table.allow_cell_spacing = True
        table.cell_spacing = 2
            
        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.allow_cell_spacing.docx")
        #ExEnd:AllowCellSpacing
        

    def test_build_table_with_style(self) :
        
        #ExStart:BuildTableWithStyle
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        table = builder.start_table()
            
        # We must insert at least one row first before setting any table formatting.
        builder.insert_cell()

        # Set the table style used based on the unique style identifier.
        table.style_identifier = aw.StyleIdentifier.MEDIUM_SHADING1_ACCENT1
            
        # Apply which features should be formatted by the style.
        table.style_options = aw.tables.TableStyleOptions.FIRST_COLUMN | aw.tables.TableStyleOptions.ROW_BANDS | aw.tables.TableStyleOptions.FIRST_ROW
        table.auto_fit(aw.tables.AutoFitBehavior.AUTO_FIT_TO_CONTENTS)

        builder.writeln("Item")
        builder.cell_format.right_padding = 40
        builder.insert_cell()
        builder.writeln("Quantity (kg)")
        builder.end_row()

        builder.insert_cell()
        builder.writeln("Apples")
        builder.insert_cell()
        builder.writeln("20")
        builder.end_row()

        builder.insert_cell()
        builder.writeln("Bananas")
        builder.insert_cell()
        builder.writeln("40")
        builder.end_row()

        builder.insert_cell()
        builder.writeln("Carrots")
        builder.insert_cell()
        builder.writeln("50")
        builder.end_row()

        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.build_table_with_style.docx")
        #ExEnd:BuildTableWithStyle
        

    def test_expand_formatting_on_cells_and_row_from_style(self) :
        
        #ExStart:ExpandFormattingOnCellsAndRowFromStyle
        doc = aw.Document(docs_base.my_dir + "Tables.docx")

        # Get the first cell of the first table in the document.
        table = doc.get_child(aw.NodeType.TABLE, 0, True).as_table()
        firstCell = table.first_row.first_cell

        # First print the color of the cell shading.
        # This should be empty as the current shading is stored in the table style.
        cellShadingBefore = firstCell.cell_format.shading.background_pattern_color
        print(f"Cell shading before style expansion: {cellShadingBefore}")

        doc.expand_table_styles_to_direct_formatting()

        # Now print the cell shading after expanding table styles.
        # A blue background pattern color should have been applied from the table style.
        cellShadingAfter = firstCell.cell_format.shading.background_pattern_color
        print(f"Cell shading after style expansion: {cellShadingAfter}")
        #ExEnd:ExpandFormattingOnCellsAndRowFromStyle
        

    def test_create_table_style(self) :
        
        #ExStart:CreateTableStyle
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        table = builder.start_table()
        builder.insert_cell()
        builder.write("Name")
        builder.insert_cell()
        builder.write("Value")
        builder.end_row()
        builder.insert_cell()
        builder.insert_cell()
        builder.end_table()

        tableStyle = doc.styles.add(aw.StyleType.TABLE, "MyTableStyle1").as_table_style()
        tableStyle.borders.line_style = aw.LineStyle.DOUBLE
        tableStyle.borders.line_width = 1
        tableStyle.left_padding = 18
        tableStyle.right_padding = 18
        tableStyle.top_padding = 12
        tableStyle.bottom_padding = 12

        table.style = tableStyle

        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.create_table_style.docx")
        #ExEnd:CreateTableStyle
        

    def test_define_conditional_formatting(self) :
        
        #ExStart:DefineConditionalFormatting
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        table = builder.start_table()
        builder.insert_cell()
        builder.write("Name")
        builder.insert_cell()
        builder.write("Value")
        builder.end_row()
        builder.insert_cell()
        builder.insert_cell()
        builder.end_table()

        tableStyle = doc.styles.add(aw.StyleType.TABLE, "MyTableStyle1").as_table_style()
        tableStyle.conditional_styles.first_row.shading.background_pattern_color = drawing.Color.green_yellow
        tableStyle.conditional_styles.first_row.shading.texture = aw.TextureIndex.TEXTURE_NONE

        table.style = tableStyle

        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.define_conditional_formatting.docx")
        #ExEnd:DefineConditionalFormatting
        

    def test_set_table_cell_formatting(self) :
        
        #ExStart:DocumentBuilderSetTableCellFormatting
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.start_table()
        builder.insert_cell()

        cellFormat = builder.cell_format
        cellFormat.width = 250
        cellFormat.left_padding = 30
        cellFormat.right_padding = 30
        cellFormat.top_padding = 30
        cellFormat.bottom_padding = 30

        builder.writeln("I'm a wonderful formatted cell.")

        builder.end_row()
        builder.end_table()

        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.document_builder_set_table_cell_formatting.docx")
        #ExEnd:DocumentBuilderSetTableCellFormatting
        

    def test_set_table_row_formatting(self) :
        
        #ExStart:DocumentBuilderSetTableRowFormatting
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        table = builder.start_table()
        builder.insert_cell()

        rowFormat = builder.row_format
        rowFormat.height = 100
        rowFormat.height_rule = aw.HeightRule.EXACTLY
            
        # These formatting properties are set on the table and are applied to all rows in the table.
        table.left_padding = 30
        table.right_padding = 30
        table.top_padding = 30
        table.bottom_padding = 30

        builder.writeln("I'm a wonderful formatted row.")

        builder.end_row()
        builder.end_table()

        doc.save(docs_base.artifacts_dir + "WorkingWithTableStylesAndFormatting.document_builder_set_table_row_formatting.docx")
        #ExEnd:DocumentBuilderSetTableRowFormatting
        
    

if __name__ == '__main__':
    unittest.main()