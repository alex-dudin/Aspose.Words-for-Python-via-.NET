import aspose.words as aw
from docs_examples_base import DocsExamplesBase, MY_DIR

class WorkingWithParagraph(DocsExamplesBase):

    def test_count_lines_in_paragraph(self):

        #ExStart:CountLinesInParagraph
        document = aw.Document(MY_DIR + "Bibliography.docx")

        collector = aw.layout.LayoutCollector(document)
        enumerator = aw.layout.LayoutEnumerator(document)

        for paragraph in document.get_child_nodes(aw.NodeType.PARAGRAPH, True):

            paragraph = paragraph.as_paragraph()
            para_break = collector.get_entity(paragraph)

            stop = None
            prev_item = paragraph.previous_sibling
            if prev_item is not None:
                prev_break = collector.get_entity(prev_item)
                if prev_item.node_type == aw.NodeType.PARAGRAPH:
                    enumerator.current = collector.get_entity(prev_item) # para break
                    enumerator.move_parent() # last line
                    stop = enumerator.current
                elif prev_item.node_type == aw.NodeType.TABLE:
                    table = prev_item.as_table()
                    enumerator.current = collector.get_entity(table.last_row.last_cell.last_paragraph) # cell break
                    enumerator.move_parent()    # cell
                    enumerator.move_parent()    # row
                    stop = enumerator.current
                else:
                    raise RuntimeError()

            enumerator.current = para_break
            enumerator.move_parent()

            # We move from line to line in a paragraph.
            # When paragraph spans multiple pages the we will follow across them.
            count = 1
            while enumerator.current != stop:
                if not enumerator.move_previous_logical():
                    break
                count += 1

            max_chars = 16
            para_text = paragraph.get_text()
            if len(para_text) > max_chars:
                para_text = f"{para_text[:max_chars]}..."

            print(f"Paragraph '{para_text}' has {count} line(-s).")
        #ExEnd:CountLinesInParagraph
