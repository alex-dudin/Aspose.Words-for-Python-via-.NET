import unittest
import io

import aspose.words as aw
import aspose.pydrawing as drawing

from api_example_base import ApiExampleBase, my_dir, artifacts_dir

MY_DIR = my_dir
ARTIFACTS_DIR = artifacts_dir

class ExTabStop(ApiExampleBase):

    def test_add_tab_stops(self):

        #ExStart
        #ExFor:TabStopCollection.Add(TabStop)
        #ExFor:TabStopCollection.Add(Double, TabAlignment, TabLeader)
        #ExSummary:Shows how to add custom tab stops to a document.
        doc = aw.Document()
        paragraph = doc.get_child(aw.NodeType.PARAGRAPH, 0, True).as_paragraph()

        # Below are two ways of adding tab stops to a paragraph's collection of tab stops via the "paragraph_format" property.
        # 1 -  Create a "TabStop" object, and then add it to the collection:
        tab_stop = aw.TabStop(aw.ConvertUtil.inch_to_point(3), aw.TabAlignment.LEFT, aw.TabLeader.DASHES)
        paragraph.paragraph_format.tab_stops.add(tab_stop)

        # 2 -  Pass the values for properties of a new tab stop to the "add" method:
        paragraph.paragraph_format.tab_stops.add(aw.ConvertUtil.millimeter_to_point(100),
                                                 aw.TabAlignment.LEFT, aw.TabLeader.DASHES)

        # Add tab stops at 5 cm to all paragraphs.
        for para in doc.get_child_nodes(aw.NodeType.PARAGRAPH, True):
            para = para.as_paragraph()
            para.paragraph_format.tab_stops.add(aw.ConvertUtil.millimeter_to_point(50),
                                                aw.TabAlignment.LEFT, aw.TabLeader.DASHES)

        # Every "tab" character takes the builder's cursor to the location of the next tab stop.
        builder = aw.DocumentBuilder(doc)
        builder.writeln("Start\tTab 1\tTab 2\tTab 3\tTab 4")

        doc.save(ARTIFACTS_DIR + "TabStopCollection.AddTabStops.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "TabStopCollection.AddTabStops.docx")
        tab_stops = doc.first_section.body.paragraphs[0].paragraph_format.tab_stops

        #TestUtil.verify_tab_stop(141.75d, TabAlignment.Left, TabLeader.Dashes, False, tab_stops[0])
        #TestUtil.verify_tab_stop(216.0d, TabAlignment.Left, TabLeader.Dashes, False, tab_stops[1])
        #TestUtil.verify_tab_stop(283.45d, TabAlignment.Left, TabLeader.Dashes, False, tab_stops[2])

    def test_tab_stop_collection(self):

        #ExStart
        #ExFor:TabStop.#ctor
        #ExFor:TabStop.#ctor(Double)
        #ExFor:TabStop.#ctor(Double,TabAlignment,TabLeader)
        #ExFor:TabStop.Equals(TabStop)
        #ExFor:TabStop.IsClear
        #ExFor:TabStopCollection
        #ExFor:TabStopCollection.After(Double)
        #ExFor:TabStopCollection.Before(Double)
        #ExFor:TabStopCollection.Clear
        #ExFor:TabStopCollection.Count
        #ExFor:TabStopCollection.Equals(TabStopCollection)
        #ExFor:TabStopCollection.Equals(Object)
        #ExFor:TabStopCollection.GetHashCode
        #ExFor:TabStopCollection.Item(Double)
        #ExFor:TabStopCollection.Item(Int32)
        #ExSummary:Shows how to work with a document's collection of tab stops.
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)

        tab_stops = builder.paragraph_format.tab_stops

        # 72 points is one "inch" on the Microsoft Word tab stop ruler.
        tab_stops.add(aw.TabStop(72.0))
        tab_stops.add(aw.TabStop(432.0, aw.TabAlignment.RIGHT, aw.TabLeader.DASHES))

        self.assertEqual(2, tab_stops.count)
        self.assertFalse(tab_stops[0].is_clear)
        self.assertNotEqual(tab_stops[0], tab_stops[1])

        # Every "tab" character takes the builder's cursor to the location of the next tab stop.
        builder.writeln("Start\tTab 1\tTab 2")

        paragraphs = doc.first_section.body.paragraphs

        self.assertEqual(2, paragraphs.count)

        # Each paragraph gets its tab stop collection, which clones its values from the document builder's tab stop collection.
        self.assertEqual(paragraphs[0].paragraph_format.tab_stops, paragraphs[1].paragraph_format.tab_stops)
        #Assert.are_not_same(paragraphs[0].paragraph_format.tab_stops, paragraphs[1].paragraph_format.tab_stops)

        # A tab stop collection can point us to tab_stops before and after certain positions.
        self.assertEqual(72.0, tab_stops.before(100.0).position)
        self.assertEqual(432.0, tab_stops.after(100.0).position)

        # We can clear a paragraph's tab stop collection to revert to the default tabbing behavior.
        paragraphs[1].paragraph_format.tab_stops.clear()

        self.assertEqual(0, paragraphs[1].paragraph_format.tab_stops.count)

        doc.save(ARTIFACTS_DIR + "TabStopCollection.TabStopCollection.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "TabStopCollection.TabStopCollection.docx")
        tab_stops = doc.first_section.body.paragraphs[0].paragraph_format.tab_stops

        self.assertEqual(2, tab_stops.count)
        #TestUtil.verify_tab_stop(72.0d, TabAlignment.Left, TabLeader.None, False, tab_stops[0])
        #TestUtil.verify_tab_stop(432.0d, TabAlignment.Right, TabLeader.Dashes, False, tab_stops[1])

        tab_stops = doc.first_section.body.paragraphs[1].paragraph_format.tab_stops

        self.assertEqual(0, tab_stops.count)

    def test_remove_by_index(self):

        #ExStart
        #ExFor:TabStopCollection.RemoveByIndex
        #ExSummary:Shows how to select a tab stop in a document by its index and remove it.
        doc = aw.Document()
        tab_stops = doc.first_section.body.paragraphs[0].paragraph_format.tab_stops

        tab_stops.add(aw.ConvertUtil.millimeter_to_point(30), aw.TabAlignment.LEFT, aw.TabLeader.DASHES)
        tab_stops.add(aw.ConvertUtil.millimeter_to_point(60), aw.TabAlignment.LEFT, aw.TabLeader.DASHES)

        self.assertEqual(2, tab_stops.count)

        # Remove the first tab stop.
        tab_stops.remove_by_index(0)

        self.assertEqual(1, tab_stops.count)

        doc.save(ARTIFACTS_DIR + "TabStopCollection.RemoveByIndex.docx")
        #ExEnd

        doc = aw.Document(ARTIFACTS_DIR + "TabStopCollection.RemoveByIndex.docx")

        #TestUtil.verify_tab_stop(170.1d, TabAlignment.Left, TabLeader.Dashes, False, doc.first_section.Body.Paragraphs[0].paragraph_format.TabStops[0])

    def test_get_position_by_index(self):

        #ExStart
        #ExFor:TabStopCollection.GetPositionByIndex
        #ExSummary:Shows how to find a tab, stop by its index and verify its position.
        doc = aw.Document()
        tab_stops = doc.first_section.body.paragraphs[0].paragraph_format.tab_stops

        tab_stops.add(aw.ConvertUtil.millimeter_to_point(30), aw.TabAlignment.LEFT, aw.TabLeader.DASHES)
        tab_stops.add(aw.ConvertUtil.millimeter_to_point(60), aw.TabAlignment.LEFT, aw.TabLeader.DASHES)

        # Verify the position of the second tab stop in the collection.
        self.assertAlmostEqual(aw.ConvertUtil.millimeter_to_point(60), tab_stops.get_position_by_index(1), 1)
        #ExEnd

    def test_get_index_by_position(self):

        #ExStart
        #ExFor:TabStopCollection.GetIndexByPosition
        #ExSummary:Shows how to look up a position to see if a tab stop exists there and obtain its index.
        doc = aw.Document()
        tab_stops = doc.first_section.body.paragraphs[0].paragraph_format.tab_stops

        # Add a tab stop at a position of 30mm.
        tab_stops.add(aw.ConvertUtil.millimeter_to_point(30), aw.TabAlignment.LEFT, aw.TabLeader.DASHES)

        # A result of "0" returned by "GetIndexByPosition" confirms that a tab stop
        # at 30mm exists in this collection, and it is at index 0.
        self.assertEqual(0, tab_stops.get_index_by_position(aw.ConvertUtil.millimeter_to_point(30)))

        # A "-1" returned by "GetIndexByPosition" confirms that
        # there is no tab stop in this collection with a position of 60mm.
        self.assertEqual(-1, tab_stops.get_index_by_position(aw.ConvertUtil.millimeter_to_point(60)))
        #ExEnd
