import unittest
import io
import uuid
from datetime import datetime

import aspose.words as aw
import aspose.pydrawing as drawing

from api_example_base import ApiExampleBase, my_dir, artifacts_dir, golds_dir
from document_helper import DocumentHelper

MY_DIR = my_dir
ARTIFACTS_DIR = artifacts_dir
GOLDS_DIR = golds_dir

class ExStructuredDocumentTag(ApiExampleBase):

    def test_repeating_section(self):

        #ExStart
        #ExFor:StructuredDocumentTag.sdt_type
        #ExSummary:Shows how to get the type of a structured document tag.
        doc = aw.Document(MY_DIR + "Structured document tags.docx")

        sd_tags = [node.as_structured_document_tag() for node in doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG, True)]

        self.assertEqual(aw.markup.SdtType.REPEATING_SECTION, sd_tags[0].sdt_type)
        self.assertEqual(aw.markup.SdtType.REPEATING_SECTION_ITEM, sd_tags[1].sdt_type)
        self.assertEqual(aw.markup.SdtType.RICH_TEXT, sd_tags[2].sdt_type)
        #ExEnd

    def test_apply_style(self):

        #ExStart
        #ExFor:StructuredDocumentTag
        #ExFor:StructuredDocumentTag.NodeType
        #ExFor:StructuredDocumentTag.Style
        #ExFor:StructuredDocumentTag.StyleName
        #ExFor:MarkupLevel
        #ExFor:SdtType
        #ExSummary:Shows how to work with styles for content control elements.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Below are two ways to apply a style from the document to a structured document tag.
        # 1 -  Apply a style object from the document's style collection:
        quote_style = doc.styles[aw.StyleIdentifier.QUOTE]
        sdt_plain_text = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)
        sdt_plain_text.style = quote_style

        # 2 -  Reference a style in the document by name:
        sdt_rich_text = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.RICH_TEXT, aw.markup.MarkupLevel.INLINE)
        sdt_rich_text.style_name = "Quote"

        builder.insert_node(sdt_plain_text)
        builder.insert_node(sdt_rich_text)

        self.assertEqual(aw.NodeType.STRUCTURED_DOCUMENT_TAG, sdt_plain_text.node_type)

        tags = doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG, True)

        for node in tags:
            sdt = node.as_structured_document_tag()

            self.assertEqual(aw.StyleIdentifier.QUOTE, sdt.style.style_identifier)
            self.assertEqual("Quote", sdt.style_name)

        #ExEnd

    def test_check_box(self):

        #ExStart
        #ExFor:StructuredDocumentTag.#ctor(DocumentBase, SdtType, MarkupLevel)
        #ExFor:StructuredDocumentTag.Checked
        #ExFor:StructuredDocumentTag.SetCheckedSymbol(System.Int32, System.String)
        #ExFor:StructuredDocumentTag.SetUncheckedSymbol(System.Int32, System.String)
        #ExSummary:Show how to create a structured document tag in the form of a check box.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        sdt_check_box = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.CHECKBOX, aw.markup.MarkupLevel.INLINE)
        sdt_check_box.checked = True

        # We can set the symbols used to represent the checked/unchecked state of a checkbox content control.
        sdt_check_box.set_checked_symbol(0x00A9, "Times New Roman")
        sdt_check_box.set_unchecked_symbol(0x00AE, "Times New Roman")

        builder.insert_node(sdt_check_box)

        doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.CheckBox.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "StructuredDocumentTag.CheckBox.docx")

        tags = [node.as_structured_document_tag() for node in doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG, True)]

        self.assertTrue(tags[0].checked)
        self.assertEquals(tags[0].xml_mapping.store_item_id, "")

    def test_date(self):

        #ExStart
        #ExFor:StructuredDocumentTag.CalendarType
        #ExFor:StructuredDocumentTag.DateDisplayFormat
        #ExFor:StructuredDocumentTag.DateDisplayLocale
        #ExFor:StructuredDocumentTag.DateStorageFormat
        #ExFor:StructuredDocumentTag.FullDate
        #ExSummary:Shows how to prompt the user to enter a date with a structured document tag.
        doc = aw.Document()

        # Insert a structured document tag that prompts the user to enter a date.
        # In Microsoft Word, this element is known as a "Date picker content control".
        # When we click on the arrow on the right end of this tag in Microsoft Word,
        # we will see a pop up in the form of a clickable calendar.
        # We can use that popup to select a date that the tag will display.
        sdt_date = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.DATE, aw.markup.MarkupLevel.INLINE)

        # Display the date, according to the Saudi Arabian Arabic locale.
        sdt_date.date_display_locale = 1025 #CultureInfo.get_culture_info("ar-SA").LCID

        # Set the format with which to display the date.
        sdt_date.date_display_format = "dd MMMM, yyyy"
        sdt_date.date_storage_format = aw.markup.SdtDateStorageFormat.DATE_TIME

        # Display the date according to the Hijri calendar.
        sdt_date.calendar_type = aw.markup.SdtCalendarType.HIJRI

        # Before the user chooses a date in Microsoft Word, the tag will display the text "Click here to enter a date.".
        # According to the tag's calendar, set the "full_date" property to get the tag to display a default date.
        sdt_date.full_date = datetime(1440, 10, 20)

        builder = aw.DocumentBuilder(doc)
        builder.insert_node(sdt_date)

        doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.Date.docx")
        #ExEnd

    def test_plain_text(self):

        #ExStart
        #ExFor:StructuredDocumentTag.Color
        #ExFor:StructuredDocumentTag.contents_font
        #ExFor:StructuredDocumentTag.end_character_font
        #ExFor:StructuredDocumentTag.Id
        #ExFor:StructuredDocumentTag.Level
        #ExFor:StructuredDocumentTag.Multiline
        #ExFor:StructuredDocumentTag.Tag
        #ExFor:StructuredDocumentTag.Title
        #ExFor:StructuredDocumentTag.RemoveSelfOnly
        #ExSummary:Shows how to create a structured document tag in a plain text box and modify its appearance.
        doc = aw.Document()

        # Create a structured document tag that will contain plain text.
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)

        # Set the title and color of the frame that appears when you mouse over the structured document tag in Microsoft Word.
        tag.title = "My plain text"
        tag.color = drawing.Color.magenta

        # Set a tag for this structured document tag, which is obtainable
        # as an XML element named "tag", with the string below in its "@val" attribute.
        tag.tag = "MyPlainTextSDT"

        # Every structured document tag has a random unique ID.
        self.assertGreater(tag.id, 0)

        # Set the font for the text inside the structured document tag.
        tag.contents_font.name = "Arial"

        # Set the font for the text at the end of the structured document tag.
        # Any text that we type in the document body after moving out of the tag with arrow keys will use this font.
        tag.end_character_font.name = "Arial Black"

        # By default, this is false and pressing enter while inside a structured document tag does nothing.
        # When set to true, our structured document tag can have multiple lines.

        # Set the "multiline" property to "False" to only allow the contents
        # of this structured document tag to span a single line.
        # Set the "multiline" property to "True" to allow the tag to contain multiple lines of content.
        tag.multiline = True

        builder = aw.DocumentBuilder(doc)
        builder.insert_node(tag)

        # Insert a clone of our structured document tag in a new paragraph.
        tag_clone = tag.clone(True).as_structured_document_tag()
        builder.insert_paragraph()
        builder.insert_node(tag_clone)

        # Use the "remove_self_only" method to remove a structured document tag, while keeping its contents in the document.
        tag_clone.remove_self_only()

        doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.PlainText.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "StructuredDocumentTag.PlainText.docx")
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()

        self.assertEqual("My plain text", tag.title)
        self.assertEqual(drawing.Color.magenta.to_argb(), tag.color.to_argb())
        self.assertEqual("MyPlainTextSDT", tag.tag)
        self.assertGreater(tag.id, 0)
        self.assertEqual("Arial", tag.contents_font.name)
        self.assertEqual("Arial Black", tag.end_character_font.name)
        self.assertTrue(tag.multiline)

    def test_is_temporary(self):

        for is_temporary in (False, True):
            with self.subTest(is_temporary=is_temporary):
                #ExStart
                #ExFor:StructuredDocumentTag.IsTemporary
                #ExSummary:Shows how to make single-use controls.
                doc = aw.Document()

                # Insert a plain text structured document tag,
                # which will act as a plain text form that the user may enter text into.
                tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)

                # Set the "is_temporary" property to "True" to make the structured document tag disappear and
                # assimilate its contents into the document after the user edits it once in Microsoft Word.
                # Set the "is_temporary" property to "False" to allow the user to edit the contents
                # of the structured document tag any number of times.
                tag.is_temporary = is_temporary

                builder = aw.DocumentBuilder(doc)
                builder.write("Please enter text: ")
                builder.insert_node(tag)

                # Insert another structured document tag in the form of a check box and set its default state to "checked".
                tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.CHECKBOX, aw.markup.MarkupLevel.INLINE)
                tag.checked = True

                # Set the "is_temporary" property to "True" to make the check box become a symbol
                # once the user clicks on it in Microsoft Word.
                # Set the "is_temporary" property to "False" to allow the user to click on the check box any number of times.
                tag.is_temporary = is_temporary

                builder.write("\nPlease click the check box: ")
                builder.insert_node(tag)

                doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.IsTemporary.docx")
                #ExEnd

                doc = aw.Document(ARTIFACTS_DIR + "StructuredDocumentTag.IsTemporary.docx")

                self.assertEqual(2, len([sdt.as_structured_document_tag().is_temporary == is_temporary for sdt in doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG, True)]))

    def test_placeholder_building_block(self):

        for is_showing_placeholder_text in (False, True):
            with self.subTest(is_showing_placeholder_text=is_showing_placeholder_text):
                #ExStart
                #ExFor:StructuredDocumentTag.IsShowingPlaceholderText
                #ExFor:StructuredDocumentTag.Placeholder
                #ExFor:StructuredDocumentTag.placeholder_name
                #ExSummary:Shows how to use a building block's contents as a custom placeholder text for a structured document tag.
                doc = aw.Document()

                # Insert a plain text structured document tag of the "PlainText" type, which will function as a text box.
                # The contents that it will display by default are a "Click here to enter text." prompt.
                tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)

                # We can get the tag to display the contents of a building block instead of the default text.
                # First, add a building block with contents to the glossary document.
                glossary_doc = doc.glossary_document

                substitute_block = aw.buildingblocks.BuildingBlock(glossary_doc)
                substitute_block.name = "Custom Placeholder"
                substitute_block.append_child(aw.Section(glossary_doc))
                substitute_block.first_section.append_child(aw.Body(glossary_doc))
                substitute_block.first_section.body.append_paragraph("Custom placeholder text.")

                glossary_doc.append_child(substitute_block)

                # Then, use the structured document tag's "placeholder_name" property to reference that building block by name.
                tag.placeholder_name = "Custom Placeholder"

                # If "placeholder_name" refers to an existing block in the parent document's glossary document,
                # we will be able to verify the building block via the "placeholder" property.
                self.assertEqual(substitute_block, tag.placeholder)

                # Set the "is_showing_placeholder_text" property to "True" to treat the
                # structured document tag's current contents as placeholder text.
                # This means that clicking on the text box in Microsoft Word will immediately highlight all the tag's contents.
                # Set the "is_showing_placeholder_text" property to "False" to get the
                # structured document tag to treat its contents as text that a user has already entered.
                # Clicking on this text in Microsoft Word will place the blinking cursor at the clicked location.
                tag.is_showing_placeholder_text = is_showing_placeholder_text

                builder = aw.DocumentBuilder(doc)
                builder.insert_node(tag)

                doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.PlaceholderBuildingBlock.docx")
                #ExEnd

                doc = aw.Document(ARTIFACTS_DIR + "StructuredDocumentTag.PlaceholderBuildingBlock.docx")
                tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
                substitute_block = doc.glossary_document.get_child(aw.NodeType.BUILDING_BLOCK, 0, True).as_building_block()

                self.assertEqual("Custom Placeholder", substitute_block.name)
                self.assertEqual(is_showing_placeholder_text, tag.is_showing_placeholder_text)
                self.assertEqual(substitute_block, tag.placeholder)
                self.assertEqual(substitute_block.name, tag.placeholder_name)

    def test_lock(self):

        #ExStart
        #ExFor:StructuredDocumentTag.lock_content_control
        #ExFor:StructuredDocumentTag.lock_contents
        #ExSummary:Shows how to apply editing restrictions to structured document tags.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        # Insert a plain text structured document tag, which acts as a text box that prompts the user to fill it in.
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)

        # Set the "lock_contents" property to "True" to prohibit the user from editing this text box's contents.
        tag.lock_contents = True
        builder.write("The contents of this structured document tag cannot be edited: ")
        builder.insert_node(tag)

        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.INLINE)

        # Set the "lock_content_control" property to "True" to prohibit the user from
        # deleting this structured document tag manually in Microsoft Word.
        tag.lock_content_control = True

        builder.insert_paragraph()
        builder.write("This structured document tag cannot be deleted but its contents can be edited: ")
        builder.insert_node(tag)

        doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.Lock.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "StructuredDocumentTag.Lock.docx")
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()

        self.assertTrue(tag.lock_contents)
        self.assertFalse(tag.lock_content_control)

        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 1, True).as_structured_document_tag()

        self.assertFalse(tag.lock_contents)
        self.assertTrue(tag.lock_content_control)

    def test_list_item_collection(self):

        #ExStart
        #ExFor:SdtListItem
        #ExFor:SdtListItem.#ctor(System.String)
        #ExFor:SdtListItem.#ctor(System.String,System.String)
        #ExFor:SdtListItem.DisplayText
        #ExFor:SdtListItem.Value
        #ExFor:SdtListItemCollection
        #ExFor:SdtListItemCollection.Add(Aspose.Words.Markup.SdtListItem)
        #ExFor:SdtListItemCollection.Clear
        #ExFor:SdtListItemCollection.count
        #ExFor:SdtListItemCollection.GetEnumerator
        #ExFor:SdtListItemCollection.Item(System.Int32)
        #ExFor:SdtListItemCollection.RemoveAt(System.Int32)
        #ExFor:SdtListItemCollection.SelectedValue
        #ExFor:StructuredDocumentTag.list_items
        #ExSummary:Shows how to work with drop down-list structured document tags.
        doc = aw.Document()
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.DROP_DOWN_LIST, aw.markup.MarkupLevel.BLOCK)
        doc.first_section.body.append_child(tag)

        # A drop-down list structured document tag is a form that allows the user to
        # select an option from a list by left-clicking and opening the form in Microsoft Word.
        # The "list_items" property contains all list items, and each list item is an "SdtListItem".
        list_items = tag.list_items
        list_items.add(aw.markup.SdtListItem("Value 1"))

        self.assertEqual(list_items[0].display_text, list_items[0].value)

        # Add 3 more list items. Initialize these items using a different constructor to the first item
        # to display strings that are different from their values.
        list_items.add(aw.markup.SdtListItem("Item 2", "Value 2"))
        list_items.add(aw.markup.SdtListItem("Item 3", "Value 3"))
        list_items.add(aw.markup.SdtListItem("Item 4", "Value 4"))

        self.assertEqual(4, list_items.count)

        # The drop-down list is displaying the first item. Assign a different list item to the "selected_value" to display it.
        list_items.selected_value = list_items[3]

        self.assertEqual("Value 4", list_items.selected_value.value)

        # Enumerate over the collection and print each element.
        for item in list_items:
            if item is not None:
                print(f"List item: {item.display_text}, value: {item.value}")

        # Remove the last list item.
        list_items.remove_at(3)

        self.assertEqual(3, list_items.count)

        # Since our drop-down control is set to display the removed item by default, give it an item to display which exists.
        list_items.selected_value = list_items[1]

        doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.ListItemCollection.docx")

        # Use the "clear" method to empty the entire drop-down item collection at once.
        list_items.clear()

        self.assertEqual(0, list_items.count)
        #ExEnd

    def test_creating_custom_xml(self):

        #ExStart
        #ExFor:CustomXmlPart
        #ExFor:CustomXmlPart.Clone
        #ExFor:CustomXmlPart.Data
        #ExFor:CustomXmlPart.Id
        #ExFor:CustomXmlPart.Schemas
        #ExFor:CustomXmlPartCollection
        #ExFor:CustomXmlPartCollection.Add(CustomXmlPart)
        #ExFor:CustomXmlPartCollection.Add(String, String)
        #ExFor:CustomXmlPartCollection.Clear
        #ExFor:CustomXmlPartCollection.Clone
        #ExFor:CustomXmlPartCollection.count
        #ExFor:CustomXmlPartCollection.GetById(String)
        #ExFor:CustomXmlPartCollection.GetEnumerator
        #ExFor:CustomXmlPartCollection.Item(Int32)
        #ExFor:CustomXmlPartCollection.RemoveAt(Int32)
        #ExFor:Document.custom_xml_parts
        #ExFor:StructuredDocumentTag.XmlMapping
        #ExFor:XmlMapping.SetMapping(CustomXmlPart, String, String)
        #ExSummary:Shows how to create a structured document tag with custom XML data.
        doc = aw.Document()

        # Construct an XML part that contains data and add it to the document's collection.
        # If we enable the "Developer" tab in Microsoft Word,
        # we can find elements from this collection in the "XML Mapping Pane", along with a few default elements.
        xml_part_id = str(uuid.uuid4())
        xml_part_content = "<root><text>Hello world!</text></root>"
        xml_part = doc.custom_xml_parts.add(xml_part_id, xml_part_content)

        self.assertEqual(xml_part_content.encode('ascii'), xml_part.data)
        self.assertEqual(xml_part_id, xml_part.id)

        # Below are two ways to refer to XML parts.
        # 1 -  By an index in the custom XML part collection:
        self.assertEqual(xml_part, doc.custom_xml_parts[0])

        # 2 -  By GUID:
        self.assertEqual(xml_part, doc.custom_xml_parts.get_by_id(xml_part_id))

        # Add an XML schema association.
        xml_part.schemas.add("http://www.w3.org/2001/XMLSchema")

        # Clone a part, and then insert it into the collection.
        xml_part_clone = xml_part.clone()
        xml_part_clone.id = str(uuid.uuid4())
        doc.custom_xml_parts.add(xml_part_clone)

        self.assertEqual(2, doc.custom_xml_parts.count)

        # Iterate through the collection and print the contents of each part.
        for index, part in enumerate(doc.custom_xml_parts):
            print(f"XML part index {index}, ID: {part.id}")
            print(f"\tContent: {part.data.decode('utf-8')}")

        # Use the "remove_at" method to remove the cloned part by index.
        doc.custom_xml_parts.remove_at(1)

        self.assertEqual(1, doc.custom_xml_parts.count)

        # Clone the XML parts collection, and then use the "Clear" method to remove all its elements at once.
        custom_xml_parts = doc.custom_xml_parts.clone()
        custom_xml_parts.clear()

        # Create a structured document tag that will display our part's contents and insert it into the document body.
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.BLOCK)
        tag.xml_mapping.set_mapping(xml_part, "/root[1]/text[1]", "")

        doc.first_section.body.append_child(tag)

        doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.CustomXml.docx")
        #ExEnd

        self.assertTrue(DocumentHelper.compare_docs(ARTIFACTS_DIR + "StructuredDocumentTag.CustomXml.docx", GOLDS_DIR + "StructuredDocumentTag.CustomXml Gold.docx"))

        doc = aw.Document(ARTIFACTS_DIR + "StructuredDocumentTag.CustomXml.docx")
        xml_part = doc.custom_xml_parts[0]

        xml_part_id = uuid.UUID(xml_part.id)
        self.assertEqual("<root><text>Hello world!</text></root>", xml_part.data.decode('utf-8'))
        self.assertEqual("http://www.w3.org/2001/XMLSchema", xml_part.schemas[0])

        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual("Hello world!", tag.get_text().strip())
        self.assertEqual("/root[1]/text[1]", tag.xml_mapping.xpath)
        self.assertEqual("", tag.xml_mapping.prefix_mappings)
        self.assertEqual(xml_part.data_checksum, tag.xml_mapping.custom_xml_part.data_checksum)

    def test_data_checksum(self):

        #ExStart
        #ExFor:CustomXmlPart.DataChecksum
        #ExSummary:Shows how the checksum is calculated in a runtime.
        doc = aw.Document()

        rich_text = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.RICH_TEXT, aw.markup.MarkupLevel.BLOCK)
        doc.first_section.body.append_child(rich_text)

        # The checksum is read-only and computed using the data of the corresponding custom XML data part.
        rich_text.xml_mapping.set_mapping(doc.custom_xml_parts.add(str(uuid.uuid4()),
            "<root><text>ContentControl</text></root>"), "/root/text", "")

        checksum = rich_text.xml_mapping.custom_xml_part.data_checksum
        print(checksum)

        rich_text.xml_mapping.set_mapping(doc.custom_xml_parts.add(str(uuid.uuid4()),
            "<root><text>Updated ContentControl</text></root>"), "/root/text", "")

        updated_checksum = rich_text.xml_mapping.custom_xml_part.data_checksum
        print(updated_checksum)

        # We changed the XmlPart of the tag, and the checksum was updated at runtime.
        self.assertNotEqual(checksum, updated_checksum)
        #ExEnd

    def test_xml_mapping(self):

        #ExStart
        #ExFor:XmlMapping
        #ExFor:XmlMapping.CustomXmlPart
        #ExFor:XmlMapping.Delete
        #ExFor:XmlMapping.IsMapped
        #ExFor:XmlMapping.PrefixMappings
        #ExFor:XmlMapping.XPath
        #ExSummary:Shows how to set XML mappings for custom XML parts.
        doc = aw.Document()

        # Construct an XML part that contains text and add it to the document's CustomXmlPart collection.
        xml_part_id = str(uuid.uuid4())
        xml_part_content = "<root><text>Text element #1</text><text>Text element #2</text></root>"
        xml_part = doc.custom_xml_parts.add(xml_part_id, xml_part_content)

        self.assertEqual("<root><text>Text element #1</text><text>Text element #2</text></root>", xml_part.data.decode('utf-8'))

        # Create a structured document tag that will display the contents of our CustomXmlPart.
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.BLOCK)

        # Set a mapping for our structured document tag. This mapping will instruct
        # our structured document tag to display a portion of the XML part's text contents that the XPath points to.
        # In this case, it will be contents of the the second "<text>" element of the first "<root>" element: "Text element #2".
        tag.xml_mapping.set_mapping(xml_part, "/root[1]/text[2]", "xmlns:ns='http://www.w3.org/2001/XMLSchema'")

        self.assertTrue(tag.xml_mapping.is_mapped)
        self.assertEqual(xml_part, tag.xml_mapping.custom_xml_part)
        self.assertEqual("/root[1]/text[2]", tag.xml_mapping.xpath)
        self.assertEqual("xmlns:ns='http://www.w3.org/2001/XMLSchema'", tag.xml_mapping.prefix_mappings)

        # Add the structured document tag to the document to display the content from our custom part.
        doc.first_section.body.append_child(tag)
        doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.xml_mapping.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "StructuredDocumentTag.xml_mapping.docx")
        xml_part = doc.custom_xml_parts[0]

        xml_part_id = uuid.UUID(xml_part.id)
        self.assertEqual("<root><text>Text element #1</text><text>Text element #2</text></root>", xml_part.data.decode('utf-8'))

        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        self.assertEqual("Text element #2", tag.get_text().strip())
        self.assertEqual("/root[1]/text[2]", tag.xml_mapping.xpath)
        self.assertEqual("xmlns:ns='http://www.w3.org/2001/XMLSchema'", tag.xml_mapping.prefix_mappings)

    def test_structured_document_tag_range_start_xml_mapping(self):

        #ExStart
        #ExFor:StructuredDocumentTagRangeStart.XmlMapping
        #ExSummary:Shows how to set XML mappings for the range start of a structured document tag.
        doc = aw.Document(MY_DIR + "Multi-section structured document tags.docx")

        # Construct an XML part that contains text and add it to the document's CustomXmlPart collection.
        xml_part_id = str(uuid.uuid4())
        xml_part_content = "<root><text>Text element #1</text><text>Text element #2</text></root>"
        xml_part = doc.custom_xml_parts.add(xml_part_id, xml_part_content)

        self.assertEqual("<root><text>Text element #1</text><text>Text element #2</text></root>", xml_part.data.decode('utf-8'))

        # Create a structured document tag that will display the contents of our CustomXmlPart in the document.
        sdt_range_start = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, 0, True).as_structured_document_tag_range_start()

        # If we set a mapping for our structured document tag,
        # it will only display a portion of the CustomXmlPart that the XPath points to.
        # This XPath will point to the contents second "<text>" element of the first "<root>" element of our CustomXmlPart.
        sdt_range_start.xml_mapping.set_mapping(xml_part, "/root[1]/text[2]", None)

        doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.StructuredDocumentTagRangeStartXmlMapping.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "StructuredDocumentTag.StructuredDocumentTagRangeStartXmlMapping.docx")
        xml_part = doc.custom_xml_parts[0]

        xml_part_id = uuid.UUID(xml_part.id)
        self.assertEqual("<root><text>Text element #1</text><text>Text element #2</text></root>", xml_part.data.decode('utf-8'))

        sdt_range_start = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, 0, True).as_structured_document_tag_range_start()
        self.assertEqual("/root[1]/text[2]", sdt_range_start.xml_mapping.xpath)

    def test_custom_xml_schema_collection(self):

        #ExStart
        #ExFor:CustomXmlSchemaCollection
        #ExFor:CustomXmlSchemaCollection.Add(System.String)
        #ExFor:CustomXmlSchemaCollection.Clear
        #ExFor:CustomXmlSchemaCollection.Clone
        #ExFor:CustomXmlSchemaCollection.count
        #ExFor:CustomXmlSchemaCollection.GetEnumerator
        #ExFor:CustomXmlSchemaCollection.IndexOf(System.String)
        #ExFor:CustomXmlSchemaCollection.Item(System.Int32)
        #ExFor:CustomXmlSchemaCollection.Remove(System.String)
        #ExFor:CustomXmlSchemaCollection.RemoveAt(System.Int32)
        #ExSummary:Shows how to work with an XML schema collection.
        doc = aw.Document()

        xml_part_id = str(uuid.uuid4())
        xml_part_content = "<root><text>Hello, World!</text></root>"
        xml_part = doc.custom_xml_parts.add(xml_part_id, xml_part_content)

        # Add an XML schema association.
        xml_part.schemas.add("http://www.w3.org/2001/XMLSchema")

        # Clone the custom XML part's XML schema association collection,
        # and then add a couple of new schemas to the clone.
        schemas = xml_part.schemas.clone()
        schemas.add("http://www.w3.org/2001/XMLSchema-instance")
        schemas.add("http://schemas.microsoft.com/office/2006/metadata/contentType")

        self.assertEqual(3, schemas.count)
        self.assertEqual(2, schemas.index_of("http://schemas.microsoft.com/office/2006/metadata/contentType"))

        # Enumerate the schemas and print each element.
        for schema in schemas:
            print(schema)

        # Below are three ways of removing schemas from the collection.
        # 1 -  Remove a schema by index:
        schemas.remove_at(2)

        # 2 -  Remove a schema by value:
        schemas.remove("http://www.w3.org/2001/XMLSchema")

        # 3 -  Use the "clear" method to empty the collection at once.
        schemas.clear()

        self.assertEqual(0, schemas.count)
        #ExEnd

    def test_custom_xml_part_store_item_id_read_only(self):

        #ExStart
        #ExFor:XmlMapping.StoreItemId
        #ExSummary:Shows how to get the custom XML data identifier of an XML part.
        doc = aw.Document(MY_DIR + "Custom XML part in structured document tag.docx")

        # Structured document tags have IDs in the form of GUIDs.
        tag = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()

        self.assertEqual("{F3029283-4FF8-4DD2-9F31-395F19ACEE85}", tag.xml_mapping.store_item_id)
        #ExEnd

    def test_custom_xml_part_store_item_id_read_only_null(self):

        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        sdt_check_box = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.CHECKBOX, aw.markup.MarkupLevel.INLINE)
        sdt_check_box.checked = True

        builder.insert_node(sdt_check_box)

        doc = DocumentHelper.save_open(doc)

        sdt = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()
        print("The Id of your custom xml part is:", sdt.xml_mapping.store_item_id)

    def test_clear_text_from_structured_document_tags(self):

        #ExStart
        #ExFor:StructuredDocumentTag.Clear
        #ExSummary:Shows how to delete contents of structured document tag elements.
        doc = aw.Document()

        # Create a plain text structured document tag, and then append it to the document.
        tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.BLOCK)
        doc.first_section.body.append_child(tag)

        # This structured document tag, which is in the form of a text box, already displays placeholder text.
        self.assertEqual("Click here to enter text.", tag.get_text().strip())
        self.assertTrue(tag.is_showing_placeholder_text)

        # Create a building block with text contents.
        glossary_doc = doc.glossary_document
        substitute_block = aw.buildingblocks.BuildingBlock(glossary_doc)
        substitute_block.name = "My placeholder"
        substitute_block.append_child(aw.Section(glossary_doc))
        substitute_block.first_section.ensure_minimum()
        substitute_block.first_section.body.first_paragraph.append_child(aw.Run(glossary_doc, "Custom placeholder text."))
        glossary_doc.append_child(substitute_block)

        # Set the structured document tag's "placeholder_name" property to our building block's name to get
        # the structured document tag to display the contents of the building block in place of the original default text.
        tag.placeholder_name = "My placeholder"

        self.assertEqual("Custom placeholder text.", tag.get_text().strip())
        self.assertTrue(tag.is_showing_placeholder_text)

        # Edit the text of the structured document tag and hide the placeholder text.
        run = tag.get_child(aw.NodeType.RUN, 0, True).as_run()
        run.text = "New text."
        tag.is_showing_placeholder_text = False

        self.assertEqual("New text.", tag.get_text().strip())

        # Use the "Clear" method to clear this structured document tag's contents and display the placeholder again.
        tag.clear()

        self.assertTrue(tag.is_showing_placeholder_text)
        self.assertEqual("Custom placeholder text.", tag.get_text().strip())
        #ExEnd

    def test_access_to_building_block_properties_from_doc_part_obj_sdt(self):

        doc = aw.Document(MY_DIR + "Structured document tags with building blocks.docx")

        doc_part_obj_sdt = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()

        self.assertEqual(aw.markup.SdtType.DOC_PART_OBJ, doc_part_obj_sdt.sdt_type)
        self.assertEqual("Table of Contents", doc_part_obj_sdt.building_block_gallery)

    def test_access_to_building_block_properties_from_plain_text_sdt(self):

        doc = aw.Document(MY_DIR + "Structured document tags with building blocks.docx")

        plain_text_sdt = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 1, True).as_structured_document_tag()

        self.assertEqual(aw.markup.SdtType.PLAIN_TEXT, plain_text_sdt.sdt_type)
        with self.assertRaises(Exception, msg="BuildingBlockType is only accessible for BuildingBlockGallery SDT type."):
            building_block_gallery = plain_text_sdt.building_block_gallery

    def test_building_block_categories(self):

        #ExStart
        #ExFor:StructuredDocumentTag.BuildingBlockCategory
        #ExFor:StructuredDocumentTag.BuildingBlockGallery
        #ExSummary:Shows how to insert a structured document tag as a building block, and set its category and gallery.
        doc = aw.Document()

        building_block_sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.BUILDING_BLOCK_GALLERY, aw.markup.MarkupLevel.BLOCK)
        building_block_sdt.building_block_category = "Built-in"
        building_block_sdt.building_block_gallery = "Table of Contents"

        doc.first_section.body.append_child(building_block_sdt)

        doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.BuildingBlockCategories.docx")
        #ExEnd

        building_block_sdt = doc.first_section.body.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG, 0, True).as_structured_document_tag()

        self.assertEqual(aw.markup.SdtType.BUILDING_BLOCK_GALLERY, building_block_sdt.sdt_type)
        self.assertEqual("Table of Contents", building_block_sdt.building_block_gallery)
        self.assertEqual("Built-in", building_block_sdt.building_block_category)

    def test_update_sdt_content(self):

        for update_sdt_content in (False, True):
            with self.subTest(update_sdt_content=update_sdt_content):
                #ExStart
                #ExFor:SaveOptions.UpdateSdtContent
                #ExSummary:Shows how to update structured document tags while saving a document to PDF.
                doc = aw.Document()

                # Insert a drop-down list structured document tag.
                tag = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.DROP_DOWN_LIST, aw.markup.MarkupLevel.BLOCK)
                tag.list_items.add(aw.markup.SdtListItem("Value 1"))
                tag.list_items.add(aw.markup.SdtListItem("Value 2"))
                tag.list_items.add(aw.markup.SdtListItem("Value 3"))

                # The drop-down list currently displays "Choose an item" as the default text.
                # Set the "selected_value" property to one of the list items to get the tag to
                # display that list item's value instead of the default text.
                tag.list_items.selected_value = tag.list_items[1]

                doc.first_section.body.append_child(tag)

                # Create a "PdfSaveOptions" object to pass to the document's "Save" method
                # to modify how that method saves the document to .PDF.
                options = aw.saving.PdfSaveOptions()

                # Set the "update_sdt_content" property to "False" not to update the structured document tags
                # while saving the document to PDF. They will display their default values as they were at the time of construction.
                # Set the "update_sdt_content" property to "True" to make sure the tags display updated values in the PDF.
                options.update_sdt_content = update_sdt_content

                doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.UpdateSdtContent.pdf", options)
                #ExEnd

                #pdf_doc = aspose.pdf.Document(ARTIFACTS_DIR + "StructuredDocumentTag.UpdateSdtContent.pdf")
                #text_absorber = aspose.pdf.text.TextAbsorber()
                #text_absorber.visit(pdf_doc)

                #self.assertEqual(
                #    "Value 2" if update_sdt_content else "Choose an item.",
                #    text_absorber.text)

    def test_fill_table_using_repeating_section_item(self):

        #ExStart
        #ExFor:SdtType
        #ExSummary:Shows how to fill a table with data from in an XML part.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        xml_part = doc.custom_xml_parts.add("Books",
            "<books>" +
                "<book>" +
                    "<title>Everyday Italian</title>" +
                    "<author>Giada De Laurentiis</author>" +
                "</book>" +
                "<book>" +
                    "<title>The C Programming Language</title>" +
                    "<author>Brian W. Kernighan, Dennis M. Ritchie</author>" +
                "</book>" +
                "<book>" +
                    "<title>Learning XML</title>" +
                    "<author>Erik T. Ray</author>" +
                "</book>" +
            "</books>")

        # Create headers for data from the XML content.
        table = builder.start_table()
        builder.insert_cell()
        builder.write("Title")
        builder.insert_cell()
        builder.write("Author")
        builder.end_row()
        builder.end_table()

        # Create a table with a repeating section inside.
        repeating_section_sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.REPEATING_SECTION, aw.markup.MarkupLevel.ROW)
        repeating_section_sdt.xml_mapping.set_mapping(xml_part, "/books[1]/book", "")
        table.append_child(repeating_section_sdt)

        # Add repeating section item inside the repeating section and mark it as a row.
        # This table will have a row for each element that we can find in the XML document
        # using the "/books[1]/book" XPath, of which there are three.
        repeating_section_item_sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.REPEATING_SECTION_ITEM, aw.markup.MarkupLevel.ROW)
        repeating_section_sdt.append_child(repeating_section_item_sdt)

        row = aw.tables.Row(doc)
        repeating_section_item_sdt.append_child(row)

        # Map XML data with created table cells for the title and author of each book.
        title_sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.CELL)
        title_sdt.xml_mapping.set_mapping(xml_part, "/books[1]/book[1]/title[1]", "")
        row.append_child(title_sdt)

        author_sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.CELL)
        author_sdt.xml_mapping.set_mapping(xml_part, "/books[1]/book[1]/author[1]", "")
        row.append_child(author_sdt)

        doc.save(ARTIFACTS_DIR + "StructuredDocumentTag.RepeatingSectionItem.docx")
		#ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "StructuredDocumentTag.RepeatingSectionItem.docx")
        tags = [node.as_structured_document_tag() for node in doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG, True)]

        self.assertEqual("/books[1]/book", tags[0].xml_mapping.xpath)
        self.assertEqual("", tags[0].xml_mapping.prefix_mappings)

        self.assertEqual("", tags[1].xml_mapping.xpath)
        self.assertEqual("", tags[1].xml_mapping.prefix_mappings)

        self.assertEqual("/books[1]/book[1]/title[1]", tags[2].xml_mapping.xpath)
        self.assertEqual("", tags[2].xml_mapping.prefix_mappings)

        self.assertEqual("/books[1]/book[1]/author[1]", tags[3].xml_mapping.xpath)
        self.assertEqual("", tags[3].xml_mapping.prefix_mappings)

        self.assertEqual("Title\u0007Author\u0007\u0007" +
                        "Everyday Italian\u0007Giada De Laurentiis\u0007\u0007" +
                        "The C Programming Language\u0007Brian W. Kernighan, Dennis M. Ritchie\u0007\u0007" +
                        "Learning XML\u0007Erik T. Ray\u0007\u0007", doc.first_section.body.tables[0].get_text().strip())

    def test_custom_xml_part(self):

        xml_string = ("<?xml version=\"1.0\"?>" +
            "<Company>" +
                "<Employee id=\"1\">" +
                    "<FirstName>John</FirstName>" +
                    "<LastName>Doe</LastName>" +
                "</Employee>" +
                "<Employee id=\"2\">" +
                    "<FirstName>Jane</FirstName>" +
                    "<LastName>Doe</LastName>" +
                "</Employee>" +
            "</Company>")

        doc = aw.Document()

        # Insert the full XML document as a custom document part.
        # We can find the mapping for this part in Microsoft Word via "Developer" -> "XML Mapping Pane", if it is enabled.
        xml_part = doc.custom_xml_parts.add(str(uuid.uuid4()), xml_string)

        # Create a structured document tag, which will use an XPath to refer to a single element from the XML.
        sdt = aw.markup.StructuredDocumentTag(doc, aw.markup.SdtType.PLAIN_TEXT, aw.markup.MarkupLevel.BLOCK)
        sdt.xml_mapping.set_mapping(xml_part, "Company//Employee[@id='2']/FirstName", "")

        # Add the StructuredDocumentTag to the document to display the element in the text.
        doc.first_section.body.append_child(sdt)

    def test_multi_section_tags(self):

        #ExStart
        #ExFor:StructuredDocumentTagRangeStart
        #ExFor:StructuredDocumentTagRangeStart.Id
        #ExFor:StructuredDocumentTagRangeStart.Title
        #ExFor:StructuredDocumentTagRangeStart.placeholder_name
        #ExFor:StructuredDocumentTagRangeStart.IsShowingPlaceholderText
        #ExFor:StructuredDocumentTagRangeStart.lock_content_control
        #ExFor:StructuredDocumentTagRangeStart.lock_contents
        #ExFor:StructuredDocumentTagRangeStart.Level
        #ExFor:StructuredDocumentTagRangeStart.RangeEnd
        #ExFor:StructuredDocumentTagRangeStart.Color
        #ExFor:StructuredDocumentTagRangeStart.sdt_type
        #ExFor:StructuredDocumentTagRangeStart.Tag
        #ExFor:StructuredDocumentTagRangeEnd
        #ExFor:StructuredDocumentTagRangeEnd.Id
        #ExSummary:Shows how to get the properties of multi-section structured document tags.
        doc = aw.Document(MY_DIR + "Multi-section structured document tags.docx")

        range_start_tag = doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, True)[0].as_structured_document_tag_range_start()
        range_end_tag = doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_END, True)[0].as_structured_document_tag_range_end()

        self.assertEqual(range_start_tag.id, range_end_tag.id) #ExSkip
        self.assertEqual(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, range_start_tag.node_type) #ExSkip
        self.assertEqual(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_END, range_end_tag.node_type) #ExSkip

        print("StructuredDocumentTagRangeStart values:")
        print(f"\t|id: {range_start_tag.id}")
        print(f"\t|title: {range_start_tag.title}")
        print(f"\t|placeholder_name: {range_start_tag.placeholder_name}")
        print(f"\t|is_showing_placeholder_text: {range_start_tag.is_showing_placeholder_text}")
        print(f"\t|lock_content_control: {range_start_tag.lock_content_control}")
        print(f"\t|lock_contents: {range_start_tag.lock_contents}")
        print(f"\t|level: {range_start_tag.level}")
        print(f"\t|node_type: {range_start_tag.node_type}")
        print(f"\t|range_end: {range_start_tag.range_end}")
        print(f"\t|color: {range_start_tag.color.to_argb()}")
        print(f"\t|sdt_type: {range_start_tag.sdt_type}")
        print(f"\t|tag: {range_start_tag.tag}\n")

        print("StructuredDocumentTagRangeEnd values:")
        print(f"\t|id: {range_end_tag.id}")
        print(f"\t|node_type: {range_end_tag.node_type}")
        #ExEnd

    def test_sdt_child_nodes(self):

        #ExStart
        #ExFor:StructuredDocumentTagRangeStart.ChildNodes
        #ExFor:StructuredDocumentTagRangeStart.GetChildNodes(NodeType, bool)
        #ExSummary:Shows how to get child nodes of StructuredDocumentTagRangeStart.
        doc = aw.Document(MY_DIR + "Multi-section structured document tags.docx")
        tag = doc.get_child_nodes(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, True)[0].as_structured_document_tag_range_start()

        print("StructuredDocumentTagRangeStart values:")
        print(f"\t|Child nodes count: {tag.child_nodes.count}\n")

        for node in tag.child_nodes:
            print(f"\t|Child node type: {node.node_type}")

        for node in tag.get_child_nodes(aw.NodeType.RUN, True):
            print(f"\t|Child node text: {node.get_text()}")
        #ExEnd

    #ExStart
    #ExFor:StructuredDocumentTagRangeStart.#ctor(DocumentBase, SdtType)
    #ExFor:StructuredDocumentTagRangeEnd.#ctor(DocumentBase, int)
    #ExFor:StructuredDocumentTagRangeStart.RemoveSelfOnly
    #ExFor:StructuredDocumentTagRangeStart.RemoveAllChildren
    #ExSummary:Shows how to create/remove structured document tag and its content.
    def test_sdt_range_extended_methods(self):

        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.writeln("StructuredDocumentTag element")

        range_start = self.insert_structured_document_tag_ranges(doc)

        # Removes ranged structured document tag, but keeps content inside.
        range_start.remove_self_only()

        range_start = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_START, 0, False).as_structured_document_tag_range_start()
        self.assertEqual(null, range_start)

        range_end = doc.get_child(aw.NodeType.STRUCTURED_DOCUMENT_TAG_RANGE_END, 0, False).as_structured_document_tag_range_end()

        self.assertIsNone(range_end)
        self.assertEqual("StructuredDocumentTag element", doc.get_text().strip())

        range_start = self.insert_structured_document_tag_ranges(doc)

        paragraph_node = range_start.last_or_default()
        self.assertEqual("StructuredDocumentTag element", paragraph_node.get_text().strip())

        # Removes ranged structured document tag and content inside.
        range_start.remove_all_children()

        paragraph_node = range_start.last_or_default()
        self.assertIsNone(None, paragraph_node.get_text())

    def insert_structured_document_tag_ranges(self, doc: aw.Document) -> aw.markup.StructuredDocumentTagRangeStart:

        range_start = aw.markup.StructuredDocumentTagRangeStart(doc, aw.markup.SdtType.PLAIN_TEXT)
        range_end = aw.markup.StructuredDocumentTagRangeEnd(doc, range_start.id)

        doc.first_section.body.insert_before(range_start, doc.first_section.body.first_paragraph)
        doc.last_section.body.insert_after(range_end, doc.first_section.body.first_paragraph)
        return range_start

    #ExEnd
