import unittest
import io

import aspose.words as aw
import aspose.pydrawing as drawing

from api_example_base import ApiExampleBase, my_dir, artifacts_dir

MY_DIR = my_dir
ARTIFACTS_DIR = artifacts_dir

class ExNodeImporter(ApiExampleBase):

    def test_keep_source_numbering(self):

        for keep_source_numbering in (False, True):
            with self.subTest(keep_source_numbering=keep_source_numbering):
                #ExStart
                #ExFor:ImportFormatOptions.KeepSourceNumbering
                #ExFor:NodeImporter.#ctor(DocumentBase, DocumentBase, ImportFormatMode, ImportFormatOptions)
                #ExSummary:Shows how to resolve list numbering clashes in source and destination documents.
                # Open a document with a custom list numbering scheme, and then clone it.
                # Since both have the same numbering format, the formats will clash if we import one document into the other.
                src_doc = aw.Document(MY_DIR + "Custom list numbering.docx")
                dst_doc = src_doc.clone()

                # When we import the document's clone into the original and then append it,
                # then the two lists with the same list format will join.
                # If we set the "keep_source_numbering" flag to "False", then the list from the document clone
                # that we append to the original will carry on the numbering of the list we append it to.
                # This will effectively merge the two lists into one.
                # If we set the "keep_source_numbering" flag to "True", then the document clone
                # list will preserve its original numbering, making the two lists appear as separate lists.
                import_format_options = aw.ImportFormatOptions()
                import_format_options.keep_source_numbering = keep_source_numbering

                importer = aw.NodeImporter(src_doc, dst_doc, aw.ImportFormatMode.KEEP_DIFFERENT_STYLES, import_format_options)
                for paragraph in src_doc.first_section.body.paragraphs:
                    paragraph = paragraph.as_paragraph()
                    imported_node = importer.import_node(paragraph, True)
                    dst_doc.first_section.body.append_child(imported_node)

                dst_doc.update_list_labels()

                if keep_source_numbering:
                    self.assertEqual(
                        "6. Item 1\r\n" +
                        "7. Item 2 \r\n" +
                        "8. Item 3\r\n" +
                        "9. Item 4\r\n" +
                        "6. Item 1\r\n" +
                        "7. Item 2 \r\n" +
                        "8. Item 3\r\n" +
                        "9. Item 4", dst_doc.first_section.body.to_string(aw.SaveFormat.TEXT).strip())
                else:
                    self.assertEqual(
                        "6. Item 1\r\n" +
                        "7. Item 2 \r\n" +
                        "8. Item 3\r\n" +
                        "9. Item 4\r\n" +
                        "10. Item 1\r\n" +
                        "11. Item 2 \r\n" +
                        "12. Item 3\r\n" +
                        "13. Item 4", dst_doc.first_section.body.to_string(aw.SaveFormat.TEXT).strip())

                #ExEnd

    #ExStart
    #ExFor:Paragraph.IsEndOfSection
    #ExFor:NodeImporter
    #ExFor:NodeImporter.#ctor(DocumentBase, DocumentBase, ImportFormatMode)
    #ExFor:NodeImporter.ImportNode(Node, Boolean)
    #ExSummary:Shows how to insert the contents of one document to a bookmark in another document.

    def test_insert_at_bookmark(self):

        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        builder.start_bookmark("InsertionPoint")
        builder.write("We will insert a document here: ")
        builder.end_bookmark("InsertionPoint")

        doc_to_insert = aw.Document()
        builder = aw.DocumentBuilder(doc_to_insert)

        builder.write("Hello world!")

        doc_to_insert.save(ARTIFACTS_DIR + "NodeImporter.insert_at_merge_field.docx")

        bookmark = doc.range.bookmarks.get_by_name("InsertionPoint")
        ExNodeImporter.insert_document(bookmark.bookmark_start.parent_node, doc_to_insert)

        self.assertEqual("We will insert a document here: " +
                         "\rHello world!", doc.get_text().strip())

    def insert_document(insertion_destination: aw.Node, doc_to_insert: aw.Document):
        """Inserts the contents of a document after the specified node."""

        if insertion_destination.node_type == aw.NodeType.PARAGRAPH or insertion_destination.node_type == aw.NodeType.TABLE:

            destination_parent = insertion_destination.parent_node

            importer = aw.NodeImporter(doc_to_insert, insertion_destination.document, aw.ImportFormatMode.KEEP_SOURCE_FORMATTING)

            # Loop through all block-level nodes in the section's body,
            # then clone and insert every node that is not the last empty paragraph of a section.
            for src_section in doc_to_insert.sections:
                src_section = src_section.as_section()
                for src_node in src_section.body:
                    if src_node.node_type == aw.NodeType.PARAGRAPH:
                        para = src_node.as_paragraph()
                        if para.is_end_of_section and not para.has_child_nodes:
                            continue

                    new_node = importer.import_node(src_node, True)

                    destination_parent.insert_after(new_node, insertion_destination)
                    insertion_destination = new_node
        else:
            raise Exception("The destination node should be either a paragraph or table.")

    #ExEnd

    #def test_insert_at_merge_field(self):

    #    doc = aw.Document()
    #    builder = aw.DocumentBuilder(doc)
    #    builder.write("A document will appear here: ")
    #    builder.insert_field(" MERGEFIELD Document_1 ")

    #    sub_doc = aw.Document()
    #    builder = aw.DocumentBuilder(sub_doc)
    #    builder.write("Hello world!")

    #    sub_doc.save(ARTIFACTS_DIR + "NodeImporter.insert_at_merge_field.docx")

    #    doc.mail_merge.field_merging_callback = ExNodeImporter.InsertDocumentAtMailMergeHandler()

    #    # The main document has a merge field in it called "Document_1".
    #    # Execute a mail merge using a data source that contains a local system filename
    #    # of the document that we wish to insert into the MERGEFIELD.
    #    doc.mail_merge.execute(["Document_1"], [ARTIFACTS_DIR + "NodeImporter.insert_at_merge_field.docx"])

    #    self.assertEqual("A document will appear here: \r" +
    #                     "Hello world!", doc.get_text().strip())

    #class InsertDocumentAtMailMergeHandler(aw.mailmerging.IFieldMergingCallback):
    #    """If the mail merge encounters a MERGEFIELD with a specified name,
    #    this handler treats the current value of a mail merge data source as a local system filename of a document.
    #    The handler will insert the document in its entirety into the MERGEFIELD instead of the current merge value."""

    #    def field_merging(self, args: aw.mailmerging.FieldMergingArgs):

    #        if args.document_field_name == "Document_1":
    #            builder = aw.DocumentBuilder(args.document)
    #            builder.move_to_merge_field(args.document_field_name)

    #            sub_doc = aw.Document(str(args.field_value))

    #            ExNodeImporter.insert_document(builder.current_paragraph, sub_doc)

    #            if not builder.current_paragraph.has_child_nodes:
    #                builder.current_paragraph.remove()

    #            args.text = None

    #    def image_field_merging(self, args: aw.mailmerging.ImageFieldMergingArgs):
    #        # Do nothing.
