import unittest
import io

import aspose.words as aw
import aspose.pydrawing as drawing

from api_example_base import ApiExampleBase, my_dir, artifacts_dir

MY_DIR = my_dir
ARTIFACTS_DIR = artifacts_dir

class ExPdfLoadOptions(ApiExampleBase):

    def test_skip_pdf_images(self):

        for is_skip_pdf_images in (True, False):
            with self.subTest(is_skip_pdf_images=is_skip_pdf_images):
                #ExStart
                #ExFor:PdfLoadOptions.SkipPdfImages
                #ExSummary:Shows how to skip images during loading PDF files.
                options = aw.loading.PdfLoadOptions()
                options.skip_pdf_images = is_skip_pdf_images

                doc = aw.Document(MY_DIR + "Images.pdf", options)
                shape_collection = doc.get_child_nodes(aw.NodeType.SHAPE, True)

                if is_skip_pdf_images:
                    self.assertEqual(shape_collection.count, 0)
                else:
                    self.assertNotEqual(shape_collection.count, 0)

                #ExEnd
